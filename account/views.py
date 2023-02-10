from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import UserRegisterMForm,LoginForm,StudentForm
from django.contrib import messages  
from django.contrib.auth import authenticate,login,logout
from .models import StudentModel
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrapper  
      

class UserRegister(View):
    def get(self,request,*args,**kwargs):
        form = UserRegisterMForm()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = UserRegisterMForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Registered Successfully!')
            return redirect('login')    
        else:
            messages.error(request,'User Registration Failed!')
            return render(request,'register.html',{'form':form})
        

class UserLogin(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            a = form.cleaned_data.get('Username')
            b = form.cleaned_data.get('Password')
            user = authenticate(username=a,password=b)
            if user:
                login(request,user)
                messages.success(request,'User Logined')
                return redirect('studentview')
            else:
                messages.error(request,'User not Logined')
                return redirect('login')
        else:
            messages.error(request,'User not logged')
            return render(request,'login.html',{'form':form})

@method_decorator(signin_required,name='dispatch')
class AddStudent(View):
    def get(self,request,*args,**kwargs):
        form = StudentForm()
        return render(request,'addstudent.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Added')
            return redirect('studentview')    
        else:
            messages.error(request,'Not added')
            return render(request,'addstudent.html',{'form':form})

@method_decorator(signin_required,name='dispatch')
class StudentView(View):
    def get(self,request,*args,**kwargs):
        students = StudentModel.objects.all()
        return render(request,'studentview.html',{'students':students})

@method_decorator(signin_required,name='dispatch')
class StudentUpdate(View):
    def get(self,request,*args,**kwargs):
        studentid = kwargs.get('id')
        student = StudentModel.objects.get(id=studentid)
        form = StudentForm(instance=student)
        return render(request,'studentedit.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        studentid = kwargs.get('id')
        student = StudentModel.objects.get(id=studentid)
        form = StudentForm(instance=student,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated')
            return redirect('studentview')    
        else:
            messages.error(request,'Not Updated')
            return render(request,'studentedit.html',{'form':form})

@method_decorator(signin_required,name='dispatch')
class StudentDelete(View):
    def get(self,request,*args,**kwargs):
        studentid = kwargs.get('id')
        student = StudentModel.objects.get(id=studentid)
        student.delete()
        return render(request,'studentview.html')

class UserLogout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('login')