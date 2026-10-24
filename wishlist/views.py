from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import (
    Wishlist,
    WishlistItem
)

from .serializers import (
    WishlistSerializer,
    WishlistItemSerializer
)


class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class WishlistItemViewSet(ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer