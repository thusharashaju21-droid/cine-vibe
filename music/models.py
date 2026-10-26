from django.db import models
from django.contrib.auth.models import User
from film.models import Movie
# Create your models here.

class Song(models.Model):

    track_number = models.PositiveIntegerField()

    title = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    duration = models.CharField(max_length=200)

    rating = models.DecimalField(max_digits=2,decimal_places=1)

    song_by = models.CharField(max_length=200)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):

        last_song_object = Song.objects.filter(movie=self.movie).last()

        if last_song_object:

            self.track_number = last_song_object.track_number+1

        else:

            self.track_number = 1
            
        return super().save(*args,**kwargs)
