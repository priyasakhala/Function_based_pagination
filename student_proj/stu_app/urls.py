from django.urls import path
from . import views

urlpatterns = [

    path('ho/',views.HomeView,name='home_url'),
    path('sv/',views.StuView,name='stuform_url'),
    path('ss/',views.ShowStudent,name='showstu_url'),
    path('ss/<int:page>/',views.ShowStudent,name='showstu_url'),
    path('us/<int:id>/',views.UpdateView,name='update_url'),
    path('del/<int:id>/',views.DeleteStudentView,name='confirmation_url')
]