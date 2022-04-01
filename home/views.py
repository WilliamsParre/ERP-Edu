from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from flask import redirect


def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        from_email = request.POST['email']
        message = 'Message : \n'+request.POST['message'] + \
            f'\n\n\nSender details :\nFirst Name : {first_name}\nLast Name : {last_name}\nEmail : {from_email}'
        subject = f'Hello admin, I am {first_name} {last_name}, I have a query.'
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email,
                          ['williamsparre2002@gmail.com'])
            except BadHeaderError:
                messages.warning(
                    request, 'Internal error! Try after some time.')
                return render(request, 'home/index.html')
            messages.success(
                request, f'Hi {first_name} {last_name}, we have successfully recived your message.')
            return render(request, 'home/index.html')
        else:
            messages.warning(
                request, 'Make sure all fields are entered and valid.')
            return render(request, 'home/index.html', {'err': 'Make sure all fields are entered and valid.'})

    return render(request, 'home/index.html')
