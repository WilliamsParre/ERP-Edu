from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from flask import redirect


def home(requests):
    return render(requests, 'home/index.html')


def contact_us(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        from_email = request.POST['email']
        message = 'Message :\n'+request.POST['message'] + \
            f'\n Sender details :\nFirst Name : {first_name}\nLast Name : {last_name}\n Email : {from_email}'
        subject = f'Hello admin, I am {first_name} {last_name}, I have a query.'
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email,
                          ['williamsparre2002@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Mail sent successfully')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    else:
        # raise Http404
        return HttpResponseRedirect('/')
