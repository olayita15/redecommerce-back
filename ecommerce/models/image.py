from django.db import models

class Image(models.Model):
    url = models.URLField(max_length=400)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.url
