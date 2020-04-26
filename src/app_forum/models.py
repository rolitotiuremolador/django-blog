from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
  title = models.CharField(max_length=50, unique=True)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.title

class Topic(models.Model):
  subject       = models.CharField(max_length=255)
  last_updated  = models.DateTimeField(auto_now_add=True)
  forum         = models.ForeignKey(Forum, related_name='topics', on_delete=models.CASCADE)
  starter       = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)

class Post(models.Model):
  message       = models.TextField(max_length=5000)
  topic         = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
  created_at    = models.DateTimeField(auto_now_add=True)
  updated_at    = models.DateTimeField(null=True)
  created_by    = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
  updated_by    = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

