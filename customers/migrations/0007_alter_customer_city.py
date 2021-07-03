# Generated by Django 3.2.4 on 2021-07-03 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20210629_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('Vavuniya', 'Vavuniya'), ('Kalutara', 'Kalutara'), ('Puttalam', 'Puttalam'), ('Badulla', 'Badulla'), ('Mullaitivu', 'Mullaitivu'), ('Matara', 'Matara'), ('Mannar', 'Mannar'), ('Monaragala', 'Monaragala'), ('Galle', 'Galle'), ('Anuradhapura', 'Anuradhapura'), ('Jaffna', 'Jaffna'), ('Batticaloa', 'Batticaloa'), ('Hambantota', 'Hambantota'), ('Ampara', 'Ampara'), ('Ratnapura', 'Ratnapura'), ('Polonnaruwa', 'Polonnaruwa'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Kurunegala', 'Kurunegala'), ('Matale', 'Matale'), ('Kegalle', 'Kegalle'), ('Trincomalee', 'Trincomalee'), ('Gampaha', 'Gampaha'), ('Kandy', 'Kandy'), ('Kilinochchi', 'Kilinochchi'), ('Colombo', 'Colombo')], max_length=225),
        ),
    ]
