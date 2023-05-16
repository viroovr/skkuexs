from django.contrib import admin
from django.urls import path, include

from skkuexs.views import base_views
from common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skkuexs/', include('skkuexs.urls')),
    path('common/', include('common.urls')),
    path('common/', include('allauth.urls')),
    path('common/', include('dj_rest_auth.urls')),
    path('forums/', include('forums.urls')),
	path('', base_views.index, name='index'),  # '/' 에 해당되는 path

    # common으로 옮기면 오류    
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
