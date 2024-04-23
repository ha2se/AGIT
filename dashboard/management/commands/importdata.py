import csv
from django.core.management.base import BaseCommand
from dashboard.models import Dataset  # Import your model

class Command(BaseCommand):
    help = 'Import dataset from CSV file'

    def handle(self, *args, **kwargs):
        # Specify the path to your CSV file
        csv_file_path = 'static/WildFires_DataSet.csv'
        
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Dataset.objects.create(
                    ndvi=row['NDVI'],
                    lst=row['LST'],
                    burned_area=row['BURNED_AREA'],
                    classification=row['CLASS'],
                    longitude=row['longitude'],
                    latitude=row['latitude'],
                    month=row['month']
                )
        self.stdout.write(self.style.SUCCESS('Dataset imported successfully'))