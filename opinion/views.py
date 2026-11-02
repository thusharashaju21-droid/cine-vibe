from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from opinion.serializers import ReviewSerializer
from opinion.models import Review
from film.models import Movie
from opinion.permissions import IsOwner

# Create your views here.

class ReviewListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_id = pk
        movie_object = Movie.objects.get(id=movie_id)

        form_data = request.data

        serializer_instance = ReviewSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_object,owner=request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class ReviewRetrieveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    