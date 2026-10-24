from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from catalog.models import Product


class Wishlist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist"
    )

    def __str__(self):
        return self.user.email


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            "wishlist",
            "product"
        )

    def __str__(self):
        return self.product.name