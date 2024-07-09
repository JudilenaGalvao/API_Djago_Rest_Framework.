from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Products
from .serializers import ProductsSerializers

import json
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializers