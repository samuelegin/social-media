from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="receiver")
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.content



class Post(models.Model):
    post_owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    post_image = models.ImageField(upload_to="post_image",blank=True,null=True)
    caption = models.CharField(max_length=3000,blank=True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.post_owner.username



class Comment(models.Model):
    commentter = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    comment = models.CharField(max_length=500)
    date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_commented"]

    def __str__(self):
        return self.post.caption



class Reply(models.Model):
    replier = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="replies")
    reply = models.CharField(max_length=200)
    date_replied = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_replied"]
        verbose_name_plural = "Replies"

    def __str__(self):
        return self.comment.comment
