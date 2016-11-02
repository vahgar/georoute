from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from location.api.serializers import LocationSerializer
from location.models import Location


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationUpdateAPIView(UpdateAPIView,RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDeleteAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
