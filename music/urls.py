from django.urls import path

from music.views import SongCreateView,SongRetrieveUpdateDeleteView

urlpatterns = [

    # route to song creation view
    path("movie/<int:pk>/song/",SongCreateView.as_view()),

    # route to song retreive,update,delete view
    path("song/<int:pk>/",SongRetrieveUpdateDeleteView.as_view()),
]