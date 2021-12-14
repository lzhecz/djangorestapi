from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer, VDSerializer
from .created import DriverFilter


class DriverListView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_class = DriverFilter
    filter_backends = (DjangoFilterBackend,)


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class VehicleListView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers_param = self.request.query_params.get('with_drivers')
        print(with_drivers_param)

        if with_drivers_param == 'no':
            queryset = queryset.filter(driver_id__isnull = True)
        elif with_drivers_param == 'yes':
            queryset = queryset.filter(driver_id__isnull = False)

        return queryset


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class SetDriverView(generics.CreateAPIView):
    serializer_class = VDSerializer
    queryset = Vehicle.objects.all()
    lookup_url_kwarg = "pk"
    lookup_field = "id"

    def create(self, request, pk):
        vehicle = self.get_object()
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        vehicle.driver_id = serializer.data["driver"]
        vehicle.save()

        return Response(VehicleSerializer(instance = vehicle).data)
