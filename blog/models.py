from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    # tags = list field

    def __str__(self):
        return f"{self.title} by {self.author}"
