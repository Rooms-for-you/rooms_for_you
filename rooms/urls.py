from django.urls import path
from .views import RoomView
from . import views

urlpatterns = [
    path("rooms/", views.RoomView.as_view()),
    path("rooms/<str:pk>/", views.RoomDetailView.as_view())
]