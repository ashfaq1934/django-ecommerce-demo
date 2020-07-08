from django import forms
from .models import OrderDetails

class OrderDetailsForm(forms.ModelForm):
    default = forms.BooleanField(label="Make Default", required=False)
    class Meta:
        model = OrderDetails
        fields = ['address', 'city', 'county', 'postal_code', 'phone_number']
