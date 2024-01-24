from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import Tusuarios
from django.contrib.auth.hashers import make_password, check_password
import json
import jwt
import datetime
import re

@csrf_exempt
# REGISTER - FUNCIONA
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
#def inicio_sesion(request):
#        if request.method!='POST':
#                return None

#	token_csrf = get_token(request) # ?????

#        json_peticion = json.loads(request.body)
#        correo = json_peticion['ingresar_correo']
#        contrasena =json_peticion['ingresar_contrasena']

        #comprobación campos no vacíos
#        if correo == '' or contrasena == '':
#                return JsonResponse({"Bad Request":"Faltan parametros"}, status = 400)

        #comprobación correo está registrado
#        try:
#                usuario = Tusuarios.objects.get(correo=correo)
#        except Tusuarios.DoesNotExist:
#                return JsonResponse({"Not Found":"El correo proporcionado no esta registrado"}, status = 404) #comentar con rubén

        #comprobación la contraseña es correcta
#        if not check_password(contrasena, usuario.contrasena):
#                return JsonResponse({'Bad request':'La contrasena no es valida'}, status = 401)

        #generar token (inicio de sesión????)
#        def generar_jwt_token():
#                payload = {
#                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1), # Token expira en 1 día
#                        'iat': datetime.datetime.utcnow(),
#                }
#                token = jwt.encode(payload, 'gatitosfelices123', algorithm='HS256')

#                return token
#        return JsonResponse({"OK":"Sesion iniciada con exito"}, status = 200 ) #dejar así?
