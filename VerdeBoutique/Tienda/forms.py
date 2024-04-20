from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Productos, Categoria


# ----------- Usuario Custom

class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
# ----------- Edicion de Usuario
class UserEditForm(UserChangeForm):
    
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    imagen = forms.ImageField(label="avatar", required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'imagen']

# ----------- Productos

class Productos_formulario(forms.Form):  #No esta en uso
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

# ----------- Categorias   
    
class CatForm(forms.Form):
    nombre = forms.CharField(max_length=100)

# ----------- Proveedores

class ProvForm(forms.Form):
    razonsocial = forms.CharField(max_length=60)
    nombre = forms.CharField(max_length=60)
    rut = forms.IntegerField()
    giro = forms.CharField(max_length=60)

# ----------- Staff    
    
class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    status = forms.CharField(max_length=100)
    contacto = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    
    