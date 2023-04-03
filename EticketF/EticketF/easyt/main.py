from django.contrib import admin
from django.urls import path
from ticket import views

urlpatterns = [
    path('', views.login, name='login'),
    path('user/', views.user, name='user'),
    path('teller/', views.teller, name='teller'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('forget/', views.forget, name='forget'),
    path('forget2/', views.forget2, name='forget2'),
    path('ticket/', views.ticket, name='ticket'),
    path('my_ticket/', views.my_ticket, name='my_ticket'),
]
