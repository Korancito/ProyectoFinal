from django.shortcuts import render, redirect
from Tienda.models import Categoria, Productos, Proveedor, Staff, Avatar
from django.http import HttpResponse
from django.template import loader
from Tienda.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required





# ----------- Login / Registro -----------------

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contra) 
            
            if user is not None:
                login(request, user)
                return redirect('Home')     
            
            else:
                return HttpResponse(f"usuario no encontrado")      
        else:
            return HttpResponse(f"Form Incorrecto, {form}")   
        
        
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

#------------------EditUser ----------------------

@login_required
def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        miform = UserEditForm(request.POST, request.FILES, instance=request.user)
        
        if miform.is_valid():
            datos = miform.cleaned_data
            usuario.username = datos['username']
            usuario.first_name = datos['first_name']
            usuario.last_name = datos['last_name']
            usuario.email = datos['email']
            
            avatar_get= miform.cleaned_data.get('imagen')
            
            if avatar_get:
                
                try:
                    avatar = Avatar.objects.get(user=usuario)
                    avatar.image = avatar_get
                    avatar.save()
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, image=avatar_get)
                    avatar.save()
                    
            usuario.save()             
            miform.save()
            
            return render(request,"Home.html")
        
    else:
        miform = UserEditForm(instance=request.user)
    
    return render(request, "#14EdtPrf.html", {'miform':miform, 'usuario':usuario})

# -------------- Errores ------------------------

def wrongdata(request):
    return redirect('Wrong')

# ---------------- Navegacion Simple ------------

def intro(request):
    return render(request, "FirstPage.html")

@login_required
def home(request):
    return render(request, "Home.html")

def previewproduct(request):
    return render(request, "PreviewProducts.html")

def aboutus(request):
    return render(request, "Nosotros.html")


@login_required
def nosotroslog(request):
    return render(request, "#10Nosotros.html")


@login_required
def productslog(request):
    return render(request, "#11Products.html")



# -------------- Staff Only ------------------ #

# ------------- Manejo de Modelos ----------- #

# ------------ Productos ------------------- #

@staff_member_required
def ver_p(request):
   productos = Productos.objects.all()
   dicc = {'productos':productos}
   return render(request, '#2StockActivo.html', dicc)

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

@staff_member_required
def edit_p(request, id):
    producto = Productos.objects.get(id=id)
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            producto.nombre = datos['nombre']
            producto.cantidad = datos['cantidad']
            producto.precio = datos['precio']
            producto.precio_costo = datos['precio_costo']
            producto.save()
            productos = Productos.objects.all()
            
            return render(request, "#2StockActivo.html", {"productos":productos} )
    
    else:
        form = ProductForm(initial={'nombre':producto.nombre, 'cantidad':producto.cantidad, 'precio':producto.precio, 'precio_costo':producto.precio_costo})
    
    return render(request, "#9EditProd.html", {'form':form, 'producto':producto})

@staff_member_required
def del_p(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    
    productos = Productos.objects.all()
    return render(request, "#2StockActivo.html", {"productos": productos})


# -------------- Staff --------------


@staff_member_required
def ver_s(request):
    pass

@staff_member_required
def agregar_s(request):
    pass

@staff_member_required
def edit_s(request):
    pass

@staff_member_required
def del_s(request):
    pass

# --------------- Proveedores ------------


@staff_member_required
def ver_prov(request):
    proveedores = Proveedor.objects.all()
    dicc = {"proveedores": proveedores}
    return render(request, "#6ProveedorList.html", dicc)

@staff_member_required
def agregar_prov(request):
    
    if request.method == 'POST':
        
        formP = ProvForm(request.POST)
        if formP.is_valid():
            datos = formP.cleaned_data
            formprov = Proveedor(razonsocial=datos["razonsocial"], nombre=datos["nombre"], rut=datos["rut"], giro=datos["giro"])
            formprov.save()
            return redirect('Proveedor')
        
    return render(request, "#5AddProv.html")

@staff_member_required
def edit_prov(request,id):
    proveedor = Proveedor.objects.get(id=id)
    
    if request.method == "POST":
        form = ProvForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            proveedor.razonsocial = datos['razonsocial']
            proveedor.nombre = datos['nombre']
            proveedor.rut = datos['rut']
            proveedor.giro = datos['giro']
            proveedor.save()
            proveedores = Proveedor.objects.all()
            
            return render(request, "#2StockActivo.html", {"proveedores":proveedores} )
    
    else:
        form = ProvForm(initial={'razonsocial':proveedor.razonsocial, 'nombre':proveedor.nombre, 'rut':proveedor.rut, 'giro':proveedor.giro})
    
    return render(request, "#12EditProv.html", {'form':form, 'proveedor':proveedor})

@staff_member_required
def del_prov(request,id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    
    proveedores = Proveedor.objects.all()
    return render(request, "#6ProveedorList.html", {"proveedores":proveedores})


# ------------- Categorias ----------------


@staff_member_required
def ver_cat(request):
    categorias = Categoria.objects.all()
    dicc = {"categorias": categorias}
    return render(request, '#4CategoriaActiva.html', dicc)

@staff_member_required
def agregar_cat(request):
    
    if request.method == 'POST':
        
        form = CatForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            formulario = Categoria(nombre=datos["nombre"])
            formulario.save()
            return redirect('Cats')
        
    return render(request, "#3AddCat.html")

@staff_member_required
def edit_cat(request, id):
    categoria = Categoria.objects.get(id=id)
    
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            categoria.nombre = datos['nombre']
            categoria.save()
            categorias = Categoria.objects.all()
            
            return render(request, "#4CategoriaActiva.html", {"categorias":categorias} )
    
    else:
        form = CatForm(initial={'nombre':categoria.nombre})
    
    return render(request, "#13EditCat.html", {'form':form, 'categoria':categoria})

@staff_member_required
def del_cat(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    
    categorias = Categoria.objects.all()
    return render(request, "#4CategoriaActiva.html", {"categorias":categorias})


    
