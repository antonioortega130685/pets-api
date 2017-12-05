# pets-api
codigo de web api en django rest framework

Proyecto que integra una app semi-personalizada de registro y login con django crispy forms

Se utiliza una API con operaciones de CRUD (Create/Retrieve/Update/Delete) sobre las mascotas, pudiendo ser llevadas a cabo sólo por su dueño.

La aplicación esta en inglés, porque salió de una solicitud en una entrevista laboral.

Se utilizaron: 

Python 3.6
Django 1.11.5
Crispy forms
Django Rest Framework
Markdown

Se requiere instalación de todos estos paquetes.

se puede acceder a la api tirando el runserver y accediendo a localhost....
/api/pets              para listado
/api/pets/create       para crear mascota
/api/pets/#            siendo # el numero de mascota
/api/pets/#/edit
/api/pets/#/detail
/api/pets/#/delete

Sólo el dueño puede realizar cambios

Tambien se puede acceder al registro mediante localhost....
/register/
y login
/login/

y como de costumbre, el admin
/admin/
