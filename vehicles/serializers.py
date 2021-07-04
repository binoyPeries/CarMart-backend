from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ['customer']

# fields = ['id', 'vehicle_type', 'vehicle_make', 'vehicle_model', 'price', 'condition', 'year', 'mileage',
#                   'fuel_type', 'engine_capacity', 'transmission', 'description', 'front', 'back', 'interior', ]
