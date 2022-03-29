from django.shortcuts import render
def home(requests):
    return render(requests,'home/index.html')
# Create your views here.
