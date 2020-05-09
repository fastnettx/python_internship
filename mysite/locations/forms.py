from django import forms
from .models import Country, City, Symbol


class AddCountry(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class AddCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'longitude', 'latitude')


class AddSymbol(forms.ModelForm):
    class Meta:
        model = Symbol
        fields = ('image',)
