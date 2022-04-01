from django.urls import path
from .views import home, contact_us
urlpatterns = [
    path('', home, name='index'),
    path('contactus_post/', contact_us, name='contactus_post')
]
