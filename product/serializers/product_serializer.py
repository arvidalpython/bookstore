from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = [
        'title',
        'description',
        'price',
        'active',
        'category',
        ]