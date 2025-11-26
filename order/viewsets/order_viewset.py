from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from order.serializers import OrderSerializer
from core.models import Order

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()