from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import (
    Order,
    OrderItem,
    Payment
)

from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
    PaymentSerializer
)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer