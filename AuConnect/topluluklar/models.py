from django.db import models

# Create your models here.

class Topluluklar(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    description = models.TextField()
    