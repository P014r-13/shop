from django.urls import path
from .views import HomeView,ProductView,AccountView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('accounts/', AccountView.as_view(), name='account')
]