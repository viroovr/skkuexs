from django.urls import path

from .views import base_views

app_name = 'skkuexs'

urlpatterns = [
    # base
    path('', base_views.index, name='index')
]
