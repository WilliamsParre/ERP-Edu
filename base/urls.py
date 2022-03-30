from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_page, name="signup"),
    path('courses/', views.courses, name='courses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('attendance/', views.attendance, name='attendance'),
    path('fees/', views.fees, name='fees'),
    path('grades/', views.grades, name='grades'),
    path('qualification/', views.qualification, name='qualification'),
    path('profile/', views.user_profile, name='profile'),
    path('settings/', views.settings, name='settings')
]
