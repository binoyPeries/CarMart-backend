# Generated by Django 3.2.4 on 2021-07-16 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_alter_customer_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('Trincomalee', 'Trincomalee'), ('Puttalam', 'Puttalam'), ('Batticaloa', 'Batticaloa'), ('Kandy', 'Kandy'), ('Kurunegala', 'Kurunegala'), ('Mannar', 'Mannar'), ('Polonnaruwa', 'Polonnaruwa'), ('Kilinochchi', 'Kilinochchi'), ('Ampara', 'Ampara'), ('Hambantota', 'Hambantota'), ('Ratnapura', 'Ratnapura'), ('Anuradhapura', 'Anuradhapura'), ('Gampaha', 'Gampaha'), ('Colombo', 'Colombo'), ('Vavuniya', 'Vavuniya'), ('Kegalle', 'Kegalle'), ('Matale', 'Matale'), ('Badulla', 'Badulla'), ('Kalutara', 'Kalutara'), ('Galle', 'Galle'), ('Mullaitivu', 'Mullaitivu'), ('Matara', 'Matara'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Monaragala', 'Monaragala'), ('Jaffna', 'Jaffna')], max_length=225),
        ),
    ]