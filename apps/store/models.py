from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Catgeories'

    def __str__(self):
        return self.title
    