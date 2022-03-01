from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    subject = 'Subject'
    message = 'Actual Message'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['example@mail.com',]
    send_mail( subject, message, email_from, recipient_list, fail_silently=False )

    return render(request,'send/index.html')    
