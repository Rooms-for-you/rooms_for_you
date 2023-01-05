from django.urls import path
from . import views

urlpatterns = [
    path("hotels/", views.ListCreateHotelView.as_view()),
    path("hotels/<int:pk>/", views.RetrieveHotelView.as_view()),
]
