from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    release_year = models.PositiveIntegerField()

    duration = models.CharField(max_length=200,null=True)

    rating = models.DecimalField(max_digits=5,decimal_places=2)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

