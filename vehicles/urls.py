from django.urls import path
from .views import VehicleListView

urlpatterns = [
    path('', VehicleListView.as_view(), name='all_vehicles')
]
