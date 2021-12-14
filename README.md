# djangorestapi
Rest Api project for vehicle park with drivers

Task for Yalantis Python School

It contains next two models:

Driver:
 + id: int
 + first_name: str
 + last_name: str
 + created_at
 + updated_at

Vehicle
 + id: int
 + driver_id: FK to Driver
 + make: str
 + model: str
 + plate_number: str  - format example "AA 1234 OO"
 + created_at
 + updated_at
 
 Can work with open endpoint for next operations:
 Driver:
+ GET /drivers/driver/ - output driver list
+ GET /drivers/driver/?created_at__gte=10-11-2021 - outpud driver list created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 -  outpud driver list created before 16-11-2021

+ GET /drivers/driver/<driver_id>/ - output driver info for certain drive
+ POST /drivers/driver/ - create new driver
+ UPDATE /drivers/driver/<driver_id>/ - edit driver
+ DELETE /drivers/driver/<driver_id>/ - delete driver

Vehicle:
+ GET /vehicles/vehicle/ - output vehicles list
+ GET /vehicles/vehicle/?with_drivers=yes - output vehicles list with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output vehicles list without drivers

+ GET /vehicles/vehicle/<vehicle_id> - output vehicle info for certain vehicle
+ POST /vehicles/vehicle/ - create new vehicle
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - edit vehicle
+ POST /vehicles/set_driver/<vehicle_id>/ - set/unset driver in vehicle
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete vehicle

