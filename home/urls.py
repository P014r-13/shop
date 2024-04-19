from django.urls import path
from .views import HomeView,ProductView,AccountView,OrderView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('accounts/', AccountView.as_view(), name='account'),
    path('order/', OrderView.as_view(), name='Order')
]