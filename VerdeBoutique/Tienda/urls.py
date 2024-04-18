from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    # --------- Navegacion Simple ------------
    path('', views.intro, name='First'),
    path('Preview/', views.previewproduct, name='Preview'),
    path('Nosotros/', views.aboutus, name='About'),
    path('Home', views.home, name='Home'),
    path('#10Nosotros/', views.nosotroslog, name='NosL'),
    path('#11Prductos/', views.productslog, name='PrdL'),
    
    #------------ Login ----------------------
    
    path('Login/', views.login_request, name='Login'),
    path('Register', views.register, name='Registro'),
    path('Logout', LogoutView.as_view(template_name='FirstPage.html'), name='Logout'),
    
    #------------ Perfil ---------------------
    
    path('EditarPerfil', views.editarPerfil, name='EdtPrf'),
    
    #----------- Errores --------------------
    
    path('somethingwaswrong', views.wrongdata, name='Wrong'),
    
    
    # ---------- Manejo de Modelos ---------
    
    # ---- Productos ---
    path('StockActivo', views.ver_p, name='StockA'),
    path('agregar_producto', views.agregar_producto, name='Agregar'),
    path('editprod/<int:id>', views.edit_p, name='EdtPro'),
    path('delprod/<int:id>', views.del_p, name='DelProd'),
    
    # --- Categorias ---
    
    path('Categorias', views.ver_cat, name='Cats'),
    path('AddCat', views.agregar_cat, name = 'AddCat'),
    path('editCat/<int:id>', views.edit_cat, name='EdtCat'),
    path('delCat/<int:id>', views.del_cat, name='DelCat'),
    
    # --- Proovedores ---
    
    path('Proveedores', views.ver_prov, name='Proveedor'),
    path('AddProv', views.agregar_prov, name='AddProv'),
    path('editProv/<int:id>', views.edit_prov, name='EdtProv'),
    path('delProv/<int:id>', views.del_prov, name='DelProv'),
    
    # --- Staff ---
    
    path('Staff', views.ver_s, name='SeeStaff'),
    path('AddStf', views.agregar_s, name='AddStf'),
    path('editStaff', views.edit_s, name='EdtStf'),
    path('delStaff', views.del_s, name='DelStf'),
    
    
]


