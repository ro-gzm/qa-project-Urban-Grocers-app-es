# Proyecto Urban Grocers 

## Descripción: Pruebas para el parámetro "name" al crear un/a usuario/a en UrbanGrocers
  - Este proyecto hace uso de Pycharm para automatizar pruebas de una lista de comprobación específica con 9 elementos.
  - Utilicé la documentación de APIdoc para crear nuevos kits con distintos nombres a probar, cada uno con su propio authorization token.
  - Las solicitudes se encuentran en sender_stand_request.py, haciendo una copia de los datos del archivo data.py
  - Creé una función para cambiar el el parametro "name" del cuerpo de solicitud de get_kit_body.
  - Las pruebas positivas y negativas se hicieron a partir de las funciones positive_assert(kit_body) y negative_assert_code_400(kit_body) respectivamente.
    
## Requerimientos:
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.

## Documentación: https://cnt-9d48880e-a3a9-4122-bfb8-04edcd9d60bf.containerhub.tripleten-services.com/docs/
