from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('<str:school_name>', views.main, name='main'),
    path('<str:school_name>/community', views.community, name='community')
]