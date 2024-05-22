from rest_framework import serializers

from ecommerce.models.image import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = [
            "id",
            "url",
            "image",
        ]
