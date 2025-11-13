from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Product
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
