from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomerManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, contact_no, city, password=None):
        if email is None:
            raise TypeError('User should have a email')
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          contact_no=contact_no, city=city)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, password=None):
        if password is None:
            raise TypeError('password can not be empty')
        if email is None:
            raise TypeError('User should have an email')
        user = self.create_user(email, first_name, '', '', '', password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    CITY_OPTIONS = {
        ('Ampara', 'Ampara'),
        ('Anuradhapura', 'Anuradhapura'),
        ('Badulla', 'Badulla'),
        ('Batticaloa', 'Batticaloa'),
        ('Colombo', 'Colombo'),
        ('Galle', 'Galle'),
        ('Gampaha', 'Gampaha'),
        ('Hambantota', 'Hambantota'),
        ('Jaffna', 'Jaffna'),
        ('Kalutara', 'Kalutara'),
        ('Kandy', 'Kandy'),
        ('Kegalle', 'Kegalle'),
        ('Kilinochchi', 'Kilinochchi'),
        ('Kurunegala', 'Kurunegala'),
        ('Mannar', 'Mannar'),
        ('Matale', 'Matale'),
        ('Matara',),
        ('Monaragala', 'Monaragala'),
        ('Mullaitivu', 'Mullaitivu'),
        ('Nuwara Eliya', 'Nuwara Eliya'),
        ('Polonnaruwa', 'Polonnaruwa'),
        ('Puttalam', 'Puttalam'),
        ('Ratnapura', 'Ratnapura'),
        ('Trincomalee', 'Trincomalee'),
        ('Vavuniya', 'Vavuniya')
    }

    email = models.EmailField(max_length=225, unique=True, db_index=True)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    contact_no = models.IntegerField(max_length=10)
    city = models.CharField(choices=CITY_OPTIONS, max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    object = CustomerManager

    def __str__(self):
        return self.email
