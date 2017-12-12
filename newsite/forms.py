from django import forms

from .models import Region, District


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('name', 'population', 'field', 'center', 'governer', 'about')


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = ('name', 'center', 'about', 'region')
