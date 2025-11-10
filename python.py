import re
import pywhatkit
from datetime import datetime, timedelta

usuarios = []

def enviar_mensaje(numero_de_telefono, nombre):
  ahora = datetime.now()
  envio= ahora + timedelta(minutes=2)
  hora= envio.hour
  minutos= envio.minute
  
  try:
    pywhatkit.sendwhatmsg(
      phone_no=numero_de_telefono,
      message=f"¡Hola {nombre} ! Bienvenido a nuestro sistema de Python.",
      time_hour=hora,
      time_min=minutos,
      wait_time=40,  
      tab_close=True,
      close_time=5
      )
  except:
    print("no se pudo enviar mensaje")
  
    

def crear_nombre():
  entrada_nombre=input("Ingresa un nombre: ")
  nombre_valido= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_nombre)
  if not nombre_valido:
    print("Ingrese un nombre valido")
    return crear_nombre()
  else:
    return entrada_nombre
  

def crear_apellido():
  entrada_apellido=input("Ingresa un apellido: ")
  apellido_valido= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_apellido)
  if not apellido_valido:
    print("Ingrese un apellido valido")
    return crear_apellido()
  else: 
    return entrada_apellido

def crear_cedula():
  entrada_cedula=input("Ingresa el numero de cedula: ")
  cedula_valida= re.search(r'^[VvEe]?-?(\d{1,3}(\.|\s)?){1,3}\d{3,4}$', entrada_cedula)
  if not cedula_valida:
    print("Ingrese una cedula valida")
    return crear_cedula()
  else: 
    return entrada_cedula

def crear_correo():
  entrada_correo=input("Ingresa el correo: ")
  correo_valido= re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', entrada_correo)
  if not correo_valido:
    print("Ingrese un correo valido")
    return crear_correo()
  else:
    return entrada_correo

def crear_numeroTelefono():
  entrada_numeroTelefono=input("Ingresa el número de teléfono en formato internacional ej: +584143417985 ")
  numero_valido= re.search(r'^\+58[246789]\d{9}$', entrada_numeroTelefono)
  if not numero_valido:
    print("Ingrese un numero valido")
    return crear_numeroTelefono()
  else:
    return entrada_numeroTelefono
    
  
def buscar_usuario():
  encontrado=False
  entrada_buscador=input("Ingresa un nombre, apellido, cedula, correo o telefono: ")
  for usuario in usuarios:
    if entrada_buscador in usuario.values():
      encontrado= True
      print(f"si hay: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")     
  if not encontrado:
      print("no hay coincidencias")

def entrada_modificar_valor():
  print("¿que deseas modificar? ejemplo: nombre, apellido, cedula, correo o telefono")
  entrada_modificar_por_clave = input("Escribe aqui: ")
  return entrada_modificar_por_clave

def actualizar_usuario():
  contador=0
  for usuario in usuarios: 
    print(f" usuario numero {contador}: {usuario}")
    contador= contador+1
  try: 
    print("Ingresa el numero de usuario que quieres modificar")
    entrada_modificar = int(input("Escribe el numero: "))
    print(f"Escogiste este usuario: {usuarios[entrada_modificar]}")
    clave_ingresada=entrada_modificar_valor() 
    if clave_ingresada == "nombre":
      entrada_nuevo_nombre = input("Escribe el nuevo nombre aqui: ")
      nombre_valido_editado= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_nuevo_nombre)
      if not nombre_valido_editado:
        print("debe ingresar un nombre valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["nombre"]= entrada_nuevo_nombre
        print("nombre actualizado")
    elif clave_ingresada == "apellido":
      entrada_nuevo_apellido = input("Escribe el nuevo apellido aqui: ")
      apellido_valido_editado= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_nuevo_apellido)
      if not apellido_valido_editado:
        print("debe ingresar un apellido valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["apellido"]= entrada_nuevo_apellido
        print("apellido actualizado")  
    elif clave_ingresada == "cedula":
      entrada_nueva_cedula = input("Escribe la nueva cedula aqui: ")
      cedula_valida_editada= re.search(r'^[VvEe]?-?(\d{1,3}(\.|\s)?){1,3}\d{3,4}$', entrada_nueva_cedula)
      if not cedula_valida_editada:
        print("debe ingresar un numero de cedula valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["cedula"]= entrada_nueva_cedula
        print("cedula actualizada")
    elif clave_ingresada == "correo":
      entrada_nuevo_correo = input("Escribe el nuevo correo aqui: ")
      correo_valido_editado= re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', entrada_nuevo_correo)
      if not correo_valido_editado:
        print("debe ingresar un correo valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["correo"]= entrada_nuevo_correo
        print("correo actualizado")
    elif clave_ingresada == "telefono":
      entrada_nuevo_telefono = input("Escribe el nuevo telefono aqui en formato internacional ej: +584143417985: ")
      telefono_valido_editado= re.search(r'^\+58[246789]\d{9}$', entrada_nuevo_telefono)
      if not telefono_valido_editado:
        print("debe ingresar un numero de telefono valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["telefono"]= entrada_nuevo_telefono
        print("telefono actualizado")
    else:
      print("Debe ingresar alguna de las siguientes palabras validas: nombre, apellido, cedula, correo, o telefono") 
      actualizar_usuario() 
  except IndexError:
    print("No hay un usuario con ese numero asignado")
    actualizar_usuario()
  except ValueError:
    print("Ingrese un numero valido")
    actualizar_usuario() 

def borrar_usuario():
  contador=0
  for usuario in usuarios: 
    print(f" usuario numero {contador}: {usuario}")
    contador= contador+1
  try:
    print("Ingresa el numero de usuario que quieres borrar")
    entrada_borrar = int(input("Escribe el numero: "))
    print(f"Escogiste este usuario: {usuarios[entrada_borrar]}")
    usuarios.pop(entrada_borrar)
    print("usuario eliminado")
  except IndexError:
    print("No hay un usuario con ese numero asignado")
  except ValueError:
    print("Ingrese un numero valido")
    borrar_usuario() 
        

while True:
  print("Escoge un número de acuerdo a la opción que desees")
  print("Escribe 1 para crear usuario, 2 para buscar en la lista de usuarios, 3 para actualizar un usuario y 4 para borrar un usuario")
  try:
    entrada = int(input("Escribe un numero: "))
    if entrada == 1:
      nombre= crear_nombre()
      apellido= crear_apellido()
      cedula= crear_cedula()
      correo= crear_correo()
      telefono= crear_numeroTelefono()
      usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula,
        "correo": correo,
        "telefono": telefono
      }
      usuarios.append(usuario)
      print(f"usuarios: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")
      print(f"usuarios: {usuarios} ")
      ultimo_usuario=len(usuarios)-1
      enviar_mensaje(usuarios[ultimo_usuario]['telefono'], usuarios[ultimo_usuario]['nombre'])
    elif entrada == 2:
      buscar_usuario()  
    elif entrada == 3: 
      actualizar_usuario()  
    elif entrada == 4:
      borrar_usuario()
    else:
      print("debe ingresar un numero del 1 al 4")
  except ValueError:
    print("Ingrese un numero valido")
