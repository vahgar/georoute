from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from location.api.serializers import LocationSerializer, LocationCreateSerializer
from location.models import Location


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



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
