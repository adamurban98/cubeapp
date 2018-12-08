from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Abbreviation, IllegalLetter
from . import logout_success


def index(request):
    cards = []
    for a in Abbreviation.objects.all():
        card = {}
        card['abbreviation'] = a
        card['realobjects'] = a.realobject_set.all()[:3]
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

    def get_success_message(self, cleaned_data):
        return 'login success'


class AbbreviationDetail(DetailView):
    model = Abbreviation


class MeUserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'cubeapp/user_detail.html'
    login_url = '/login'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['illegalletters'] = self.request.user.illegalletter_set.all()
        return context
