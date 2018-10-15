from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .models import Abbreviation
from . import logout_success


def index(request):
    cards = []
    for a in Abbreviation.objects.all():
        card = {}
        card['abbreviation'] = a
        card['realobjects'] = a.realobject_set.all()
        cards.append(card)
    context = {'request': request, 'cards': cards}
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