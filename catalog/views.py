from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.viewsets import (
    ModelViewSet
)

from .models import (
    Category,
    Brand,
    Product
)

from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer
)

from .permissions import (
    IsAdminOrReadOnly
)


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [
        IsAdminOrReadOnly
    ]


class BrandViewSet(ModelViewSet):

    queryset = Brand.objects.all()

    serializer_class = BrandSerializer

    permission_classes = [
        IsAdminOrReadOnly
    ]


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [
        IsAdminOrReadOnly
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "category",
        "brand",
        "is_featured",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
        "sku",
    ]

    ordering_fields = [
        "price",
        "created_at",
    ]

    ordering = [
        "-created_at"
    ]