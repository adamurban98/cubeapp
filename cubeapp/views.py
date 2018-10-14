from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from . import logout_success


def index(request):
    context = {"request": request}
    return render(request, 'cubeapp/index.html', context)


@login_required()
def user(request):
    pass


def add(request):
    pass


class LoginSuccessView(SuccessMessageMixin, LoginView):
    success_message = 'Succesfully logged in!'
    succes_url = '/admin'

    def get_succes_message(self, cleaned_data):
        return 'login succes'