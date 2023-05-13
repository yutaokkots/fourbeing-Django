from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from useraccounts.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    profile = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created=models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    def __str__ (self):
        return f"New post: called '{self.title}'"
    
class Reply(models.Model):
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=2000)
    love = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='replies', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    created = models.DateTimeField(auto_now_add=True)

    def add_love(self):
        self.love += 1
        self.save()

class Photo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    url = models.CharField(max_length=200)
    userPhoto = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for user: {self.user_id} @{self.url}"


# This test class was created to experiment with initial api calls
class Test(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  def __str__(self):
    return f"This test returned: ${self.name}"
  



