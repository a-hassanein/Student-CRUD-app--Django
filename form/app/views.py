from django.shortcuts import render ,redirect
from .models import Myuser, Student
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def login(request):
    if (request.method == 'GET'):
        return render(request, 'pages/login.html')

    else:
        user = Myuser.objects.filter(userPass=request.POST['userPass'], userEmail=request.POST['userEmail'])
        if ( len(user) > 0 ):
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
        Myuser.objects.create(username=request.POST['myusername'], userPass=request.POST['userPass'], userEmail=request.POST['userEmail'])
        return render(request, 'pages/login.html')

def insert_student(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'pages/home.html')

    else:
        Student.objects.create(studentname=request.POST['studentname'], studentemail=request.POST['studentemail'], studentage=request.POST['studentage'], trackname=request.POST['trackname'])
        context['doneMsg'] = 'student inserted sucessfully'
        return render(request, 'pages/home.html', context)


# def insert_student(request):
#     if request.method == 'POST':
#         context = {}
#         studentname = request.POST['studentname']
#         studentage = request.POST['studentage']
#         studentemail = request.POST['studentemail']
#         trackname = request.POST['trackname']
#
#         try:
#             Student.objects.create(studentname=studentname, studentemail=studentemail,
#                                    studentage=studentage, track_name=trackname)
#             context['doneMsg'] = 'student inserted sucessfully'
#         except:
#             context['doneMsg'] = 'failed to insert student :('
#
#         students = Student.objects.all()
#         context['students'] = students
#         return render(request, 'pages/home.html', context)
#     # else:
#     #     index_students(request)
#
#     def index_students(request):
#         if request.method == 'GET':
#             context = {}
#             students = Student.objects.all()
#             print(students)
#             context['students'] = students
#             return render(request, 'pages/home.html', context)
#         else:
#             insert_student(request)