from django.contrib import admin
from django.urls import path
from ticket import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('user/', views.user, name='user'),
    path('signup/',views.signup, name='signup'),
    path('teller/', views.teller, name='teller'),
    path('dashboard', views.dashboard, name='dashboard'),
]
