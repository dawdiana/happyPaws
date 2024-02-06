from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Tusuarios, Tanimales, Tproductos, Tnocitias
from django.contrib.auth.hashers import make_password, check_password
import json
import jwt
import datetime
import re

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import requires_csrf_token

#REGISTER - FUNCIONA
@csrf_exempt
def formulario_registro(request):
	if request.method!='POST':
		return JsonResponse({'error': 'Método no permitido'}, status = 405)

	json_peticion = json.loads(request.body)
	nombre = json_peticion['nuevo_nombre'] #variables
	ap1 = json_peticion['nuevo_ap1']
	ap2 = json_peticion['nuevo_ap2']
	correo = json_peticion['nueva_correo']
	nombreusuario = json_peticion['nuevo_nombreUsuario']
	contrasena = json_peticion['nueva_contrasena']
	conf_contrasena = json_peticion['confirmar_contrasena']

	#comprobación para campos vacíos
	if any(value is None or value == '' for value in [nombre, ap1, correo, nombreusuario, contrasena, conf_contrasena]):
		return JsonResponse({"Bad Request":"Faltan parametros o no son validos"}, status = 400)

	#Confirmar contraseña
	if len(contrasena) < 5: #largo de la contraseña
    		return JsonResponse({"Bad Request":"La contrasena debe tener al menos 5 caracteres"}, status = 400)

	if conf_contrasena !=contrasena: #contraseñas coinciden
		return JsonResponse({"Bad Request":"Las contrasenas no coinciden"}, status = 400)

	#Confirmar formato correo
	patron = '^[\w\.-]+@[\w\.-]+\.\w+$' #palabra@palabra.dominio #se podrían añadir más patrones

	if re.match(patron, correo) is None:
		return JsonResponse({"Bad request":"Formato de correo no valido"}, status = 400 )

	#Confirmar usuario no existe en la base de datos
	if Tusuarios.objects.filter(correo=correo).exists(): #correo electrónico
    		return JsonResponse({"Conflict":"El correo electronico ya esta registrado"}, status = 409)

	if Tusuarios.objects.filter(nombreusuario=nombreusuario).exists(): #nombre de usuario
		return JsonResponse({"Conflict":"El nombre de usuario ya existe"}, status = 409)

	#Cifrar contraseña
	contrasena_segura = make_password(contrasena)

	try:
		#GUARDAR USUARIO
		usuario = Tusuarios() #guardar datos después de comprobaciones
		usuario.nombre = nombre
		usuario.ap1 = ap1
		usuario.ap2 = ap2
		usuario.correo = correo
		usuario.nombreusuario = nombreusuario
		usuario.contrasena = contrasena_segura
		usuario.save()
		return JsonResponse({"Created":"Usuario registrado"}, status = 201)
	except Exception as e:
		print(str(e))
		return JsonResponse({"Error":f"Error de registro de usuario: {str(e)}"}, status=500)


#LOG-IN - FUNCIONA
@csrf_exempt
def inicio_sesion(request):
	if request.method!='POST':
		return JsonResponse({'error': 'Método no permitido'}, status = 405)

	json_peticion = json.loads(request.body)
	correo = json_peticion['ingresar_correo'] #variables
	contrasena =json_peticion['ingresar_contrasena']

        #Comprobación campos no vacíos
	if correo == '' or contrasena == '':
		 return JsonResponse({"Bad Request":"Faltan parametros"}, status = 400)

        #Comprobación correo está registrado
	try:
		usuario = Tusuarios.objects.get(correo=correo)
	except Tusuarios.DoesNotExist:
		return JsonResponse({"Unauthorized":"El correo proporcionado no esta registrado"}, status = 401)

	#Generar token
	def generar_jwt_token(usuario_id):
		payload = {
			'id':  usuario_id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1), # Token expira >
			'iat': datetime.datetime.utcnow(),
		}
		token = jwt.encode(payload, 'gatitosfelices123', algorithm='HS256')
		return token

	#Comprobación la contraseña es correcta
	if check_password(contrasena, usuario.contrasena): #si la contraseña es correcta, se genera el token, pero solo es correcta si la contraseña de la tabla está hasheada

		#generamos token del usuario
		token = generar_jwt_token(usuario.pk)
		usuario.token = token #asignamos el token al usuario y lo guardamos
		usuario.save()
		return JsonResponse({"OK":"Sesion iniciada con exito", "token": token}, status = 200)
	else:
		return JsonResponse({'Unauthorized':'La contrasena no es valida'}, status = 401)


#Verificar token
def verify_token(request):
	token = request.META.get('HTTP_AUTHORIZATION',None) #leemos token
	if not token: #si no existe
		return JsonResponse({'error':'No se ha identificado un token'}), None
	try:
		if token.startswith('Bearer '):
			token = token.split(' ')[1]

		payload = jwt.decode(token, 'gatitosfelices123', algorithms=['HS256'])
		return None, payload
	except jwt.ExpiredSignatureError:
		return JsonResponse({'error': 'Falta el token!'}, status = 401), None
	except jwt.InvalidTokenError:
		return JsonResponse({'error':'Token no válido!'}, status = 401), None

# EDITAR PERFIL - FUNCIONA
@csrf_exempt
def editar_perfil(request, id): #request se refiere a la información sobre la solicitud http
	error_response, payload = verify_token(request)
	if error_response:
		return error_response

	if request.method!='PATCH':
		return JsonResponse({'error': 'Método no permitido'}, status = 405)
	try:
		usuario = Tusuarios.objects.get(pk=payload['id']) #intenta obtener un objeto de la tabla con el id proporcionado en el token
		data = json.loads(request.body)

		#si alguno de los atributos presentes en los if están en el curl, se actualizarán los datos referenciados
		if 'nuevo_nombre' in data:
			usuario.nombre = data['nuevo_nombre']
		if 'nuevo_ap1' in data:
			usuario.ap1 = data['nuevo_ap1']
		if 'nuevo_ap2' in data:
			usuario.ap2 = data['nuevo_ap2']

		if 'nuevo_correo' in data:
			nuevo_correo = data['nuevo_correo']

			#Confirmar formato correo
			patron = '^[\w\.-]+@[\w\.-]+\.\w+$' #palabra@palabra.dominio #se podrían añadir más patrones

			if re.match(patron, nuevo_correo) is None:
				return JsonResponse({"Bad request":"Formato de correo no valido"}, status = 400 )

			# Comprobar que no haya otro usuario con un correo igual
			if Tusuarios.objects.exclude(pk=usuario.id).filter(correo=nuevo_correo).exists():
            			return JsonResponse({'Conflict': 'Este correo ya esta en uso por otro usuario'}, status=401)
			else:
				usuario.correo = data['nuevo_correo'] #sino, se guardará

		# Comprobación de que el nuevo nombre de usuario no esté pillado
		if 'nuevo_nombreusuario' in data:
			nuevo_nombreusuario = data['nuevo_nombreusuario']
			if Tusuarios.objects.exclude(pk=usuario.id).filter(nombreusuario=nuevo_nombreusuario).exists():
                        	return JsonResponse({'Conflict': 'Este nombre de usuario ya esta en uso por otro usuario'}, status=401)
			else:
				usuario.nombreusuario = data['nuevo_nombreusuario']

		# Comprobación largo conraseña y cifrado
		if 'nueva_contrasena' in data:
			nueva_contrasena = data['nueva_contrasena']
			if len(nueva_contrasena) < 5: #largo de la contraseña
				return JsonResponse({"Bad Request":"La contrasena debe tener al menos 5 caracteres"}, status = 400)
			else:
				usuario.contrasena = make_password(data['nueva_contrasena'])

		# Se guarda la nueva info
		usuario.save()
		return JsonResponse({'Created': 'Datos actualizados correctamente'}, status = 201)
	except Tusuarios.DoesNotExist:
		return JsonResponse({'Not found':'Usuario no encontrado'}, status = 404)

# LOG-OUT - FUNCIONA
@csrf_exempt
def logout(request):
	#Comprobamos que el usuario tenga un token
	error_response, payload = verify_token(request)
	if error_response:
		return error_response
	if request.method !='POST':
		return JsonResponse({'error': 'Método no permitido'}, status = 405)
	try:
		usuario = Tusuarios.objects.get(pk=payload['id'])
		usuario.token = None #si el usuario es identificado correctamente, se vacía su token
		usuario.save()

		return JsonResponse({'OK': 'La sesion terminada con exito'}, status = 200)

	except Tusuarios.DoesNotExist:
		return JsonResponse({'Not found': 'Usuario no encontraado'}, status = 404)

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


#--------------------------------------------------------------------------------------------------------------
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
