from django.shortcuts import render
from django.http import HttpResponse


def index_authentication(request):
    return HttpResponse("Hello this is a nice page")