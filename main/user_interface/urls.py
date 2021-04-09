from django.urls import path

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductsViewSet, basename='products')
router.register('reviews', views.ReviewsViewSet, basename='reviews')
router.register('custom', views.CustomViewSet, basename='custom')

urlpatterns = router.urls
