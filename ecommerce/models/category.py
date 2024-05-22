from django.db import models
from django.db.models import SlugField
from django.utils.text import slugify

from ecommerce.models.image import Image


class Category(models.Model):
    slug = SlugField(unique=True, max_length=300)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    image = models.ForeignKey(
        Image, verbose_name="Imagen asociada", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
