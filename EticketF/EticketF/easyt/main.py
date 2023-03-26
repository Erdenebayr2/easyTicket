from django.contrib import admin
from django.urls import path
from ticket import views

urlpatterns = [
    path('', views.login, name='login'),
    path('{user/}', views.user, name='user'),
    path('{teller/}', views.teller, name='teller'),
    path('{dashboard/}', views.dashboard, name='dashboard'),
    path('{contact/}', views.contact, name='contact'),
]
