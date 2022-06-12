from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage


# Create your views here.

@login_required(login_url='login_url')
def StuView(request):
    form = StudentForm()
    template_name = 'stu_app/stuform.html'
    context={'form':form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstu_url')
    return render(request,template_name,context)


@login_required(login_url='login_url')
def ShowStudent(request, page=1):
    data = Student.objects.all()
    
    paginator = Paginator(data,3)
    try:
        data=paginator.page(page)
    except EmptyPage:
            data = paginator.page(paginator.num_pages)
    template_name = 'stu_app/showstu.html'
    context={'obj':data}
    return render(request,template_name,context)
'''
def list_users(request, id=1):
    users = Student.objects.all()
    paginator = Paginator(users, 2) # 2 users per page
    
    try:
        users = paginator.page(id)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        users = paginator.page(paginator.num_pages)
            
    return render(request, template_name='stu_app/showstu.html',context= {'obj': users})
'''
@login_required(login_url ='login_url')
def UpdateView(request,id):
    data = Student.objects.get(id=id)
    form = StudentForm(instance=data)
    template_name = 'stu_app/stuform.html'
    context = {'form':form}
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('showstu_url')
    return render(request, template_name, context)

@login_required(login_url ='login_url')
def DeleteStudentView(request,id):
    obj = Student.objects.get(id = id)
    template_name = 'stu_app/confirmation.html'
    context = {'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showstu_url')
    return render(request, template_name, context)

@login_required(login_url ='login_url')
def HomeView(request):
    template_name = 'stu_app/home.html'
    context={}
    return render(request,template_name,context)