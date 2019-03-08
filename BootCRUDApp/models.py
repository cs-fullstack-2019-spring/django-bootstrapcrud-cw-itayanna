from django.db import models

# Create your models here.

# this is the model used for the form

class sellItem(models.Model):
    picture = models.CharField(max_length=800, default="")
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=6000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
