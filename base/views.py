import re
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import StudentRegistriationForm, signUpForm, OrginizationRegistrationForm, FacultyRegistriationForm, NonTeachingFacultyRegistriationForm, UserProfileChangeForm
from leave.forms import Leave, NonTeachingLeave, LeaveForm, NonTeachingLeaveForm
from base.models import Course, Lecturer, NonTeaching, Orginization, Student
from django.contrib.auth import update_session_auth_hash


@login_required(login_url='login')
def home(request):
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
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Registered successful! Account created successfully!')
            org = OrginizationRegistrationForm()
            faculty = FacultyRegistriationForm()
            non_teaching = NonTeachingFacultyRegistriationForm()
            return render(request, 'base/registration.html', {'org': org, 'faculty': faculty, 'non_teaching': non_teaching})
        else:
            messages.error(request, 'An error occured during regestration')

    return render(request, 'base/login_register.html', {'form': form})


def org_registration(request):

    if request.method == 'POST':
        form = OrginizationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.user.username)
            user.username = user.username.lower()
            user.is_active = True
            # user.is_staff = True
            admin = Group.objects.get(name='admin')
            user.save()
            user.groups.add(admin)
            user.save()
            logout(request)
            messages.success(
                request, 'Registered successful! Orginization added successfully.')
        else:
            messages.error(request, 'An error occured during regestration')

    return redirect('signup')


def faculty_registration(request):

    if request.method == 'POST':
        form = FacultyRegistriationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.user.username)
            user.username = user.username.lower()
            user.is_active = False
            lecturer = Group.objects.get(name='lecturer')
            user.save()
            user.groups.add(lecturer)
            user.save()
            logout(request)
            messages.success(
                request, 'Registered successful! Message is sent to you orginisation for account activation.')
        else:
            messages.error(request, 'An error occured during regestration')

    return redirect('signup')


def non_teaching_registration(request):

    if request.method == 'POST':
        form = NonTeachingFacultyRegistriationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.user.username)
            user.username = user.username.lower()
            user.is_active = False
            non_teaching = Group.objects.get(name='non_teaching')
            user.save()
            user.groups.add(non_teaching)
            user.save()
            logout(request)
            messages.success(
                request, 'Registered successful! Message is sent to you orginisation for account activation.')
        else:
            messages.error(request, 'An error occured during regestration')

    return redirect('signup')


@login_required(login_url='login')
def user_profile(request, pk):
    # user = User.objects.get(id=pk)
    user = User.objects.get(id=pk)
    group = user.groups.all()[0].name
    profile = ''
    if group == 'admin':
        print('Hi you are admin')
    elif group == 'lecturer':
        if Lecturer.objects.all().count() > 0:
            profile = Lecturer.objects.get(user=user.id)
    elif group == 'student':
        # profile = User.objects.filter(student__first_name=user.first_name)
        if Student.objects.all().count() > 0:
            profile = Student.objects.get(user=user.id)
    elif group == 'non_teaching':
        profile = NonTeaching.objects.get(user=user.id)
    context = {'user': user, 'profile': profile}
    return render(request, 'base/profile.html', context)


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
@allowed_user(roles=['lecturer', 'non_teaching'])
def leave(request):
    no_of_leaves = 0
    if request.user.groups.all()[0].name == 'non_teaching':
        user = NonTeaching.objects.get(user=request.user.id)
        leaves = NonTeachingLeave.objects.filter(e_id=user.nt_e_id)
        total_leaves = NonTeachingLeave.objects.filter(
            e_id=user.nt_e_id).count()
        no_of_leaves_granted = NonTeachingLeave.objects.filter(
            e_id=user.nt_e_id, leave_Status='Approved').count()
        no_of_leaves_pending = NonTeachingLeave.objects.filter(
            e_id=user.nt_e_id, leave_Status='Pending').count()
        no_of_leaves_declined = NonTeachingLeave.objects.filter(
            e_id=user.nt_e_id, leave_Status='Declined').count()
    else:
        user = Lecturer.objects.get(user=request.user.id)
        leaves = Leave.objects.filter(e_id=user.e_id)
        total_leaves = Leave.objects.filter(e_id=user.e_id).count()
        no_of_leaves_granted = Leave.objects.filter(
            e_id=user.e_id, leave_Status='Approved').count()
        no_of_leaves_pending = Leave.objects.filter(
            e_id=user.e_id, leave_Status='Pending').count()
        no_of_leaves_declined = Leave.objects.filter(
            e_id=user.e_id, leave_Status='Declined').count()
    return render(request, 'base/leave.html', {'leaves': leaves, 'total_leaves': total_leaves, 'no_of_leaves_granted': no_of_leaves_granted, 'no_of_leaves_pending': no_of_leaves_pending, 'no_of_leaves_declined': no_of_leaves_declined})


@login_required(login_url='login')
@allowed_user(roles=['lecturer', 'non_teaching'])
def apply_leave(request):
    if request.user.groups.all()[0].name == 'non_teaching':
        form = NonTeachingLeaveForm()
    else:
        form = LeaveForm()

    if request.method == "POST":
        if request.user.groups.all()[0].name == 'non_teaching':
            form = NonTeachingLeaveForm(request.POST)
        else:
            form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            form = LeaveForm()
            messages.success(
                request, 'Leave has been applied successfully! Message is sent to you orginisation for leave approval.')
        else:
            messages.error(
                request, 'An error occured during leave processing.')

    return render(request, 'base/apply_leave.html', {'form': form})


@login_required(login_url='login')
def fees(request):
    return render(request, 'base/fees.html')


@login_required(login_url='login')
def grades(request):
    return render(request, 'base/grades.html')


@login_required(login_url='login')
def qualification(request):
    return render(request, 'base/qualification.html')


@login_required(login_url='login')
def settings(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Passord changed successfully!')
            form = PasswordChangeForm(user=request.user)
            return render(request, 'base/settings.html', {'form': form})
        else:
            messages.error(request, 'Error occured during form validation.')

    return render(request, 'base/settings.html', {'form': form})


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def teaching_accept_leave(request, pk):
    user_leave = Leave.objects.get(id=pk)
    user_leave.leave_Status = 'Approved'
    user_leave.save()
    messages.success(request, 'Leave has been granted successfully!')
    return redirect('admin_leave')


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def non_teaching_accept_leave(request, pk):
    user_leave = NonTeachingLeave.objects.get(id=pk)
    user_leave.leave_Status = 'Approved'
    user_leave.save()
    messages.success(request, 'Leave has been granted successfully!')
    return redirect('admin_leave')


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def teaching_reject_leave(request, pk):
    user_leave = Leave.objects.get(id=pk)
    user_leave.leave_Status = 'Declined'
    user_leave.save()
    messages.success(request, 'Leave has been rejected successfully!')
    return redirect('admin_leave')


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def non_teaching_reject_leave(request, pk):
    user_leave = NonTeachingLeave.objects.get(id=pk)
    user_leave.leave_Status = 'Declined'
    user_leave.save()
    messages.success(request, 'Leave has been rejected successfully!')
    return redirect('admin_leave')


@login_required(login_url='login')
def update_user_profile(request):

    form = UserProfileChangeForm(instance=request.user)

    if request.method == "POST":
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return user_profile(request, pk=request.user.id)
        else:
            messages.error(request, 'Error occured during form processing.')

    return render(request, 'base/update_user_prof.html', {'form': form})


@login_required(login_url='login')
@allowed_user(roles=['student', 'lecturer', 'non_teaching'])
def update_org_profile(request):
    pk = request.user.id
    user = User.objects.get(id=pk)
    group = user.groups.all()[0].name
    if request.method == "POST":
        if group == 'lecturer':
            form = FacultyRegistriationForm(
                request.POST, instance=Lecturer.objects.get(user=user.id))
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Organization Profile updated successfully!')
                return user_profile(request, pk=request.user.id)
            else:
                messages.error(
                    request, 'Error occured during form processing.')

        elif group == 'student':
            form = StudentRegistriationForm(
                request.POST, instance=Student.objects.get(user=user.id))
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Organization Profile updated successfully!')
                return user_profile(request, pk=request.user.id)
            else:
                messages.error(
                    request, 'Error occured during form processing.')
        elif group == 'non_teaching':
            form = NonTeachingFacultyRegistriationForm(
                request.POST, instance=NonTeaching.objects.get(user=user.id))
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Organization Profile updated successfully!')
                return user_profile(request, pk=request.user.id)
            else:
                messages.error(
                    request, 'Error occured during form processing.')
    else:
        if group == 'lecturer':
            form = FacultyRegistriationForm(
                instance=Lecturer.objects.get(user=user.id))
        elif group == 'student':
            form = StudentRegistriationForm(
                instance=Student.objects.get(user=user.id))
        elif group == 'non_teaching':
            form = NonTeachingFacultyRegistriationForm(
                instance=NonTeaching.objects.get(user=user.id))

        return render(request, 'base/org_profile_update.html', {'form': form})


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def admin_leave(request):
    org = Orginization.objects.get(owner=request.user)
    faculty = Lecturer.objects.filter(orginization=org)
    Leave.objects.filter()
    teaching_list = []
    for i in faculty:
        teaching_list.append(Leave.objects.filter(e_id=i.id))
    non_teaching = NonTeaching.objects.filter(orginization=org)
    non_teaching_list = []
    for i in non_teaching:
        non_teaching_list.append(NonTeachingLeave.objects.filter(e_id=i.id))

    no_of_teaching_leaves = 0
    no_of_non_teaching_leaves = 0

    no_of_leaves_granted = 0
    no_of_leaves_pending = 0
    no_of_leaves_declined = 0

    teaching_pending_list = []
    teaching_approved_list = []
    teaching_declined_list = []

    for i in teaching_list:
        for j in i:
            if j.leave_Status == 'Pending':
                no_of_leaves_pending += 1
                teaching_pending_list.append(j)
            elif j.leave_Status == 'Approved':
                teaching_approved_list.append(j)
                no_of_leaves_granted += 1
            elif j.leave_Status == 'Declined':
                teaching_declined_list.append(j)
                no_of_leaves_declined += 1
            no_of_teaching_leaves += 1

    non_teaching_pending_list = []
    non_teaching_approved_list = []
    non_teaching_declined_list = []

    for i in non_teaching_list:
        for j in i:
            if j.leave_Status == 'Pending':
                non_teaching_pending_list.append(j)
                no_of_leaves_pending += 1
            elif j.leave_Status == 'Approved':
                non_teaching_approved_list.append(j)
                no_of_leaves_granted += 1
            elif j.leave_Status == 'Declined':
                non_teaching_declined_list.append(j)
                no_of_leaves_declined += 1

            no_of_non_teaching_leaves += 1
    total_leaves = no_of_teaching_leaves + no_of_non_teaching_leaves
    return render(request, 'base/admin_leave.html', {'teaching_pending_list': teaching_pending_list,
                                                     'non_teaching_pending_list': non_teaching_pending_list,
                                                     'no_of_teaching_leaves': no_of_teaching_leaves,
                                                     'no_of_non_teaching_leaves': no_of_non_teaching_leaves,
                                                     'total_leaves': total_leaves,
                                                     'no_of_leaves_granted': no_of_leaves_granted,
                                                     'no_of_leaves_pending': no_of_leaves_pending,
                                                     'no_of_leaves_declined': no_of_leaves_declined
                                                     })
