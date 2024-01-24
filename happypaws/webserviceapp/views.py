from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseNotFound, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from .models import Tanimales;
#COMPROBAMOS QUE FUNCIONE CORRECTAMENTE EN EL NAVEGADOR CON UN EJEMPLO 
def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola wey</hq>");
#ESTA SERÁ LA PÁGINA DE ACOGIDAS, DONDE TENDREMOS TODO EL LISTADO DE ANIMALES CON: IMG/NOM/
def pagAcogida(request):
    try:
        lista = Tanimales.objects.all()
        respuesta_final = []
        for fila_sql in lista:
            diccionario = {
#EN CASO DE DE QUE SI MUESTRE LOS ANIMALES, NOS APARECERÁ UN 200(OK)
                'status': 'OK',
                'id': fila_sql.id,
                'nombre': fila_sql.nombre,
                'url_imagen': fila_sql.url_imagen
            }
            respuesta_final.append(diccionario)
        return JsonResponse(respuesta_final, safe=False)
    except Tanimales.DoesNotExist:
#EN CASO DE NO ENCONTRAR NADA, NOS MOSTRARÁ UN 404(NOT FOUND)
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró el animal'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})

#información que obtendremos mediante la id de los animales de la acogidas

def pagInfAnimales_solicitado(request, id_solicitado):
    try:
        # Intentar obtener el animal con la ID solicitada
        animal = Tanimales.objects.get(id=id_solicitado)

        # Crear el diccionario de resultado con la información del animal
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
        # Manejar el caso en que no se encuentre el animal
        mensaje_error = {'status': 'Error', 'error': '404 No se encontró el animal'}
        return JsonResponse(mensaje_error, status=404, json_dumps_params={'ensure_ascii': False})
#PAGINA PRINCIPAL
#MUESTRA QUÉ TABLAS? -> CREAR UNA TABLA TpagPrincipal PARA QUE NOS MUESTRE LAS IMAGENES
#CON UNA PEQUEÑA INFORMACIÓN DE LAS IMAGENES

#FUNCION DE LOGOUT, IRÁ VICULADO CON LA VENTANA DE CERRAR SESION
def cerrar_sesion(request):
    if request.method == 'PATCH':
        # Obtén el token de la solicitud
        token = request.POST.get('Token')
        # Cierra la sesión
        logout(request)
        # Devuelve una respuesta exitosa
        return JsonResponse({'mensaje': 'Sesión cerrada exitosamente'}, status=200)
    # Si la sesión no se encuentra, redirige a la página de inicio 
    elif request.method == 'GET':
        return HttpResponseRedirect('/PagPrincipal/', status=302)
    # Si la solicitud no es de tipo PATCH ni GET, devuelve un error 404 Método no permitido
    return JsonResponse({'error': 'El servidor no consigue encontrar la sesión para cerrar'}, status=404)

