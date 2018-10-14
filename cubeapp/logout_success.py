from django.contrib.auth.signals import user_logged_out, user_login_failed
from django.contrib import messages


def show_message(sender, user, request, **kwargs):
    messages.success(request, 'You have been successfully logged out.')


def show_message2(sender, user, request, **kwargs):
    messages.success(request, 'Login failed')


user_logged_out.connect(show_message)
user_login_failed.connect(show_message2)
