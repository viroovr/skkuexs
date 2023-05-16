from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='kakao'),
    # path('rest-auth/naver/', views.NaverLogin.as_view(), name='naver'),
    # path('rest-auth/google/', views.GoogleLogin.as_view(), name='google'),
    # path('rest-auth/github/', views.GithubLogin.as_view(), name='github'),
    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/login/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
]
