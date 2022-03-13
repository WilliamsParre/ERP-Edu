from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_page, name="signup"),

    path('profile/<str:pk>/', views.user_profile, name='user-profile')
]
