from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_page, name="signup"),
    path('org/', views.org_registration, name="org_registration"),
    path('faculty/', views.faculty_registration, name="faculty_registration"),
    path('nonteaching/', views.non_teaching_registration, name="non_teaching_registration"),
    path('update_user_prof/', views.update_user_profile, name='update_profile' ),
    path('update_org_prof/', views.update_org_profile, name='update_org_profile' ),
    path('courses/', views.courses, name='courses'),
    path('accept/', views.accept, name="accept"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('attendance/', views.attendance, name='attendance'),
    path('leave/', views.leave, name='leave'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('fees/', views.fees, name='fees'),
    path('grades/', views.grades, name='grades'),
    path('qualification/', views.qualification, name='qualification'),
    path('profile/<str:pk>/', views.user_profile, name='profile'),
    path('settings/', views.settings, name='settings')
]
