from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from user.models import User

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    count = models.IntegerField()
    disc = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.name
class Order_Item(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
