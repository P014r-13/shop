from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from user.models import User
from core.models import TimeStampMixin, LogicalMixin


class Product(TimeStampMixin, LogicalMixin, models.Model):

    name = models.CharField(max_length=120)
    price = models.IntegerField()
    count = models.IntegerField()
    disc = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True)
    discount = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class OrderItem(TimeStampMixin, LogicalMixin, models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(TimeStampMixin, LogicalMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    code = models.OneToOneField('user.Code', on_delete=models.PROTECT)

    def __str__(self):
        return f"Order {self.id}"


class Comment(TimeStampMixin, LogicalMixin, models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])

    def __str__(self):
        return self.content


class Address(TimeStampMixin, LogicalMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.TextField()

    class City(models.TextChoices):
        Tehran = "TN", "Tehran"
        Karaj = "KJ", "Karaj"
        Gilan = "GN", 'Gilan'
        Tabriz = "TZ", "Tabriz"
        Mashhad = "MD", "Mashhad"
    city = models.CharField(
        max_length=2,
        choices=City.choices,
        default=City.Tehran,
    )

    def __str__(self):
        return self.address
