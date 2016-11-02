from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Location(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=5,blank=True)
    longitude =models.DecimalField(max_digits=8, decimal_places=5, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length = 20, null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True,blank=True)



    def __str__(self):
        x = str(self.latitude) + ", " + str(self.longitude)
        return x
