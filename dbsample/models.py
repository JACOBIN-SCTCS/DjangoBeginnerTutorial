# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.sid)
    
    
