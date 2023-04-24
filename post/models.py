from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="post", blank=True, null=True)
    slug = models.SlugField(editable=False)
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="modified_by", null=True, blank=True)

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1

        while Post.objects.filter(slug=unique).exists():
            unique = "{}-{}".format(slug, number)
            number += 1

        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            self.slug = self.get_slug()
        else:
            orig = Post.objects.get(pk=self.pk)
            if orig.title != self.title:
                self.slug = self.get_slug()
        self.modified = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
