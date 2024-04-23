from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Define a one-to-one relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Define fields for other data in your form
    profession = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Profile"