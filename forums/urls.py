from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('<str:school_name>', views.main, name='main'),
    path('<str:school_name>/community', views.community, name='community'),
    path('<str:school_name>/courses', views.courses, name='courses'),
    path('<str:school_name>/submain_preparation', views.submain_preparation, name='submain'),
    path('<str:school_name>/courses', views.courses, name='submain'),
    path('<str:school_name>/submain_uni_life', views.submain_uni_life, name='submain_uni_life')
]