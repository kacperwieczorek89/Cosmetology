from django.db import models
from polymorphic.models import PolymorphicModel
from django.urls import reverse

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
        return f"{self.name} | {self.product_types}"


class Product(PolymorphicModel):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Nazwa Produktu : {self.name} ; Cena: {self.price} PLN ; {self.producer} ; {self.product_type}"

class PreparationUnit(models.Model):
    unit = models.CharField(max_length=3)


class Preparation(Product):
    dimension = models.IntegerField()
    unit = models.ForeignKey(PreparationUnit, on_delete=models.CASCADE)

class Activity(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"Czynność:{self.name}  | Czas wykonania:{self.time} min | {self.description}"

class Treatment(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, through='TreatmentProduct',)
    activities = models.ManyToManyField(Activity, through='TreatmentActivity')
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True)


    def __str__(self):
        return f"{self.name} |{self.price}"

    def get_absolute_url(self):
        return reverse('treatment_detail_view',args=(self.pk,))

class TreatmentProduct(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class TreatmentActivity(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)





