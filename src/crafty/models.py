from django.core.urlresolvers import reverse
from django.db import models

class Diy(models.Model):
  artist = models.CharField(max_length=250)
  title = models.CharField(max_length=500)
  genre = models.CharField(max_length=100)
  logo = models.FileField()

  def get_absolute_url(self):
    return reverse('crafty:detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.title + " - " + self.artist

class Song(models.Model):
  # if diy is deleted, songs should be deleted
  diy = models.ForeignKey(Diy, on_delete=models.CASCADE)
  file_type = models.CharField(max_length=10)
  title = models.CharField(max_length=250)
  is_favorite = models.BooleanField(default=False)

  def __str__(self):
    return self.title
