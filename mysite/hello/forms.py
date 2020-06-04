from django import forms

class FormularioDeBusqueda(forms.Form):
    valor= forms.CharField(label="valor",required=False, widget=forms.TextInput(
        attrs={ 'class': 'form-control border-dark','placeholder': 'Search...'}
    ), max_length=100)
