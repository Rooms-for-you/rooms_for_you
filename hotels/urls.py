from django.urls import path
from . import views
from rooms.views import RoomView

urlpatterns = [
    path("hotels/", views.ListCreateHotelView.as_view()),
    path("hotels/<int:pk>/", views.RetrieveHotelView.as_view()),
    path("hotels/<int:pk>/rooms/", RoomView.as_view()),

]
