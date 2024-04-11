from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth import login,authenticate,logout

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        return render(request, 'login.html')

class LogOutView(View,LoginRequiredMixin):
    @staticmethod
    def get(request, *args, **kwargs):
        if request.user.is_authenticated:
            request.user.is_logged_in = False
            request.user.save()
            logout(request)
        return HttpResponseRedirect(reverse('login'))
