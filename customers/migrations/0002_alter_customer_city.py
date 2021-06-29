# Generated by Django 3.2.4 on 2021-06-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('Colombo', 'Colombo'), ('Kalutara', 'Kalutara'), ('Mullaitivu', 'Mullaitivu'), ('Trincomalee', 'Trincomalee'), ('Vavuniya', 'Vavuniya'), ('Matara', 'Matara'), ('Galle', 'Galle'), ('Monaragala', 'Monaragala'), ('Puttalam', 'Puttalam'), ('Hambantota', 'Hambantota'), ('Kurunegala', 'Kurunegala'), ('Ratnapura', 'Ratnapura'), ('Badulla', 'Badulla'), ('Polonnaruwa', 'Polonnaruwa'), ('Batticaloa', 'Batticaloa'), ('Gampaha', 'Gampaha'), ('Ampara', 'Ampara'), ('Jaffna', 'Jaffna'), ('Kilinochchi', 'Kilinochchi'), ('Mannar', 'Mannar'), ('Kegalle', 'Kegalle'), ('Kandy', 'Kandy'), ('Matale', 'Matale'), ('Anuradhapura', 'Anuradhapura'), ('Nuwara Eliya', 'Nuwara Eliya')], max_length=225),
        ),
    ]
