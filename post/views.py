from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Notification
from django.http import HttpRequest,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt


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


#this view brings all avialable user that can be followed
@login_required
def follow(request:HttpRequest):
    if request.method == "POST":
        search = request.POST.get("search")
        friends = User.objects.filter(username__icontains=search)

    else:
        friends = User.objects.exclude(username=request.user.username)
    context = {"follows":friends}
    return render(request,"post/follow.html",context)


@login_required
def profile(request:HttpRequest,user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request,"post/profile.html",{"user":user})


#follows a user once the follow button is clicked 
@csrf_exempt
def addfollow(request:HttpRequest):
    if request.method == "POST":
        u_id = request.POST.get("id")
        status = request.POST.get("status")

        following = get_object_or_404(User, id=u_id)
        current_user = request.user

        if status == "follow":
            current_user.follows.add(following)

            Notification.objects.create(
                user=current_user,
                receiver=following,
                content=f"{current_user} just followed you")

            current_user.save()
            return JsonResponse({"follow_num":following.followed_by.count()})

        elif status == "unfollow":
            current_user.follows.remove(following)

            Notification.objects.create(
                user=current_user,
                receiver=following,
                content=f"{current_user} just Unfollowed you")

            current_user.save()
            return JsonResponse({"follow_num":    following.followed_by.count()})


@login_required
def notification(request:HttpRequest):
    notifications = Notification.objects.filter(receiver=request.user)
    context = {"notifications":notifications}
    return render(request,"post/notification.html",context)

@csrf_exempt
def like(request:HttpRequest) -> JsonResponse:
    if request.method == "POST":
        p_id = request.POST.get("id")
        print(p_id)

        post = get_object_or_404(Post,id=int(p_id))

        if request.user not in post.like.all():
            post.like.add(request.user)
        else:
            post.like.remove(request.user)

        return JsonResponse({"like":post.like.count()})
