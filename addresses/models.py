from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Address(models.Model):

    HOME = "HOME"
    WORK = "WORK"
    OTHER = "OTHER"

    ADDRESS_CHOICES = [
        (HOME, HOME),
        (WORK, WORK),
        (OTHER, OTHER),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    full_name = models.CharField(
        max_length=255
    )

    phone = models.CharField(
        max_length=20
    )

    address_line_1 = models.CharField(
        max_length=255
    )

    address_line_2 = models.CharField(
        max_length=255,
        blank=True
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    postal_code = models.CharField(
        max_length=20
    )

    country = models.CharField(
        max_length=2
    )

    address_type = models.CharField(
        max_length=10,
        choices=ADDRESS_CHOICES,
        default=HOME
    )

    is_default = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.full_name