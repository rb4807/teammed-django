from django import forms
from . models import Booking

class DateInput(forms.DateInput):
   input_type = 'date' 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booked': DateInput(),
        }

        labels = {
            'name' : "Patient Name:",
            'number': "Patient Number:",
            'doc' : "Doctor Name:",
            'booked':  "Booking Date:",
        }