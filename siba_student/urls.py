from django.urls import path
from . import views
# from .forms import student_form

# urls in the students app

urlpatterns = [
    path('', views.home, name='home'),
    path('siba_student', views.application, name='application'),
]