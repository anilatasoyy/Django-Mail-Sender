# Django-Mail-Sender
Send Mail with Django


Ex: settings for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = your mail
EMAIL_HOST_PASSWORD = your password
EMAIL_USE_TLS = True


# IMPORTANT:
For this app to work you need to let your mail to send mail with 3rd party app
Ex: For gmail you either give access to less secure apps or you can create your own App password.
