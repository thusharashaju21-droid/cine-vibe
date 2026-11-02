
from rest_framework import serializers

from opinion.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    movie = serializers.StringRelatedField()

    owner = serializers.StringRelatedField()

    class Meta:

        model = Review

        fields = "__all__"

        read_only_fields = ["id","movie","owner","created_at","updated_at"]