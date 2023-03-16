from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Details_SLot(models.Model):
    name = models.CharField(max_length=  100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    Purpose = models.TextField(max_length=500)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



