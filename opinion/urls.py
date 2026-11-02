
from django.urls import path

from opinion.views import ReviewListView,ReviewCreateView
from opinion.views import ReviewRetrieveView,ReviewUpdateDeleteView

urlpatterns = [

    # listing review
    path("review/all/",ReviewListView.as_view()),

    # creating review
    path("movie/<int:pk>/review/",ReviewCreateView.as_view()),

    # review retrieve view
    path("review/<int:pk>/",ReviewRetrieveView.as_view()),

    # review update,delete view
    path("review/<int:pk>/",ReviewUpdateDeleteView.as_view()),
]