# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)

class Goal(models.Model):
    created = models.DateField(auto_now=True)
    entry = models.TextField(blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
