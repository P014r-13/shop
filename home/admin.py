from .models import (
    Product,
    Category,
    Address,
    Order,
    OrderItem,
    Comment
)
from django.contrib import (
    admin
)

admin.site.register(Comment)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    raw_id_fields = ('user',)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('name', 'disc')
    search_fields = ('name', 'category')
    inlines = [CommentInline]


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'parent')


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('city',)
    search_fields = ('user', 'city')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status', 'code')
    list_filter = ('user', 'status', 'date')
    search_fields = ('user', 'status')
    inlines = [OrderItemInline]


