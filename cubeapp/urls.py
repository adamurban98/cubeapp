from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'cubeapp'

urlpatterns = [
    path('login', views.LoginSuccessView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('me', views.MeUserDetailView.as_view(), name='me-detail'),
    path('pair/<int:pk>', views.AbbreviationDetail.as_view(), name='pair-detail'),
    path('', views.index, name='index'),
]
