from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.
class ProductType(models.Model):
    product_type = models.CharField(max_length=15)
    product_type_plural = models.CharField(max_length=15, default="N/A")

    def __str__(self):
        return f"{self.product_type}"

class Producer(models.Model):
    name = models.CharField(max_length=64)
    product_types = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ; {self.product_types}"


class Product(PolymorphicModel):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class PreparationUnit(models.Model):
    unit = models.CharField(max_length=3)


class Preparation(Product):
    dimension = models.IntegerField()
    unit = models.ForeignKey(PreparationUnit, on_delete=models.CASCADE)
