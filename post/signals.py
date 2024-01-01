from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Comment,Reply,Notification

@receiver(post_save,sender=Comment)
def commentsignal(sender,instance,created,**kwargs):
    if created:
        sender = instance.commentter
        content = f"{instance.commentter.username} commentted     on your post"
        receiver = instance.post.post_owner

        Notification.objects.create(
                user=sender,
                content=content,
                receiver=receiver,)


@receiver(post_save,sender=Reply)
def replysignal(sender,instance,created,**kwargs):
    if created:
        sender=instance.replier
        content = f"{self.replier.username} replied to your comment"
        receiver=instance.comment.commentter

        Notification.objects.create(
                user=sender,
                content=content,
                receiver=receiver,)
