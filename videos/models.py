# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=128)
    path = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'path': self.path,
            'created_at': self.created_at,
        }

    class Meta:
        db_table = 'videos'
