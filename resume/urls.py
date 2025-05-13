from django.urls import path
from . import views


app_name = "resume"


urlpatterns = [
    path('create/', views.create_resume, name='create'),
    path('all/', views.all_resumes, name='all'),
    path('<int:id>/', views.get_by_id, name='get_by_id'),
    path('<str:username>/', views.get_by_username, name='get_by_username'),
]