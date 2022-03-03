from django.shortcuts import render
from django.core.mail import send_mail
from .forms import MailInfo
from django.conf import settings
# Create your views here.

def home(request):
    form = MailInfo()
    return render(request,'send/home.html',{"form": form})

def success(request):
    form = MailInfo(request.POST)
    if form.is_valid():
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        recipient_list = form.cleaned_data["recipient_list"].split(',')
        send_mail( subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False )
    return render(request, "send/success.html")
