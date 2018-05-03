from django.urls import path, re_path
from AppTwo import views

urlpatterns = [
    # re_path(r'^apptwo', views.index, name='index'),
    re_path(r'help/', views.help, name='help'),
    re_path(r'users/', views.users, name='users'),
    re_path(r'signup/', views.signup, name='signup'),
]