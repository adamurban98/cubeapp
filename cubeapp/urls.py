from django.urls import path

from . import views

app_name = 'cubeapp'

urlpatterns = [
    path('', views.index, name='index'),
]
