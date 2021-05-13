from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Drone(models.Model):
    user = models.ForeignKey(User,ondelete=models.CASCADE,related_name="drone")
    roll = models.IntegerField(default=0)
    pitch = models.IntegerField(default=0)
    yaw = models.IntegerField(default=0)
    throttle = models.IntegerField(default=0)
    active = models.BooleanField(default=False)


    