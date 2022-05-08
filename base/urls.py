from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_page, name="signup"),

    # For registration
    path('org/', views.org_registration, name="org_registration"),
    path('faculty/', views.faculty_registration, name="faculty_registration"),
    path('nonteaching/', views.non_teaching_registration,
         name="non_teaching_registration"),

    # For Updating profile
    path('update_user_prof/', views.update_user_profile, name='update_profile'),
    path('update_org_prof/', views.update_org_profile, name='update_org_profile'),

    path('courses/', views.courses, name='courses'),

    # Leave Apply
    path('leave/', views.leave, name='leave'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),

    # Leave Accept
    path('teaching_accept_leave/<str:pk>/',
         views.teaching_accept_leave, name="accept_leave"),
    path('non_teaching_accept_leave/<str:pk>/',
         views.non_teaching_accept_leave, name="non_teaching_accept_leave"),

    # Leave Reject
    path('teaching_reject_leave/<str:pk>/',
         views.teaching_reject_leave, name="reject_leave"),
    path('non_teaching_reject_leave/<str:pk>/',
         views.non_teaching_reject_leave, name="non_teaching_reject_leave"),

    # Admin Dashboard for Leave Management
    path('admin_leave/', views.admin_leave, name='admin_leave'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('attendance/', views.attendance, name='attendance'),

    # Manage for Organization
    path('manage/', views.manage, name='manage'),
    path('delete_faculty/<str:pk>/', views.delete_faculty, name='delete_faculty'),
    path('delete_non_teaching/<str:pk>/', views.delete_non_teaching,
         name='delete_non_teaching'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete_student'),

    # Course for Admin
    path('admin_courses/', views.admin_courses, name="admin_courses"),
    path('delete_course/<str:pk>/', views.delete_course, name="admin_courses"),

    path('fees/', views.fees, name='fees'),
    path('grades/', views.grades, name='grades'),
    path('qualification/', views.qualification, name='qualification'),
    path('profile/<str:pk>/', views.user_profile, name='profile'),
    path('settings/', views.settings, name='settings')
]
