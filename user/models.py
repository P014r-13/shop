from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    otp = models.IntegerField(blank=True,null=True)
    verify = models.BooleanField(default=False)
    class AccountType(models.TextChoices):
        member = 'member', 'Member'
        operator = 'operator', 'Operator'
        admin = 'admin', 'Admin'
        staff = 'staff', 'Staff'
    account_type = models.CharField(max_length=10, choices=AccountType.choices, default=AccountType.member)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email


groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name="custom_user_groups",
help_text='The groups this user belongs to. A user will get all permissions granted '
'to each of their groups.')

user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True,
related_name="custom_user_permissions",
help_text='Specific permissions for this user.')



