from django import forms
from datetime import date
from booking.models import Booking

class BookingForm(forms.ModelForm):

    class Meta:

        ADDITIONAL_CHOICES = [
        ('F', 'Food'),
        ('N', 'Non-Stop'),
        ('R', 'Refundable')
        ]

        model = Booking
        fields = '__all__'

        labels = {
            'student': 'Are you a Student?:',
            'additional': 'Additional Services:',
            'budget': 'Budget(In Rupees):',
            'city': 'Destination'
        }

        widgets = {
            'date': forms.DateInput(attrs = {'type': 'date', 'min': str(date.today())}),
            'flight_class': forms.RadioSelect(),
            'additional': forms.CheckboxSelectMultiple(choices = ADDITIONAL_CHOICES)
        }
