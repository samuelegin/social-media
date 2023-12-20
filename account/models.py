from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(
            primary_key=True,
            editable=False,
            default=uuid.uuid4)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to="user_pic")
    friends = models.ManyToManyField("self",symmetrical=False)
    bio = models.TextField()
    contact = models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
