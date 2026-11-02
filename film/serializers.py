
from rest_framework import serializers

from django.contrib.auth.models import User

from film.models import Movie
from music.models import Song
from opinion.models import Review
from music.serializers import SongSerializer
from opinion.serializers import ReviewSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password"]

        read_only_fields = ["id"]

class MovieSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    song_count = serializers.SerializerMethodField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Movie

        fields = "__all__"

        read_only_fields = ["id","owner","created_at","updated_at"]

    def get_song_count(self,obj):

        return Song.objects.filter(movie=obj).count()

    def get_songs(self,obj):

        song_object = Song.objects.filter(movie=obj)

        serializer_instance = SongSerializer(song_object,many=True)

        return serializer_instance.data

    def get_reviews(self,obj):

        review_object = Review.objects.filter(movie=obj)

        serializer_instance = ReviewSerializer(review_object,many=True)

        return serializer_instance.data