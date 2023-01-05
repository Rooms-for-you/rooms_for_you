from django.urls import path
from . import views

urlpatterns = [
    path("hotel/", views.ListCreateHotelView.as_view()),
    path("hotel/<int:pk>/", views.RetrieveHotelView.as_view()),
]
