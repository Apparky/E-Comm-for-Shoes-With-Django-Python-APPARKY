from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def user(request):
    return HttpResponse('This is USER Page')
