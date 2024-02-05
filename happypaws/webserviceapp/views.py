from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from .models import Tanimales
from django.views.decorators.csrf import requires_csrf_token
from .models import Tproductos
from .models import Tnoticias
# Función de prueba para verificar si la aplicación funciona correctamente en el navegador
#def pagina_de_prueba(request):
 #   return HttpResponse("<h1>Hola wey</hq>")

# Vista que muestra el listado de animales de acogida con sus ID, nombres e URLs de imagen
def pagAcogida(request):
    try:
        lista = Tanimales.objects.all()
        respuesta_final = []

        for fila_sql in lista:
            diccionario = {
                'status': 'OK',
                'id': fila_sql.id,
                'nombre': fila_sql.nombre,
                'url_imagen': fila_sql.url_imagen
            }
            respuesta_final.append(diccionario)

        return JsonResponse(respuesta_final, safe=False)
    except Tanimales.DoesNotExist:
        # Si no se encuentra ningún animal, devuelvo un JSON con un mensaje de error y un código de estado 404
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró el animal'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})


#-------------------------------------------------------------------------------------------------------------------
# Vista que muestra información detallada sobre un animal específico solicitado por su ID
def pagInfAnimales_solicitado(request, id_solicitado):
    try:
        # Intento obtener el animal con la ID solicitada
        animal = Tanimales.objects.get(id=id_solicitado)

        # Creo el diccionario de resultado con la información del animal
        resultado = {
            'status': 'OK',
            'id_solicitado': id_solicitado,
            'nombre': animal.nombre,
            'url_imagen': animal.url_imagen,
            'edad': animal.edad,
            'especie': animal.especie,
            'raza': animal.raza,
            'genero': animal.genero,
            'descripcion': animal.descripcion
        }

        return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})
    except Tanimales.DoesNotExist:
        # Manejo el caso en que no se encuentre el animal
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró el animal con dicha id'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})

#-----------------------------------------------------------------------------------------------------------------------------
def pagProductos(request):
    try:
        lista = Tproductos.objects.all()
        respuesta_final = []
        for fila_sql in lista:
            diccionario = {
                'status': 'OK',
                'id': fila_sql.id,
                'nombre': fila_sql.nombre,
                'url_imagen': fila_sql.url_imagen,
		'precio': fila_sql.precio
            }
            respuesta_final.append(diccionario)

        return JsonResponse(respuesta_final, safe=False)
    except Tproductos.DoesNotExist:
        # Si no se encuentra ningún animal, devuelvo un JSON con un mensaje de error y un código de est>
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró el producto'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def pagInfProducto_solicitado(request, id_solicitado):
    try:
        # Intento obtener el producto con la ID solicitada
        producto = Tproductos.objects.get(id=id_solicitado)

        # Creo el diccionario de resultado con la información del producto
        resultado = {
            'status': 'OK',
            'id_solicitado': id_solicitado,
            'nombre': producto.nombre,
            'url_imagen': producto.url_imagen,
            'precio': producto.precio,
            'marca': producto.marca,
            'stock': producto.stock,
            'tipoProducto': producto.tipoproducto,
            'tipoAnimal': producto.tipoanimal,
            'descripcion': producto.descripcion
        }

        return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})
    except Tproductos.DoesNotExist:
        # Manejo el caso en que no se encuentre el producto
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró el producto con esa id'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})

#-----------------------------------------------------------------------------------------------------------------------------
# Página principal que redirige a la lista de animales de acogida
def pagPrincipal(request):
    return HttpResponseRedirect('/animales', status=302)



#------------------------------------------------------------------------------------------------------>
def pagNoticias(request):
    try:
        lista = Tnoticias.objects.all()
        respuesta_final = []
        for fila_sql in lista:
            diccionario = {
                'status': 'OK',
                'id': fila_sql.id,
                'nombre': fila_sql.nombre,
                'tituloPortada': fila_sql.tituloportada,
                'url_imagen': fila_sql.url_imagen,
                'info_noticia': fila_sql.info_noticia
            }
            respuesta_final.append(diccionario)

        return JsonResponse(respuesta_final, safe=False)
    except Tnoticias.DoesNotExist:
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró las noticias'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})
#-----------------------------------------------------------------------------------------------------------------------------
# Función de cierre de sesión
@requires_csrf_token
def cerrar_sesion(request):
    if request.method == 'PATCH':
        # Obtengo el token de los parámetros de la solicitud
        token = request.GET.get('token')

        # Verifico si el token es válido y realizo las acciones necesarias

        if token:
            # Cierro la sesión
            logout(request)
            # Devuelvo una respuesta exitosa
            return JsonResponse({'mensaje': 'Sesión cerrada exitosamente'}, status=200)
        else:
            # Si no se proporciona un token, devuelvo un error 404 Not Found
            return JsonResponse({'error': 'Token no encontrado'}, status=404)

    # Si la solicitud no es de tipo PATCH, redirijo a la página de inicio
    elif request.method == 'GET':
        return HttpResponseRedirect('/animales', status=302)

    # Si la solicitud no es ni PATCH ni GET, devuelvo un error 404 Not Found
    return HttpResponseNotFound('Not Found')

