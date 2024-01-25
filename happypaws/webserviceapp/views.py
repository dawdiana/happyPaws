from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import Tusuarios
from django.contrib.auth.hashers import make_password, check_password
import json
import jwt
import datetime
import re

#REGISTER - FUNCIONA
@csrf_exempt
def formulario_registro(request):
	if request.method!='POST':
		return None

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
		return JsonResponse({"OK":"Usuario registrado"}, status = 200)
	except Exception as e:
		print(str(e))
		return JsonResponse({"Error":f"Error de registro de usuario: {str(e)}"}, status=500)

#LOG-IN
@csrf_exempt
def inicio_sesion(request):
	if request.method!='POST':
		return None

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
	def generar_jwt_token():
		payload = {
			'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1), # Token expira >
			'iat': datetime.datetime.utcnow(),
		}
		token = jwt.encode(payload, 'gatitosfelices123', algorithm='HS256')
		return token

	#Comprobación la contraseña es correcta
	if check_password(contrasena, usuario.contrasena): #si la contraseña es correcta, se genera el token, pero solo es correcta si la contraseña de la tabla está hasheada
		return JsonResponse({"OK":"Sesion iniciada con exito", "token": generar_jwt_token()}, status = 200)
	else:
		return JsonResponse({'Unauthorized':'La contrasena no es valida'}, status = 401)
