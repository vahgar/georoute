from django.contrib.gis.db import models
from accounts.models import CustomUser

# Create your models here.

class RoadIssues(models.Model):
    name = models.CharField(max_length=20)

class Location(models.Model):
    point = models.PointField(default='POINT(77.1025 28.7041)', srid=4326)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length = 20, null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True,blank=True)
    lat = models.FloatField(blank=True,null=True)
    lon = models.FloatField(blank=True,null=True)

    @property
    def longitude(self):
        return self.point[0]

    @property
    def latitude(self):
        return self.point[1]

    def __str__(self):
        x = str(self.point[0]) + ", " + str(self.point[1])
        return x

    def save(self, *args, **kwargs):
        self.lat = self.point[0]
        self.lon = self.point[1]
        super(Location, self).save(*args, **kwargs)
