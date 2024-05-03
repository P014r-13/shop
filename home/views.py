from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Product, Category
from user.models import User


class HomeView(TemplateView,LoginRequiredMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        context['products'] = product

        return context
class ProductView(TemplateView):
    template_name = 'products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        category = Category.objects.all()
        context['products'] = product
        context['categories'] = category

        return context

class AccountView(TemplateView):
    template_name = 'account.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context

class OrderView(TemplateView):
    template_name = 'order.html'