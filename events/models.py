from django.db import models
from django.core.validators import RegexValidator

email_validators = RegexValidator(regex=r'^[a-zA-Z0-9_.-]+@+gmail.com$', message="Email formatini '@gmail.com' shaklida kiriting")
phone_validators = RegexValidator(regex=r'^\+998[0-9]{9}$', message="Telefon nomer '+998' dan keyin 9 ta raqamdan iborat bo'lishi kerak.")


class Event(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[email_validators])
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, validators=[phone_validators])

    def __str__(self):
        return self.full_name