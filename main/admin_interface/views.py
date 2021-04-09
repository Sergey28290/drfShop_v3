from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from user_interface.views import BaseView
from .models import Collections
from .filters import CollectionsFilter
from .serializers import CollectionsSerializer
from django.core import serializers


class CollectionsViewSet(BaseView, ModelViewSet):
	""" Collection view """

	queryset = Collections.objects.all()
	serializer_class = CollectionsSerializer
	filter_backends = (DjangoFilterBackend, )
	filterset_class = CollectionsFilter
