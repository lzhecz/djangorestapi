from django.urls import path
from .views import *


urlpatterns = [
    path('drivers/driver/', DriverListView.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetailView.as_view()),
    path('vehicles/vehicle/', VehicleListView.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetailView.as_view()),
    path('vehicles/set_driver/<int:pk>/', SetDriverView.as_view()),
]
