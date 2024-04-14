from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    # --------- Navegacion Simple ------------
    path('', views.intro, name='First'),
    path('Preview/', views.previewproduct, name='Preview'),
    path('Nosotros/', views.aboutus, name='About'),
    path('Home/', views.home, name='Home'),
    
    #------------ Login ----------------------
    
    path('Login/', views.login_request, name='Login'),
    path('Register', views.register, name='Registro'),
    path('Logout', LogoutView.as_view(template_name='FirstPage.html'), name='Logout'),
    
    #----------- Errores --------------------
    
    path('somethingwaswrong', views.wrongdata, name='Wrong'),
    
    
    # ---------- Manejo de Modelos ---------
    
    # ---- Productos ---
    path('StockActivo', views.ver_p, name='StockA'),
    path('agregar_producto', views.agregar_producto, name='Agregar'),
    
    # --- Categorias ---
    
    path('Categorias', views.ver_cat, name='Cats'),
    path('AddCat', views.agregar_cat, name = 'AddCat'),
    
    # --- Proovedores ---
    
    path('Proveedores', views.ver_p, name='Proveedor'),
    path('AddProv', views.agregar_prov, name='AddProv'),
    
    # --- Staff ---
    
    path('Staff', views.ver_s, name='SeeStaff'),
    path('AddStf', views.agregar_s, name='AddStf'),
    
    
]


