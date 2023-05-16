from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "skkuexs/main.html")
