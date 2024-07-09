from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from app_cadastro.views import ProductsViewSet

router = routers.DefaultRouter()
router.register("products", ProductsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]

    