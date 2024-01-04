from django.urls import path
from . import views


app_name = "post"
urlpatterns = [
        path("",views.home,name="home"),
        path("post/",views.post,name="post"),
        path("follows/",views.follow,name="follow"),
        path("profile/<uuid:user_id>/",views.profile,name="user_profile"),
        path("follows/addfollow/",views.addfollow,name="addfollow"),
        path("notification/",views.notification,name="notification"),
        path("like/",views.like,name="like"),
        ]
