from django.contrib.auth.signals import user_logged_out, user_login_failed
from django.contrib import messages


def show_message_logout_success(sender, user, request, **kwargs):
    messages.success(request, 'You have been successfully logged out.')


def show_message_login_fail(sender, credentials, request, **kwargs):
    messages.success(request, 'Login failed. Incorrect username or password.')


user_logged_out.connect(show_message_logout_success)
user_login_failed.connect(show_message_login_fail)
