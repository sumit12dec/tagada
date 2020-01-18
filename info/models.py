from django.db import models
from rest_framework import serializers

class Txn(models.Model):
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

