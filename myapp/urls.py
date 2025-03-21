from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('program', views.program, name='program'),
    path('register', views.register, name='register'),
    path('indexx', views.indexx, name='indexx'),
    # path('reset', views.reset, name='reset'),
    path('user-dash', views.dash, name='dash'),
    path('logout', views.logout, name='logout'),
]