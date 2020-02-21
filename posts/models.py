from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=300, blank=True)
    body = models.CharField(max_length=5000, blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    like = models.ManyToManyField(User, blank=True, related_name="like")
    unlike = models.ManyToManyField(User, blank=True, related_name="unlike")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'title: {self.title}, author: {self.author}'
