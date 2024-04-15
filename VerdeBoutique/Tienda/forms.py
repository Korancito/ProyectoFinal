from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Productos, Categoria


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        


class Productos_formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    cantidad = forms.IntegerField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = forms.DecimalField(max_digits=10, decimal_places=2)
    
    
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'cantidad', 'precio', 'precio_costo', 'categorias']

    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
class CatForm(forms.Form):
    nombre = forms.CharField(max_length=100)
