# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class device(models.Model):
    device_uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user_id = models.ForeignKey(User)

class devicelog(models.Model):
    device = models.ForeignKey(device)
    timestamp = models.DateTimeField(auto_now=True)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    moisture = models.FloatField(default=0)
    waterpump = models.SmallIntegerField(default=0)
    fan = models.SmallIntegerField(default=0)
    heater = models.SmallIntegerField(default=0)
