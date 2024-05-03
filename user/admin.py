from django.contrib import admin
from .models import (
    User,
    Code
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_filter = ('email',)
    search_fields = ('email',)

@admin.register(Code)
class UserAdmin(admin.ModelAdmin):
    list_display = ('code', 'time', 'user')
    list_filter = ('user',)
    search_fields = ('code',)

