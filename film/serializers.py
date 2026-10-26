
from rest_framework import serializers

from django.contrib.auth.models import User

from film.models import Movie

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password"]

        read_only_fields = ["id"]

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie

        fields = "__all__"

        read_only_fields = ["id","owner","created_at","updated_at"]
