from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.RegisterView,name = 'register_url'),
    path('login/',views.LoginView,name = 'login_url'),
    path('logout/',views.LogoutView,name = 'logout_url'),
    path('otp/',views.OTPView,name='otp_url')
]