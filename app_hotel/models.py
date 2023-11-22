from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Model For Room
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=255)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

# Model For Reservation
class Reservation(models.Model):
    customer_name = models.CharField(max_length=255)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation for {self.customer_name}"


# Model For Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    # reservations = models.ManyToManyField(Reservation)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Model For Staff
class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
