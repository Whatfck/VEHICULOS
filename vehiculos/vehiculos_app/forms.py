from django import forms
from .models import Vehiculo

# crear un form
class VehiculoForm(forms.ModelForm):

    # crear metaclass
    class Meta:
        #especificar el modelo a utilizar
        model = Vehiculo

        # especificar los campos que se uzaran
        fields = [
            "placa",
            "marca",
            "modelo",
            "color_vehiculo"
        ]

        # especificar las etiquetas para usar
        labels = {
            "placa": "Numero de Placa",
            "marca": "Marca del vehiculo",
            "modelo": "Modelo del vehiculo",
            "color_vehiculo": "Color del Vehículo"
        }

        # especificar las validaciones
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }