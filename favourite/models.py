from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.utils import timezone


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.post.title + " " + self.user.username + " tarafından " + timezone.now().strftime(
            "%Y-%m-%d %H:%M:%S") + " tarihinden favorilere alındı."
