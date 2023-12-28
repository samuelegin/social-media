from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    post_owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_owner")
    caption = models.CharField(max_length=3000,blank=True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.post_owner.username



