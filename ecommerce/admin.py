from django.contrib import admin

from ecommerce.models.category import Category
from ecommerce.models.image import Image

admin.site.register(Category)
admin.site.register(Image)