from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


from rest_framework.routers import DefaultRouter

from catalog.views import (
    CategoryViewSet,
    BrandViewSet,
    ProductViewSet
)

from reviews.views import ReviewViewSet

from addresses.views import AddressViewSet

from cart.views import (
    CartViewSet,
    CartItemViewSet
)

from wishlist.views import (
    WishlistViewSet,
    WishlistItemViewSet
)

from coupons.views import CouponViewSet

from orders.views import (
    OrderViewSet,
    OrderItemViewSet,
    PaymentViewSet
)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'wishlist-items', WishlistItemViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    path(
        "api/auth/",
        include("accounts.urls")
    ),

    path(
        'api/',
        include(router.urls)
    ),
]
