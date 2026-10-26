
from django.urls import path

from film.views import UserCreateView
from film.views import MovieListCreateView,MovieRetrieveUpdateDeleteView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # route to user create view
    path("register/",UserCreateView.as_view()),

    # route to token authentication
    path("token/",ObtainAuthToken.as_view()),

    # route to movie list,create 
    path("movie/",MovieListCreateView.as_view()),

    # route to movie retrieve,update,delete view
    path("movie/<int:pk>/",MovieRetrieveUpdateDeleteView.as_view()),
]