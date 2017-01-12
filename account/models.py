from django.contrib.auth.models import User
from django.db import models

class CraftyUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  picture = models.ImageField(null=True)

class Follow(models.Model):
   follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
   followee = models.ForeignKey(User, related_name='followee', on_delete=models.CASCADE)