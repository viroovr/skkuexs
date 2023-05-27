from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('<str:school_name>', views.main, name='main'),
    path('<str:school_name>/community', views.community, name='community'),
    path('<str:school_name>/courses', views.courses, name='courses'),
    path('<str:school_name>/submain_preparation', views.submain_preparation, name='submain'),
    # path('<str:school_name>/courses', views.courses, name='submain'),
    path('<str:school_name>/submain_uni_life', views.submain_uni_life, name='submain_uni_life'),
    path('<str:school_name>/visa', views.visa, name='visa'),
    path('<str:school_name>/dorm', views.dorm, name='dorm'),
    path('<str:school_name>/etc_pre', views.etc_pre, name='etc_pre'),
    path('<str:school_name>/fill_out', views.fill_out, name='fill_out'),
    path('<str:school_name>/uni_review', views.uni_review, name='uni_review'),
    
]