from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.all()
    c = {'courses': courses}
    return render(request, 'base/home.html', c)

