from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    # 로그인 되면 redirect할 곳
    # if request.user.is_authenticated:
    #     return redirect('forums/abc')
    # else:
        return render(request, "skkuexs/main.html")
