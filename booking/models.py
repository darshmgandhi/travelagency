from django.db import models

# Create your models here.
class Booking(models.Model):
    CITY_CHOICES = [
        ('Delhi','Delhi'),
        ('Mumbai','Mumbai'),
        ('Allahbad','Allahbad'),
        ('Chennai','Chennai'),
        ('Agra','Agra'),
        ('Rameshwaram','Rameshwaram'),
        ('Hyderabad','Hyderabad'),
        ('Goa','Goa')
    ]

    FLIGHT_CLASS_CHOICES = [
        ('E', 'Economy'),
        ('P', 'Premium Economy'),
        ('B', 'Business')
    ]

    full_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 80)
    address = models.TextField(max_length = 400)
    city = models.CharField(max_length = 30, choices = CITY_CHOICES, default = 'Delhi')
    date = models.DateField()
    travellers = models.PositiveIntegerField()
    flight_class = models.CharField(max_length = 20, choices = FLIGHT_CLASS_CHOICES, default = 'E')
    budget = models.FloatField()
    id_proof = models.ImageField(upload_to = '')
    additional = models.CharField(max_length = 20, blank = True)
    student = models.BooleanField()

    class Meta:
        db_table = 'Booking'