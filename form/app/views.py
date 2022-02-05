from django.shortcuts import render ,redirect
from .models import Myuser, Student, Track
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.views import View
from .forms import insert_student1, insert_student2
from django.views.generic import ListView

# Create your views here.
class TrackList(ListView):
    model = Track


def mylogout(request):
    logout(request)
    return render(request, 'login/login.html')


def home(request):
    return render(request, 'pages/home.html')


# def signup(request):
#     context = {}
#     if (request.method == 'GET'):
#         return render(request, 'pages/signup.html')
#
#     else:
#         # Myuser.objects.create(myusername=request.POST['myusername'], userPass=request.POST)
#         myuser = Myuser.objects.create(myusername=request.POST.get('myussername'), userPass=request.POST.get('signupPass'), userEmail=request.POST.get('signupEmail'))
#         print(myuser.myusername)
#         User.objects.create_user(username=request.POST['myussername'], password=request.POST['signupPass'], is_staff=True)
#         return render(request, 'pages/login.html')

def signup(request):
    if (request.method == 'GET'):
        return render(request, 'pages/signup.html')
    else:
        username = request.POST['myussername']
        email = request.POST['signupEmail']
        password = request.POST['signupPass']
        Myuser.objects.create(myusername=username, userEmail=email, userPass=password)
        User.objects.create_user(username, email, password, is_staff=True)
        return redirect("login")

# def login(request):
#     if (request.method == 'GET'):
#         return render(request, 'pages/login.html')
#
#     else:
#         user = Myuser.objects.filter(userPass=request.POST.get('loginpass'), myusername=request.POST.get('loginname'))
#         authuser = authenticate(username=request.POST['loginname'], userPass=request.POST['loginpass'])
#         if ( len(user) > 0  and authuser is not None):
#             request.session['username'] = request.POST['loginname']
#             authlogin(request, authuser)
#             return render(request, 'pages/home.html')
#         else:
#             context = {}
#             context['msg'] = 'Invalid username or password'
#             return render(request, 'pages/login.html', context)

def login(request):
    if (request.method == 'GET'):
        return render(request, 'pages/login.html')
    elif(request.method == 'POST'):
        email = request.POST['loginemail']
        password = request.POST['loginpass']
        print(email, "  Password ", password)
        try:
            user = Myuser.objects.get(userEmail=email, userPass=password)
            admin_user = authenticate(username=user.myusername, password=password)
            if user and admin_user is not None:
                request.session['username'] = user.myusername
                authlogin(request, admin_user)
                return redirect('/')
        except Myuser.DoesNotExist:
            return redirect("login")



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

class InsertStudent1(View):
    def get(self, request):
        context = {}
        form = insert_student1()
        context['form'] = form
        return render(request, 'pages/insertform.html', context)

    def post(self, request):
        context={}
        Student.objects.create(studentname=request.POST['studentname'], studentemail=request.POST['studentemail'],studentage=request.POST['studentage'], trackname=request.POST['trackname'])
        students = Student.objects.all()

        return render(request, 'pages/insertform.html', context)

class InsertStudent2(View):
    def get(self,request):
        context = {}
        form2 = insert_student2()
        context['form2'] = form2
        return render(request, 'pages/insertform2.html', context)

    def post(self,request):
        context={}
        afterpostform = insert_student2(request.POST)
        afterpostform.save()
        return render(request, 'pages/insertform2.html', context)


