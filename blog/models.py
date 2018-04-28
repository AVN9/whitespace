# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True)
    dob = models.DateField('Date of Birth')
    contact_no = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    sex = models.CharField(max_length=5)
    company = models.CharField(max_length=50)
    websites = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True,null=True)
    date_published = models.DateField('Date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title