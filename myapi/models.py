from django.db import models
# Driver:
# + id: int
# + first_name: str
# + last_name: str
# + created_at
# + updated_at
#
# Vehicle
# + id: int
# + driver_id: FK to Driver
# + make: str
# + model: str
# + plate_number: str  - format example "AA 1234 OO"
# + created_at
# + updated_at


class Driver(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.first_name


class Vehicle(models.Model):
    driver = models.ForeignKey('Driver', blank = True, null = True, on_delete = models.SET_NULL)
    make = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    plate_number = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.model
