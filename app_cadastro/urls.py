from django.urls import path, include
from .views import ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/filter_by_name/', ProductsViewSet.as_view({'get': 'filter_by_name'}), name='products_by_name'),
]