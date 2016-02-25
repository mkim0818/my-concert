from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=3000)
    headshot = models.ImageField(upload_to='artist-headshots', blank=True)
    banner = models.ImageField(upload_to='artist-banners', blank=True)
    slug = models.SlugField(max_length=50, allow_unicode=True, unique=True)

    def __str__(self):
        return self.name
