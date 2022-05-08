import re
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from numpy import save, tile
from .decorators import allowed_user
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import CourseForm, StudentRegistriationForm, signUpForm, OrganizationRegistrationForm, FacultyRegistriationForm, NonTeachingFacultyRegistriationForm, UserProfileChangeForm
from leave.forms import Leave, NonTeachingLeave, LeaveForm, NonTeachingLeaveForm
from base.models import Course, Faculty, NonTeaching, Organization, Student
from django.contrib.auth import update_session_auth_hash
import pandas as pd
from plotly.offline import plot
import plotly.express as px


@login_required(login_url='login')
def home(request):
    pk = request.user.id
    user = User.objects.get(id=pk)
    group = user.groups.all()[0].name

    if group == 'admin':
        return redirect('admin_dashboard')

    return redirect('dashboard')


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
        form2 = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Registered successful! Account created successfully!')
            org = OrganizationRegistrationForm()
            faculty = FacultyRegistriationForm()
            non_teaching = NonTeachingFacultyRegistriationForm()
            return render(request, 'base/registration.html', {'org': org, 'faculty': faculty, 'non_teaching': non_teaching})
        else:
            messages.error(request, 'An error occured during regestration')

    return render(request, 'base/login_register.html', {'form': form})


def org_registration(request):

    if request.method == 'POST':
        form = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.user.username)
            user.username = user.username.lower()
            user.is_active = True
            admin = Group.objects.get(name='admin')
            user.save()
            user.groups.add(admin)
            user.save()
            logout(request)
            messages.success(
                request, 'Registered successful! Organization added successfully.')
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
            faculty = Group.objects.get(name='faculty')
            user.save()
            user.groups.add(faculty)
            user.save()
            logout(request)
            messages.success(
                request, 'Registered successful! Message is sent to you organisation for account activation.')
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
                request, 'Registered successful! Message is sent to you organisation for account activation.')
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
    elif group == 'faculty':
        if Faculty.objects.all().count() > 0:
            profile = Faculty.objects.get(user=user.id)
    elif group == 'student':
        # profile = User.objects.filter(student__first_name=user.first_name)
        if Student.objects.all().count() > 0:
            profile = Student.objects.get(user=user.id)
    elif group == 'non_teaching':
        profile = NonTeaching.objects.get(user=user.id)
    context = {'user': user, 'profile': profile}
    return render(request, 'base/profile.html', context)


def dashboard(request):
    return render(request, 'base/dashboard.html')


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def admin_dashboard(request):

    org = Organization.objects.get(owner=request.user)
    faculty_strength = Faculty.objects.filter(organization=org).count()
    students_strength = Student.objects.filter(organization=org).count()
    non_teaching_strength = NonTeaching.objects.filter(
        organization=org).count()

    # Bar Graph for Strength of Organization
    org_data = {
        'users': ['Faculty', 'Non-Teaching', 'Students'],
        'strength': [faculty_strength, non_teaching_strength, students_strength],
    }

    df = pd.DataFrame(org_data, index=None)

    fig = px.bar(df, x='users', y='strength',
                 title="Organization strength")

    bar_graph = plot(fig, output_type="div")

    # Pie Chart for Organization

    fig = px.pie(df, values='strength', names='users',
                 hole=.5, title='Organization')

    org_pie_chart = plot(fig, output_type="div")

    # Pie Chart for Teaching Staff
    male = Faculty.objects.filter(organization=org, gender='Male').count()
    female = Faculty.objects.filter(organization=org, gender='Female').count()
    others = Faculty.objects.filter(organization=org, gender='Others').count()

    pie_chart_data = {
        'names': ['Male', 'Female', 'Others'],
        'no_of_users': [male, female, others]
    }

    pie_df = pd.DataFrame(pie_chart_data)

    fig = px.pie(pie_df, values='no_of_users',
                 names='names', title='Teaching Staff')

    teaching_pie_chart = plot(fig, output_type="div")

    # Pie Chart for Non-Teaching
    male = NonTeaching.objects.filter(organization=org, gender='Male').count()
    female = NonTeaching.objects.filter(
        organization=org, gender='Female').count()
    others = NonTeaching.objects.filter(
        organization=org, gender='Others').count()

    pie_chart_data = {
        'names': ['Male', 'Female', 'Others'],
        'no_of_users': [male, female, others]
    }

    pie_df = pd.DataFrame(pie_chart_data)

    fig = px.pie(pie_df, values='no_of_users',
                 names='names', title='Non-Teaching Staff')

    non_teaching_pie_chart = plot(fig, output_type="div")

    # Pie Chart for Students
    male = Student.objects.filter(organization=org, gender='Male').count()
    female = Student.objects.filter(
        organization=org, gender='Female').count()
    others = Student.objects.filter(
        organization=org, gender='Others').count()

    pie_chart_data = {
        'names': ['Male', 'Female', 'Others'],
        'no_of_users': [male, female, others]
    }

    pie_df = pd.DataFrame(pie_chart_data)

    fig = px.pie(pie_df, values='no_of_users',
                 names='names', title='Students')

    student_pie_chart = plot(fig, output_type="div")

    return render(request, 'base/admin/admin_dashboard.html', {'bar_graph': bar_graph,
                                                               'org_pie_chart': org_pie_chart,
                                                               'teaching_pie_chart': teaching_pie_chart,
                                                               'non_teaching_pie_chart': non_teaching_pie_chart,
                                                               'student_pie_chart': student_pie_chart
                                                               })


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def admin_courses(request):

    courses = Course.objects.filter(organization=request.user.organization)

    return render(request, 'base/admin/admin_courses.html', {'courses': courses})


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def add_course(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.organization = request.user.organization
            form.save()
            form = CourseForm()
            messages.success(request, 'Course added successfully!')
        else:
            messages.error(request, 'Error occured during form processing.')

    return render(request, 'base/admin/add_course.html', {'form': form})


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def edit_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        form.save()
        messages.success(request, 'Course updated successfully!')
        return redirect('admin_courses')
    else:
        messages.error(request, 'Error occured during form processing.')
    return render(request, 'base/admin/edit_course.html', {'form': form, 'id': pk})


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def delete_course(request, pk):
    Course.objects.get(id=pk).delete()
    messages.success(request, 'Course deleted successfully')
    return redirect('admin_courses')


@login_required(login_url='login')
def courses(request):
    return render(request, 'base/courses.html')


@login_required(login_url='login')
def attendance(request):
    return render(request, 'base/attendance.html')


@login_required(login_url='login')
@allowed_user(roles=['faculty', 'non_teaching'])
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
        user = Faculty.objects.get(user=request.user.id)
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
@allowed_user(roles=['faculty', 'non_teaching'])
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
                request, 'Leave has been applied successfully! Message is sent to you organisation for leave approval.')
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
@allowed_user(roles=['student', 'faculty', 'non_teaching'])
def update_org_profile(request):
    pk = request.user.id
    user = User.objects.get(id=pk)
    group = user.groups.all()[0].name
    if request.method == "POST":
        if group == 'faculty':
            form = FacultyRegistriationForm(
                request.POST, instance=Faculty.objects.get(user=user.id))
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
        if group == 'faculty':
            form = FacultyRegistriationForm(
                instance=Faculty.objects.get(user=user.id))
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
    org = Organization.objects.get(owner=request.user)
    faculty = Faculty.objects.filter(organization=org)
    Leave.objects.filter()
    teaching_list = []
    for i in faculty:
        teaching_list.append(Leave.objects.filter(e_id=i.id))
    non_teaching = NonTeaching.objects.filter(organization=org)
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
    return render(request, 'base/admin/admin_leave.html', {'teaching_pending_list': teaching_pending_list,
                                                           'non_teaching_pending_list': non_teaching_pending_list,
                                                           'no_of_teaching_leaves': no_of_teaching_leaves,
                                                           'no_of_non_teaching_leaves': no_of_non_teaching_leaves,
                                                           'total_leaves': total_leaves,
                                                           'no_of_leaves_granted': no_of_leaves_granted,
                                                           'no_of_leaves_pending': no_of_leaves_pending,
                                                           'no_of_leaves_declined': no_of_leaves_declined
                                                           })


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def manage(request):
    org = Organization.objects.get(owner=request.user)
    faculty_list = Faculty.objects.filter(organization=org)
    students = Student.objects.filter(organization=org)
    non_teaching_list = NonTeaching.objects.filter(organization=org)
    faculty_strength = len(faculty_list)
    students_strength = len(students)
    non_teaching_strength = len(non_teaching_list)
    return render(request, 'base/manage.html', {'faculty_list': faculty_list,
                                                'non_teaching_list': non_teaching_list,
                                                'students': students,
                                                'faculty_strength': faculty_strength,
                                                'students_strength': students_strength,
                                                'non_teaching_strength': non_teaching_strength
                                                })


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def delete_faculty(request, pk):
    Faculty.objects.get(e_id=pk).delete()
    messages.success(request, 'Faculty deleted successfully!')
    return redirect('manage')


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def delete_non_teaching(request, pk):
    NonTeaching.objects.get(nt_e_id=pk).delete()
    messages.success(request, 'Non-Teaching staff deleted successfully!')
    return redirect('manage')


@login_required(login_url='login')
@allowed_user(roles=['admin'])
def delete_student(request, pk):
    Student.objects.get(u_id=pk).delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('manage')
