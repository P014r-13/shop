from django.urls import path
from .views import LoginView,LogOutView,SignUpView,OtpVerifyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('verify/', OtpVerifyView.as_view(), name='otp_verify')
]