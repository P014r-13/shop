from django.contrib import admin
from .models import Product
from home.models import Category


admin.site.register((Product,Category))