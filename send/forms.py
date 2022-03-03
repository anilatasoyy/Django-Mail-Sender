from django import forms

class MailInfo(forms.Form):
    
    subject = forms.CharField(max_length=100,label="subject")
    message = forms.CharField(max_length=500,label="message")
    recipient_list = forms.CharField(label="recipients",help_text="Plase divide recipients with comma. Ex: example1@gmail.com,example2@gmail.com ")