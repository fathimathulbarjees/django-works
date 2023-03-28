from django.db import models


class Vechicle(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    model=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    oil=models.CharField(max_length=200)
    qty=models.PositiveIntegerField(default=1)
# Create your models here.
