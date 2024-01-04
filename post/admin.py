from django.contrib import admin
from .models import Post,Comment,Reply,Notification

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Notification)
