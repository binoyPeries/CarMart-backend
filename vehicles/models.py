from django.db import models
from customers.models import Customer


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICE = [
        ('car', 'Car'),
        ('van', 'Van'),
        ('suv', 'Suv/Jeep'),
        ('bike', 'Motorbike'),
        ('bus', 'Bus'),
        ('tuk', 'Three Wheeler'),
        ('heavy', 'Heavy Vehicle'),
    ]
    VEHICLE_CONDITION_CHOICE = [
        ('new', 'Brand New'),
        ('used', 'Used'),

    ]
    VEHICLE_FUEL_CHOICE = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),

    ]
    VEHICLE_TRANS_CHOICE = [
        ('manual', 'Manual'),
        ('auto', 'Auto'),
        ('semi', 'semi-automatic'),
    ]

    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICE, default='car')
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    condition = models.CharField(max_length=5, choices=VEHICLE_CONDITION_CHOICE, default='new')
    year = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10, choices=VEHICLE_FUEL_CHOICE, default='petrol')
    engine_capacity = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=7, choices=VEHICLE_TRANS_CHOICE, default='manual')
    description = models.TextField(null=True)
    front = models.ImageField()
    back = models.ImageField()
    interior = models.ImageField()

    def __str__(self):
        return str(self.customer)
