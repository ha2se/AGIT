
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.db.models import QuerySet
from dashboard.models import Dataset
import random
def dashboard(request):
    return render(request,'dashboard.html')

class RandomDataView(View):
    def get(self, request):
        # Get latitude and longitude from request
        latitude_str = request.GET.get('latitude')
        longitude_str = request.GET.get('longitude')
        
        # Validate input parameters
        if not latitude_str or not longitude_str:
            return HttpResponseBadRequest('Latitude and longitude are required.')
        
        try:
            # Convert latitude and longitude to float
            latitude = float(latitude_str)
            longitude = float(longitude_str)
        except ValueError:
            return HttpResponseBadRequest('Invalid latitude or longitude values.')
        
        # Define the radius for filtering data
        radius = 0.56  # Adjust the radius as needed

        # Query data within the specified range
        data = Dataset.objects.filter(
            latitude__range=(latitude - radius, latitude + radius),
            longitude__range=(longitude - radius, longitude + radius)
        )

        # If no data is available within the specified range, sample data from the entire Dataset
        if not data.exists():
            # Randomly sample data from the entire Dataset
            all_data = Dataset.objects.all()
            sample_size = 5  # Adjust the sample size as needed
            random_data = random.sample(list(all_data), sample_size)
        else:
            # Choose a random sample of up to 5 data points from the filtered data
            sample_size = min(data.count(), 5)
            random_data = random.sample(list(data), sample_size)
            print('Sampled data:', random_data)
        # Convert the data to JSON format
        response_data = [{
            'ndvi': d.ndvi,
            'lst': d.lst,
            'burned_area': d.burned_area,
            'longitude': d.longitude,
            'latitude': d.latitude,
            'month': d.month,
        } for d in random_data]

        # Return the response data as JSON
        return JsonResponse(response_data, safe=False)
  