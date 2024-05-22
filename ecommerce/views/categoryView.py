from rest_framework.viewsets import ModelViewSet

from ecommerce.serializer.categorySerializer import CategorySerializer
from ecommerce.models.category import Category

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
