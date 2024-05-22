# from django.db import models
# from django.db.models import SlugField
# from django.utils.text import slugify
# from ecommerce.models.category import Category
# from ecommerce.models.image import Image

# class Producto(models.Model):
#     id = models.AutoField(primary_key=True)
#     slug = SlugField(unique=True, max_length=255, populate_from='title')
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     iconColor = models.CharField(max_length=255)
#     icon = models.CharField(max_length=255)
#     rating = models.DecimalField(max_digits=2, decimal_places=1)
#     reviews = models.IntegerField()
#     price = models.IntegerField()
#     description = models.TextField()
#     availability = models.JSONField()
#     image = models.ForeignKey(
#         Image, verbose_name="Categoría asociada"
#     )
#     category = models.ForeignKey(
#         Category, verbose_name="Categoría asociada"
#     )
#     logo = models.URLField()
#     history = models.TextField()

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
