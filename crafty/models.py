from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

class SkillLevel(models.Model):
  level = models.CharField(max_length=15)

  def __str__(self):
    return self.level

class Category(models.Model):
  category = models.CharField(max_length=50)

  def __str__(self):
    return self.category

class TimeUnits(models.Model):
  unit = models.CharField(max_length=15)

  def __str__(self):
    return self.unit

class Diy(models.Model):
  title = models.CharField(max_length=500)
  description = models.CharField(max_length=1000)
  skill_level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  duration = models.IntegerField()
  duration_units = models.ForeignKey(TimeUnits, on_delete=models.CASCADE)
  picture = models.ImageField(null=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('crafty:detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.title + " - " + self.creator.username

class Material(models.Model):
  name = models.CharField(max_length=100)
  amount = models.IntegerField()
  units = models.CharField(max_length=20, null=True)
  diy = models.ForeignKey(Diy, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.amount) + " " + self.units + " of " + self.name

class Instruction(models.Model):
  instruction = models.CharField(max_length=1000)
  picture = models.ImageField(null=True)
  diy = models.ForeignKey(Diy, on_delete=models.CASCADE)

  def __str__(self):
    return self.instruction

class Favorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  diy = models.ForeignKey(Diy, on_delete=models.CASCADE)

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  diy = models.ForeignKey(Diy, on_delete=models.CASCADE)
  comment = models.CharField(max_length=1000)
