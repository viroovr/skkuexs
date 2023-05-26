from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('select/', views.select, name='select'),

    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/login/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),

    path('google/login/', views.google_login, name='google_login'),
    path('google/login/callback/', views.google_callback,
         name='google_callback'),
    path('google/login/finish/', views.GoogleLogin.as_view(),
         name='google_login_todjango'),

    path('naver/login/', views.naver_login, name='naver_login'),
    path('naver/login/callback/', views.naver_callback, name='naver_callback'),
    path('naver/login/finish/', views.NaverLogin.as_view(),
         name='naver_login_todjango'),
]
