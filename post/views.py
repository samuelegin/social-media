from django.shortcuts import render,redirect
from .models import Post,Notification
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User= get_user_model()

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


def follow(request:HttpRequest):
    if request.method == "POST":
        search = request.POST.get("search")
        friends = User.objects.filter(username__icontains=search)

    else:
        friends = User.objects.exclude(username=request.user.username)
    context = {"follows":friends}
    return render(request,"post/follow.html",context)


def profile(request:HttpRequest,user_id):
    user = User.objects.get(id=user_id)
    return render(request,"post/profile.html",{"user":user})


def addfollow(request:HttpRequest,user_id):
    following = User.objects.get(id=user_id)
    current_user = request.user

    status = request.POST.get("follow")
    if status == "follow":
        current_user.follows.add(following)

        Notification.objects.create(
                user=current_user,
                receiver=following,
                content=f"{current_user} just followed you")

    elif status == "unfollow":
        current_user.follows.remove(following)

        Notification.objects.create(
                user=current_user,
                receiver=following,
                content=f"{current_user} just Unfollowed you")

    current_user.save()

    return redirect("post:follow")
