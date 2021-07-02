from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("LightGram에 오신 것을 환영합니다.")
