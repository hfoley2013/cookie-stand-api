from django import forms
from .models import CookieStand

class CookieStandForm(forms.ModelForm):
    class Meta:
        model = CookieStand
        fields = ['location', 'owner', 'description', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale']
        widgets = {
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }
