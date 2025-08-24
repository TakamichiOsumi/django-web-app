from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Product(models.Model):

    products_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    top_photo = models.ImageField(upload_to = 'products/%Y/%m/%d/')
    extra_photo1 = models.ImageField(upload_to = 'products/%Y/%m/%d/',
                                     null = True, blank = True)
    extra_photo2 = models.ImageField(upload_to = 'products/%Y/%m/%d/',
                                     null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    price = models.PositiveIntegerField()
    company = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    score = models.PositiveIntegerField()
    comments = models.CharField(max_length = 200, blank = True)
