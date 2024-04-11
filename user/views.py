import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login,authenticate,logout
from .models import User

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

class SignUpView(View):
    def get(self, request):
        return render(request,'sign-up.html')
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password1 != password:
            return render(request,'sign-up.html')
        else:
            user = User.objects.create_user(email=email,password=password)
            print(user)
            login(request,user)
            user.otp = random.randint(1000,9999)
            send_mail(
                'Instagram',
                f'Your otp code : {user.otp}.',
                'fortanarmin@gmail.com',
                [email],
                fail_silently=False,
            )
            user.save()
            return redirect('otp_verify')

class OtpVerifyView(View):
    def get(self,request):
        return render(request,'otp-verify.html')
    def post(self,request):
        otp1 = request.POST['otp1']
        otp2 = request.POST['otp2']
        otp3 = request.POST['otp3']
        otp4 = request.POST['otp4']
        end_otp = f'{otp1}{otp2}{otp3}{otp4}'
        print(end_otp)
        print(request.user.otp)
        if request.user.otp == int(end_otp):
            print('in ifffffffffffffffffffffffffff')
            user = request.user
            user.verify = True
            user.save()
            return HttpResponseRedirect('/')
        else :
            return render(request,'otp-verify.html')
class LogOutView(View,LoginRequiredMixin):
    @staticmethod
    def get(request, *args, **kwargs):
        if request.user.is_authenticated:
            request.user.is_logged_in = False
            request.user.save()
            logout(request)
        return HttpResponseRedirect(reverse('login'))
