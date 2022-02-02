from django.shortcuts import render ,redirect
from .models import Myuser, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
# Create your views here.
def mylogout(request):
    logout(request)
    return render(request, 'login/login.html')


def home(request):
    return render(request, 'pages/home.html')

def login(request):
    if (request.method == 'GET'):
        return render(request, 'pages/login.html')

    else:
        user = Myuser.objects.filter(userPass=request.POST['userPass'], userEmail=request.POST['userEmail'])
        authuser = authenticate(userEmail=request.POST['userEmail'], userPass=request.POST['userPass'])
        if ( len(user) > 0  and authuser is not None):
            request.session['username'] = request.POST['username']
            authlogin(request, authuser)
            return render(request, 'pages/home.html')
        else:
            context = {}
            context['msg'] = 'Invalid username or password'
            return render(request, 'pages/login.html', context)

def signup(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'pages/signup.html')

    else:
        Myuser.objects.create(username=request.POST['username'], userPass=request.POST['userPass'], userEmail=request.POST['userEmail'])
        # User.objects.create_user(username=request.POST['myusername'], userPass=request.POST['userPass'], is_staff=True)
        return render(request, 'pages/login.html')

def insert_student(request):
    context = {}
    context['ID'] = 1
    if (request.method == 'GET'):
        return render(request, 'pages/home.html')

    else:
        Student.objects.create(studentname=request.POST['studentname'], studentemail=request.POST['studentemail'], studentage=request.POST['studentage'], trackname=request.POST['trackname'])
        students = Student.objects.all()
        context['students'] = students
        context['doneMsg'] = 'student inserted sucessfully'
        return render(request, 'pages/home.html', context)

def delete_student(req,id):
    context = {}
    Student.objects.filter(id=id).delete()
    students = Student.objects.all()
    context['students'] = students
    return render(req, 'pages/studentlist.html', context)

def list_students(req):
    context={}
    students = Student.objects.all()
    context['students'] = students
    return render(req, 'pages/studentlist.html', context)

def update_student(request,id):
    if request.method == 'POST':
        newstudentname = request.POST.get('newstudentname')
        student = Student.objects.get(id=id)
        if student:
            student.studentname = newstudentname
            student.save()
            return render(request, 'pages/home.html')
        else:
            return render(request, 'pages/studentlist.html')
    else:
        return render(request, 'pages/studentlist.html')