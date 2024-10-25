from django import forms
from .models import vehicle

#creating a form
class VehicleForm(forms.ModelForm):

    #create meta class
    class Meta:
        #specify model to be used 
        model = vehicle

        #specify fields to be used
        fields = [
            "placa",
            "marca",
            "modelo",
            "color_vehiculo"
        ]

        labels = {
            'placa': 'Numero de placa',
            'marca': 'Marca del vehiculo'
            'modelo': 'Modelo del vehiculo',
            'color_vehiculo': 'color del vehiculo'
        }

        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }
