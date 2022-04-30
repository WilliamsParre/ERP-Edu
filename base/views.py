from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import signUpForm, OrginizationRegistrationForm, FacultyRegistriationForm
from .models import Course, Student


@login_required(login_url='login')
def home(request):
    courses = Course.objects.all()
    s = Student.objects.all()
    return render(request, 'base/dashboard.html')


def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('dashboard')

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
    form = signUpForm()

    if request.method == 'POST':
        form = signUpForm(request.POST)
        form2 = OrginizationRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active = False
            lecturer = Group.objects.get(name='Lecturer')
            user.save()
            user.groups.add(lecturer)
            user.save()
            messages.success(
                request, 'Registered successful! Account created successfully!')
            org = OrginizationRegistrationForm()
            faculty = FacultyRegistriationForm()
            return render(request, 'base/registration.html', {'org_form': org, 'faculty_form': faculty})
        else:
            messages.warning(request, 'An error occured during regestration')

    return render(request, 'base/login_register.html', {'form': form})


def org_registration(request):

    if request.method == 'POST':
        form = FacultyRegistriationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registered successful! Orginization added successfully.')
        else:
            messages.warning(request, 'An error occured during regestration')

    return redirect('signup')


def faculty_registration(request):

    if request.method == 'POST':
        form = OrginizationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registered successful! Message is sent to you orginisation for account activation.')
        else:
            messages.warning(request, 'An error occured during regestration')

    return redirect('signup')


@login_required(login_url='login')
def user_profile(request):
    # user = User.objects.get(id=pk)
    # context = {'user': user}
    return render(request, 'base/profile.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'base/dashboard.html')


@login_required(login_url='login')
def courses(request):
    return render(request, 'base/courses.html')


@login_required(login_url='login')
def attendance(request):
    return render(request, 'base/attendance.html')


@login_required(login_url='login')
@allowed_user(roles=['admin', 'Lecturer'])
def leave(request):
    return render(request, 'base/leave.html')


@login_required(login_url='login')
def fees(request):
    return render(request, 'base/fees.html')


@login_required(login_url='login')
def grades(request):
    return render(request, 'base/grades.html')


@login_required(login_url='login')
def qualification(request):
    return render(request, 'base/qualification.html')


def settings(request):
    return render(request, 'base/settings.html')
