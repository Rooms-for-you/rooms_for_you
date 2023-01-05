from django.urls import path
from .views import RoomView
from . import views

urlpatterns = [
    path("rooms/", views.RoomView.as_view()),
    path("rooms/<int:pk>/", views.RoomDetailView.as_view())
]