from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
  title = models.TextField()
  slug = models.SlugField(unique=True)
  content = models.TextField(null=True, blank=True)
  user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return f"/blog/{self.slug}"

  def get_edit_url(self):
    return f"/blog/{self.slug}/update"

  def get_delete_url(self):
    return f"/blog/{self.slug}/delete"