from django.urls import path
from sensor_gateway.api import views

urlpatterns = [
    path('list/',views.SensorData.as_view()),
]