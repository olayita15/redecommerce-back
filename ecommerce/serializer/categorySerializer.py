from rest_framework import serializers
from django.utils.text import slugify

from ecommerce.models.category import Category
from ecommerce.models.image import Image
from ecommerce.serializer.imageSerializer import ImageSerializer

class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    slug = serializers.SlugField(read_only=True)
    
    def create(self, validated_data):
        image_data = validated_data.pop('image')
        name = validated_data.get('name')
        slug = slugify(name, allow_unicode=True)
        validated_data['slug'] = slug

        # Create the image using the ImageSerializer
        image_serializer = ImageSerializer(data=image_data)
        image_serializer.is_valid(raise_exception=True)
        image_instance = image_serializer.save()  # Save the image and get the instance

        # No need to create a separate Image object
        validated_data['image'] = image_instance  # Update validated data with the saved image

        category = Category.objects.create(**validated_data)
        return category



    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image"
        ]
