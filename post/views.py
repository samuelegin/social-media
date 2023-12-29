from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

@login_required
def home(request:HttpRequest):
    posts = Post.objects.all()
    context = {"posts":posts}

    return render(request,"post/home.html",context)

@login_required
def post(request:HttpRequest):
    if request.method == "POST":
        caption = request.POST.get("caption")
        post_image = request.FILES.get("post_image")
        print(post_image)
        Post.objects.create(
                post_owner = request.user,
                caption = caption,
                post_image = post_image,
                )
        return redirect("post:home")
    return render(request,"post/post.html")
