from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        context['products'] = product

        return context
