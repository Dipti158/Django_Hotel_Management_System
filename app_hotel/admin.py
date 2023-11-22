from django.contrib import admin

# Register your models here.

from .models import Room, Reservation, Customer, Staff

# Register your models here.

# To Register All Models
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Customer)
admin.site.register(Staff)
