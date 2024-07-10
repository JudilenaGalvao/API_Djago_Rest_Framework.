from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Products
from .serializers import ProductsSerializers
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    
    
    @action(detail= False, methods=['get'])
    def filter_by_name(self,request):
        name = request.query_params.get('name', None)
        if name is not None:
            products = Products.objects.filter(name = name)
            serializer = ProductsSerializers(products,many=True)
            return Response(serializer.data)
        return Response({"message": "Nome do produto não fornecido"}, status=400)