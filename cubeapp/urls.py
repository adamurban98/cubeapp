from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'cubeapp'

urlpatterns = [
    path('login', views.LoginSuccessView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.index, name='index'),
]
