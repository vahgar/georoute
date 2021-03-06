from django.db.models import Q
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from location.api.serializers import LocationSerializer, LocationCreateSerializer
from location.models import Location
from location.api.permissions import IsOwner

class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)



class LocationListAPIView(ListAPIView):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset_list = Location.objects.all()
        query = self.request.GET.get("q")

        if query:
            pnt = GEOSGeometry(query, srid=4326)
            queryset_list = Location.objects.filter(point__distance_lte=(pnt, D(km=15)))
        return queryset_list

class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class LocationUpdateAPIView(UpdateAPIView,RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LocationDeleteAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


# class SearchLocationListAPIView(ListAPIView):
#     serializer_class = LocationSerializer

#
# ''' eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhZ2hhdkBnbWFpbC5jb20iLCJleHAiOjE0Nzg4MDAwMTAsInVzZXJfaWQiOjEsImVtYWlsIjoicmFnaGF2QGdtYWlsLmNvbSJ9.VdUaYoCPcyn0_REk6GqTug0UFtbiXwoi4PHVJ0SOJlE '''
#
# curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhZ2hhdkBnbWFpbC5jb20iLCJleHAiOjE0Nzg4MDAwMTAsInVzZXJfaWQiOjEsImVtYWlsIjoicmFnaGF2QGdtYWlsLmNvbSJ9.VdUaYoCPcyn0_REk6GqTug0UFtbiXwoi4PHVJ0SOJlE" http://localhost:8000/location/create
