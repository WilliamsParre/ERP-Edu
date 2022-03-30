from cgitb import reset
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Course, Student


@login_required(login_url='login')
def home(request):
    courses = Course.objects.all()
    s = Student.objects.all()
    return render(request, 'base/dashboard.html')


def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password doesnot exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during regestration')

    return render(request, 'base/login_register.html', {'form': form})


@login_required(login_url='login')
def user_profile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'base/dashboard.html')


@login_required(login_url='login', redirect_field_name='courses')
def courses(request):
    return render(request, 'base/courses.html')


def attendance(request):
    return render(request, 'base/attendance.html')
