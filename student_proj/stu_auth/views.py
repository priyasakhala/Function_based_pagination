from contextlib import redirect_stderr
from email import message
import email
from multiprocessing import context
from re import template
from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from random import randint

# Create your views here.
otp = randint(1000,9999)
#otp = str(otp)
def RegisterView(request):
    form = UserCreationForm()
    template_name = 'stu_auth/register.html'
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    context ={'form': form}
    return render(request,template_name,context)


def LoginView(request):
    template_name = 'stu_auth/login.html'
    context = {}
    if request.method =='POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')
        eml = request.POST.get('e')

        global new
        user = authenticate(username=un,password=pw)
        new = user
        if user is not None:
            subject = ' WELCOME TO ELITE INSTITUTE'
            message = f'Hi {user.username},{eml}, your otp is: {otp} THANK U!!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [eml]
            send_mail(subject, message, email_from, recipient_list,fail_silently=True)#send_mail(subject, message, from_email, to_list, fail_silently=Tre)
            return redirect('otp_url')
    context = {}
    return render(request,template_name,context)
            
def LogoutView(request):
    logout(request)
    return redirect('login_url')

def OTPView(request):
    otp1 = request.POST.get('otp')
    template_name = 'stu_auth/otp.html'
    context = {}
    if request.method == 'POST':
        otp1 = int(otp1)
        #print('otp1:', otp1 ,'otp:',otp)
        if otp == otp1:
            login(request,new)
            return redirect('showstu_url')
    return render(request,template_name,context)