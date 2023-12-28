from django.shortcuts import render
from .models import Post
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

@login_required
def home(request:HttpRequest):
    return render(request,"post/home.html")
