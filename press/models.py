from django.db import models
from mdeditor.fields import MDTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = MDTextField(null=True, blank=True)
    thumbnail = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
