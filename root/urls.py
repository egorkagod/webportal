from django.urls import path
from . import views


app_name = "root"

urlpatterns = [
    path('', views.index, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
