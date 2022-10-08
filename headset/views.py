from http.client import HTTPResponse
from django.shortcuts import render


def index(requset):
    return render(requset, "index.html")
