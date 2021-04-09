from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Review, Custom
from .filters import ProductFilter, ReviewFilter, CustomFilter
from .serializers import ProductSerializer, ReviewSerializer, CustomSerializer
from rest_framework.response import Response
from django.core import serializers


class DeletedView:
	""" Deleted view 

	this class needed to delete 
	object from db
	"""
	
	def destroy(self, request, *args, **kwargs):
		""" Destroy method """
		
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response({"http_method":"DELETE"})
	

class RetrieveView:
	""" Retrieve view
	
	this class needed to get info
	about object from db
	"""

	def retrieve(self, request, *args, **kwargs):
		""" Retrieve method """
		
		print("Retrieve...")
		return super().retrieve(request)


class ListView:
	""" List view """

	def list(self, request):
		""" List method """

		print("List...")
		return super().list(request)


class BaseView(DeletedView, RetrieveView, ListView):
	""" Base view

	this class needed to combine
	classes
	"""

	pass


class ProductsViewSet(BaseView, ModelViewSet):
	""" Product view """

	queryset = Product.objects.all()
	serializer_class = ProductSerializer	
	filter_backends = (DjangoFilterBackend, )
	filterset_class = ProductFilter	


class ReviewsViewSet(BaseView, ModelViewSet):
	""" Review view """

	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	filter_backends = (DjangoFilterBackend, )
	filterset_class = ReviewFilter

	def destroy(self, request, *args, **kwargs):
		""" Destroy method """

		print("Destroy...")
		if Review.objects.get(id=kwargs['pk']).user == request.user:
			instance = self.get_object()
			self.perform_destroy(instance)
			return Response({"http_method":"DELETE"})
		else:
			return Response({"You can not delete them because it is not your review"})


class CustomViewSet(BaseView, ModelViewSet):
	""" Custom view """

	queryset = Custom.objects.all()
	serializer_class = CustomSerializer
	filter_backends = (DjangoFilterBackend, )
	filterset_class = CustomFilter

	def destroy(self, request, *args, **kwargs):
		""" Destroy method """

		print("Destroy...")
		if Custom.objects.get(id=kwargs['pk']).user == request.user:
			instance = self.get_object()
			self.perform_destroy(instance)
			return Response({"http_method":"DELETE"})
		else:
			return Response({"You can not delete them because it is not your custom"})

	def list(self, request, *args, **kwargs):
		""" List method """

		if request.user.is_superuser:
			return super().list(request)
		else:
			data = list(Custom.objects.filter(user=request.user))
			output = serializers.serialize("json", data)
			return Response({output})

