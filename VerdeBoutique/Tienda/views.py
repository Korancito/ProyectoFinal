from django.shortcuts import render, redirect
from Tienda.models import Categoria, Productos
from django.http import HttpResponse
from django.template import loader
from Tienda.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required





# ----------- Login / Registro -----------------

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=passw)
            
            if user is not None:
                login(request, user)
                return redirect('Home')
            
            else:
                return HttpResponse(f"usuario no encontrado")
            
        else:
            return render(request, "wrongdata.html")
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})
    
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Valid", form)
            form.save()
            return redirect('Login')
            
        else:
            return render(request, "wrongdata.html")
            
    else:
        form = CustomUserCreationForm()
        return render(request, "register.html", {"form":form})


# -------------- Errores ------------------------

def wrongdata(request):
    return redirect('Wrong')



# ---------------- Navegacion Simple ------------

def intro(request):
    return render(request, "FirstPage.html")

def home(request):
    return render(request, "Home.html")


def previewproduct(request):
    return render(request, "PreviewProducts.html")

def aboutus(request):
    return render(request, "Nosotros.html")











# ----------------- Staff Only ------------------
# ----------------- Manejo de Modelos -----------

# ------------ Productos -------------

@staff_member_required
def ver_p(request):
    productos = Productos.objects.all()
    dicc = {"productos": productos}
    plantilla = loader.get_template("#2StockActivo.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

@staff_member_required
def agregar_producto(request):
    if request.method == "POST":
       
        formulario = ProductForm(request.POST)
       
        if formulario.is_valid():
       
            datos = formulario.cleaned_data
            categoria_seleccion = datos["categorias"]
       
            if categoria_seleccion.exists():
                categoria = categoria_seleccion.first()
                producto = Productos(nombre=datos["nombre"], cantidad=datos["cantidad"], 
                                    precio=datos["precio"], precio_costo=datos["precio_costo"], 
                                    categoria=categoria)
                producto.save()
       
                print("Producto validado y guardado")
                
                return redirect('StockA')  
        else:
            print("Formulario no válido:", formulario.errors)
    else:
       
        formulario = ProductForm()
    
    
    categorias = Categoria.objects.all()
    context = {"formulario":formulario, "categorias":categorias}
    
    return render(request, "#1AddProd.html", context)


# -------------- Staff --------------
def ver_s(request):
    pass

def agregar_s(request):
    pass


# --------------- Proveedores ------------

def ver_prov(request):
    pass

def agregar_prov(request):
    pass


# ------------- Categorias ----------------

def ver_cat(request):
    categorias = Categoria.objects.all()
    dicc = {"categorias": categorias}
    plantilla = loader.get_template("#4CategoriaActiva.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def agregar_cat(request):
    
    if request.method == 'POST':
        
        form = CatForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            formulario = Categoria(nombre=datos["nombre"])
            formulario.save()
            return redirect('Cats')
        
    return render(request, "#3AddCat.html")
