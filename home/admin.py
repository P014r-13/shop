from django.contrib import admin
from .models import Product,Category,Address,Order,Order_Item,Code,Comment



admin.site.register((Product,Category))
admin.site.register(Address)
admin.site.register((Order,Order_Item,Code,Comment))