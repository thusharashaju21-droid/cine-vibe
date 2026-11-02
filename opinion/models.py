from django.db import models
from django.contrib.auth.models import User

from film.models import Movie
# Create your models here.
class Review(models.Model):

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    message = models.TextField()

    rating = models.DecimalField(max_digits=5,decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        unique_together = ("movie","owner")

    def __str__(self):
        return self.movie