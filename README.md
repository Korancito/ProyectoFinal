
Staff01 - Gg987413? (User - Staff)
kamo - Gg987413? (User - User)
koran - GG987413 (User - Superuser)


Se crean los modelos

Categorias
Productos
Proveedores
Staff

Se genera relacion de dependencia (no requisitoria) entre Categorias y Productos, cada ingreso de producto, tiene posibilidad de ingresarse bajo una Categoria.
Teniendo entre si Categorias y Producto Primary Key - Foregein Key


El acceso y manejo de los modelos esta limitado a User-Staff, siendo quien puede Editar, Eliminiar, Añadir valores a todos los modelos.
El concepto de la web, User-User interactua con un carrito ==EN CONSTRUCCION== y User-Staff es quien se ocupa de gestionar los productos y/o datos que estan por encima del acceso del User-User.

**el nivel de acceso 'Staff' lo brinda el administrador desde /admin**

**el listado de formularios no refleja el nombre los mismos**

===Usuarios===
<>Login</>
<>Registro</>
<>EditUser</>

===Modelos===
<>AddProducto</>
<>EditProducto</>
<>AddCategoria</>
<>EditCategoria</>
<>AddProveedor</>
<>EditProveedor</>
<>AddStaff</>
<>EditStaff</>


<>EditUser</> 
El formulario de edicion de usuario tiene la capacidad de modificar todos los datos del usuario, ademas de agregar o cambiar la imagen de avatar.




VerdeBoutique. **WEB**

FirstPage = Pagina de acceso, menu a 'Productos' y 'Nosotros', sin contenido sensible, a modo de "Muestra al cliente"
<> Ingresa </>

Login = Acceso a formulario de creacion de usuario/ Acceeso a 'Home' (Pagina Principal)



**USER-USER**


Home = (como User-User)
Accesibilidad a :
'Nosotros / Conocenos' - Visualizacion simple
'Productos / Todos los productos' - Visualizacion simple
'Productos / Frutas' ==EN CONSTRUCCION==
'Productos / Verduras' ==EN CONSTRUCCION==
'Productos / Otros' ==EN CONSTRUCCION==
'Nuestros Proveedores / ¿Quienes son?' - Visualizacion simple
'Comprar' ==EN CONSTRUCCION== 
(fas fa-user-circle) Para opciones de Usuario// (Muestra nombre de usuario) // Edicion de Usuario // Logout // 
 ==Avatar==
El acceso de User-User esta limitado actualmente a visualizaciones, no tiene funcionalidades mas alla de su edit de usuario.

**USER-STAFF**

Home = (como User-Staff)
Accesibilidad a:

'Nosotros / Staff List' = Visualizacion de lista de 'Staff' // Formularios de Edicion / Eliminacion (del Modelo)
'Nosotros / Añadir Staff' = Formulario para incorporar staff al listado
'Productos / Stock Activo = Visualizacion de lista de 'Productos' // Formularios de Edicion / Eliminacion (del Modelo) // 'Categorias' acceso a listado de categorias // 'Agregar Producto' formulario para Añadir producto
'Productos / Añadir Producto' = Formulario para incorporar producto al listado 
'Productos / Categorias' = Visualizacion ded lista de 'Categorias' // Formularios de Edicion / Eliminacion (del Modelo) // 'Añadir Categoria' Formulario para incorporar categoria.
'Nuestros Proveedores / Proveedores' = Visualizacion de lista de 'Proveedor' // Formularios de Edicion / Eliminacion (del Modelo) / 'Añadir Proveedor' Formulario para incorporar proveedor
'Nuestros Proveedores / Añadir Proveedores' = Formulario para incorporar proveedor al listado.

Edicion de usuario, logout, nombre de usuario logueado, en las mismas condiciones que User-User
 ==Avatar==




