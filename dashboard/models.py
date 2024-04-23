from django.db import models

# Create your models here.

class Dataset(models.Model):
    ndvi = models.FloatField()
    lst = models.FloatField()
    burned_area = models.FloatField()
    classification= models.CharField(max_length=50)  # Assuming CLASS is a string
    longitude = models.FloatField()
    latitude = models.FloatField()
    month = models.CharField(max_length=50)  # Assuming month is a string (e.g., "January")
    
    def __str__(self):
        return f'Classification: {self.classification}, Month: {self.month}, NDVI: {self.ndvi}, LST: {self.lst}, Burned Area: {self.burned_area}, Latitude: {self.latitude}, Longitude: {self.longitude}'