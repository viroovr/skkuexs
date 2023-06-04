import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

from django.conf import settings
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.naver import views as naver_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
import requests
from rest_framework import status
from json.decoder import JSONDecodeError

from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView
from .forms import SchoolForm
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

state = getattr(settings, 'STATE')
BASE_URL = getattr(settings, 'BASE_URL')

KAKAO_CALLBACK_URI = BASE_URL + 'common/kakao/login/callback/'
NAVER_CALLBACK_URI = BASE_URL + 'common/naver/login/callback/'
GOOGLE_CALLBACK_URI = BASE_URL + 'common/google/login/callback/'


def select(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        user = request.user
        if form.is_valid():
            school_name = form.cleaned_data['school_name']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            instance = Profile.objects.create(
                user=user, school_name=school_name)
            instance.save()
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            # profile = user.profile
            # profile.school_name = school_name
            # profile.save()
            return redirect('/forums/' + school_name)
    else:
        form = SchoolForm()

    return render(request, 'common/school_select.html', {'form': form})


def profile_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            if (request.user.is_anonymous or request.user.profile):
                return render(request, 'forums/profile_required.html')
                # profile = request.user.profile
            else:
                return view_func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return render(request, 'forums/profile_required.html')

    return wrapper


def preview(request):
    return render(request, 'common/school_select_notuser.html')


class CustomLoginView(LoginView):
    def get_success_url(self):
        # 로그인 후 리다이렉트할 URL 생성
        profile = self.request.user.profile  # 사용자의 학교 이름을 가져옴 (가정)
        school_name = profile.school_name
        url = f"/forums/{school_name}"
        return url


def social_login(request, email, access_token, code, domain):

    try:
        # 전달받은 이메일로 등록된 유저가 있는지 탐색
        user = User.objects.get(email=email)
        profile = user.profile
        # FK로 연결되어 있는 socialaccount 테이블에서 해당 이메일의 유저가 있는지 확인
        social_user = SocialAccount.objects.get(user=user)

        # 있는데 구글계정이 아니어도 에러
        if social_user.provider != domain:
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

        # 이미 Google로 제대로 가입된 유저 => 로그인 & 해당 우저의 jwt 발급
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}common/{domain}/login/finish/", data=data)
        accept_status = accept.status_code

        # 뭔가 중간에 문제가 생기면 에러
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)

        # accept_json = accept.json()
        # accept_json.pop('user', None)

        user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
        login(request, user, backend=user.backend)  # 로그인

        return redirect(f'/forums/{user.profile.school_name}')
    except (User.DoesNotExist, Profile.DoesNotExist):

        # 전달받은 이메일로 기존에 가입된 유저가 아예 없으면 => 새로 회원가입 & 해당 유저의 jwt 발급
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}common/{domain}/login/finish/", data=data)
        accept_status = accept.status_code

        # 뭔가 중간에 문제가 생기면 에러
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)

        # accept_json = accept.json()
        # accept_json.pop('user', None)

        user = User.objects.get(email=email)
        user.backend = 'allauth.account.auth_backends.AuthenticationBackend'

        login(request, user, backend=user.backend)  # 로그인
        return redirect('/common/select/')  # 로그인후 이동할 페이지 변경
    except Exception:
        return redirect('/common/select/')
    except SocialAccount.DoesNotExist:
        # User는 있는데 SocialAccount가 없을 때 (=일반회원으로 가입된 이메일일때)
        return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            school_name = form.cleaned_data.get('school_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect(f'/forums/{school_name}')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

    # return render(request, 'common/school_select.html')


def kakao_login(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )


def kakao_callback(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    code = request.GET["code"]

    redirect_uri = KAKAO_CALLBACK_URI
    """
    Access Token Request
    """
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
    """
    Email Request
    """
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()
    kakao_account = profile_json.get('kakao_account')
    """
    kakao_account에서 이메일 외에
    카카오톡 프로필 이미지, 배경 이미지 url 가져올 수 있음
    print(kakao_account) 참고
    """
    # print(kakao_account)
    email = kakao_account.get('email')
    """
    Signup or Signin Request
    """
    return social_login(request, email, access_token, code, domain="kakao")


def google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, 'SOCIAL_AUTH_GOOGLE_CLIENT_ID')
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")


def google_callback(request):
    client_id = getattr(settings, 'SOCIAL_AUTH_GOOGLE_CLIENT_ID')
    client_secret = getattr(settings, 'SOCIAL_AUTH_GOOGLE_SECRET')
    code = request.GET.get('code')
    # pprint(f"code : {code}")

    # 1. 받은 코드로 구글에 access token 요청
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")

    # 1-1. json으로 변환 & 에러 부분 파싱
    token_req_json = token_req.json()
    # pprint(f"token_req_json  : {token_req_json }")
    error = token_req_json.get("error")

    # 1-2. 에러 발생 시 종료
    if error is not None:
        raise JSONDecodeError(error)

    # 1-3. 성공 시 access_token 가져오기
    access_token = token_req_json.get('access_token')

    #################################################################

    # 2. 가져온 access_token으로 이메일값을 구글에 요청
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code

    # 2-1. 에러 발생 시 400 에러 반환
    if email_req_status != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

    # 2-2. 성공 시 이메일 가져오기
    email_req_json = email_req.json()
    # pprint(f"email_req_json : {email_req_json}")
    email = email_req_json.get('email')

    # return JsonResponse({'access': access_token, 'email':email})

    #################################################################

    # 3. 전달받은 이메일, access_token, code를 바탕으로 회원가입/로그인
    return social_login(request, email, access_token, code, domain="google")


def naver_login(request):
    client_id = getattr(settings, 'SOCIAL_AUTH_NAVER_CLIENT_ID')
    # print("ho")
    return redirect(f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&state=STATE_STRING&redirect_uri={NAVER_CALLBACK_URI}")


def naver_callback(request):
    client_id = getattr(settings, 'SOCIAL_AUTH_NAVER_CLIENT_ID')
    client_secret = getattr(settings, 'SOCIAL_AUTH_NAVER_SECRET')
    code = request.GET.get("code")
    state_string = request.GET.get("state")

    # code로 access token 요청
    token_request = requests.get(
        f"https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={code}&state={state_string}")
    token_response_json = token_request.json()

    error = token_response_json.get("error", None)
    if error is not None:
        raise JSONDecodeError(error)

    access_token = token_response_json.get("access_token")

    # return JsonResponse({"access_token":access_token})

    # access token으로 네이버 프로필 요청
    profile_request = requests.post(
        "https://openapi.naver.com/v1/nid/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()

    email = profile_json.get("response").get("email")

    if email is None:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

    # 받아온 네이버 계정으로 회원가입/로그인 시도
    """
    Signup or Signin Request
    """
    return social_login(request, email, access_token, code, domain="naver")


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI


class NaverLogin(SocialLoginView):
    adapter_class = naver_view.NaverOAuth2Adapter
    callback_url = NAVER_CALLBACK_URI
    client_class = OAuth2Client


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


class UserPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'password_reset_done_fail.html')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'  # 템플릿을 변경하려면 이와같은 형식으로 입력


UserModel = get_user_model()
INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context


def page_not_found(request, exception):
    return render(request, 'common/404.html', {})


@csrf_exempt
def form_post(request):
    # 구글 폼에서 스크립트로 /common/form 으로 post를 보냄
    body = json.loads(request.body.decode('utf-8'))
    id = body["form_id"]
    context = {
        'school_name': id
    }
    return JsonResponse(context)
