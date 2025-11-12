import re
import pywhatkit
from datetime import datetime, timedelta
import json

def leer_lista_usuarios(archivo): 
    usuarios = []
    try:
      with open(archivo, "r", encoding="utf-8") as file:
        for i, linea in enumerate(file):
          usuario_texto=linea
          diccionario=json.loads(usuario_texto)
          usuarios.append(diccionario)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
    except UnboundLocalError:
        print(f"no hay un usuario todavia")
    return usuarios

def crear_lista_usuarios(archivo, usuarios_creados):
    try:
      with open(archivo, "w", encoding="utf-8") as file:
        for usuario in usuarios_creados:
          lineajson=json.dumps(usuario)
          file.write(lineajson + "\n") 
        print("Ejecución finalizada con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

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
  entrada_nombre=input("Ingresa un nombre: ").lower()
  nombre_valido= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_nombre)
  if not nombre_valido:
    print("Ingrese un nombre valido")
    return crear_nombre()
  else:
    return entrada_nombre

def crear_apellido():
  entrada_apellido=input("Ingresa un apellido: ").lower()
  apellido_valido= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_apellido)
  if not apellido_valido:
    print("Ingrese un apellido valido")
    return crear_apellido()
  else: 
    return entrada_apellido

def crear_cedula():
  entrada_cedula=input("Ingresa el numero de cedula en este formato 26133452, sin puntos, ni espacios:" \
  " ")
  cedula_valida= re.search(r'^\d{6,8}$', entrada_cedula)
  if not cedula_valida:
    print("Ingrese una cedula valida")
    return crear_cedula()
  else: 
    return entrada_cedula

def crear_correo():
  entrada_correo=input("Ingresa el correo: ").lower()
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
  entrada_clave_buscardor=input("Deseas buscar por nombre, apellido, cedula, correo o telefono?: ").lower()
  if entrada_clave_buscardor=="nombre":
    entrada_buscador=input("Ingresa el nombre del usuario que buscas ").lower()
    nombre_archivo="usuarios.txt"
    usuarios= leer_lista_usuarios(nombre_archivo)
    for usuario in usuarios:
      if entrada_buscador in usuario.values():
        encontrado= True
        print(f"si hay: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")     
    if not encontrado:
        print("no hay coincidencias")
  elif entrada_clave_buscardor=="apellido":
    entrada_buscador=input("Ingresa el apellido del usuario que buscas ").lower()
    nombre_archivo="usuarios.txt"
    usuarios= leer_lista_usuarios(nombre_archivo)
    for usuario in usuarios:
      if entrada_buscador in usuario.values():
        encontrado= True
        print(f"si hay: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")     
    if not encontrado:
        print("no hay coincidencias")
  elif entrada_clave_buscardor=="cedula":
    entrada_buscador=input("Ingresa la cedula del usuario que buscas, debe ser en este formaro sin espacios ni puntos 26133452 ")
    cedula_valida= re.search(r'^\d{6,8}$', entrada_buscador)
    if not cedula_valida:
      print("Ingrese una cedula valida")
      return buscar_usuario()
    else:
      nombre_archivo="usuarios.txt"
      usuarios= leer_lista_usuarios(nombre_archivo)
      for usuario in usuarios:
        if entrada_buscador in usuario.values():
          encontrado= True
          print(f"si hay: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")     
      if not encontrado:
          print("no hay coincidencias")
  elif entrada_clave_buscardor=="correo":
    entrada_buscador=input("Ingresa el correo del usuario que buscas ").lower()
    correo_valido= re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', entrada_buscador)
    if not correo_valido:
      print("Ingrese un correo válido")
      return buscar_usuario()
    else:
      nombre_archivo="usuarios.txt"
      usuarios= leer_lista_usuarios(nombre_archivo)
      for usuario in usuarios:
        if entrada_buscador in usuario.values():
          encontrado= True
          print(f"si hay: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")     
      if not encontrado:
          print("no hay coincidencias")
  elif entrada_clave_buscardor=="telefono":
    entrada_buscador=input("Ingresa el telefono del usuario que buscas en este formato +584143417985 ").lower()
    telefono_valido= re.search(r'^\+58[246789]\d{9}$', entrada_buscador)
    if not telefono_valido:
      print("Ingrese un correo válido")
      return buscar_usuario()
    else:
      nombre_archivo="usuarios.txt"
      usuarios= leer_lista_usuarios(nombre_archivo)
      for usuario in usuarios:
        if entrada_buscador in usuario.values():
          encontrado= True
          print(f"si hay: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']} ")     
      if not encontrado:
          print("no hay coincidencias")
  else:        
    print("Debes ingresar alguna de las siguientes palabras nombre, apellido, cedula, correo o telefono?: ")
    return buscar_usuario()
  
def entrada_modificar_valor():
  print("¿que deseas modificar? ejemplo: nombre, apellido, cedula, correo o telefono")
  entrada_modificar_por_clave = input("Escribe aqui: ").lower()
  return entrada_modificar_por_clave

def actualizar_usuario():
  nombre_archivo="usuarios.txt"
  usuarios= leer_lista_usuarios(nombre_archivo)
  contador=0
  for usuario in usuarios: 
    print(f" usuario numero {contador}: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']}")
    contador= contador+1
  try: 
    print("Ingresa el numero de usuario que quieres modificar")
    entrada_modificar = int(input("Escribe el numero: "))
    print(f"Escogiste este usuario: {usuarios[entrada_modificar]}")
    clave_ingresada=entrada_modificar_valor() 
    if clave_ingresada == "nombre":
      entrada_nuevo_nombre = input("Escribe el nuevo nombre aqui: ").lower()
      nombre_valido_editado= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_nuevo_nombre)
      if not nombre_valido_editado:
        print("debe ingresar un nombre valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["nombre"]= entrada_nuevo_nombre
        crear_lista_usuarios(nombre_archivo, usuarios)
        print("nombre actualizado")
    elif clave_ingresada == "apellido":
      entrada_nuevo_apellido = input("Escribe el nuevo apellido aqui: ").lower()
      apellido_valido_editado= re.search(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', entrada_nuevo_apellido)
      if not apellido_valido_editado:
        print("debe ingresar un apellido valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["apellido"]= entrada_nuevo_apellido
        crear_lista_usuarios(nombre_archivo, usuarios)
        print("nombre actualizado")  
    elif clave_ingresada == "cedula":
      entrada_nueva_cedula = input("Escribe la nueva cedula aqui: ")
      cedula_valida_editada= re.search(r'^[VvEe]?-?(\d{1,3}(\.|\s)?){1,3}\d{3,4}$', entrada_nueva_cedula)
      if not cedula_valida_editada:
        print("debe ingresar un numero de cedula valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["cedula"]= entrada_nueva_cedula
        crear_lista_usuarios(nombre_archivo, usuarios)
        print("cedula actualizada")
    elif clave_ingresada == "correo":
      entrada_nuevo_correo = input("Escribe el nuevo correo aqui: ").lower()
      correo_valido_editado= re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', entrada_nuevo_correo)
      if not correo_valido_editado:
        print("debe ingresar un correo valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["correo"]= entrada_nuevo_correo
        crear_lista_usuarios(nombre_archivo, usuarios)
        print("correo actualizado")
    elif clave_ingresada == "telefono":
      entrada_nuevo_telefono = input("Escribe el nuevo telefono aqui en formato internacional ej: +584143417985: ")
      telefono_valido_editado= re.search(r'^\+58[246789]\d{9}$', entrada_nuevo_telefono)
      if not telefono_valido_editado:
        print("debe ingresar un numero de telefono valido")
        actualizar_usuario()
      else:
        usuarios[entrada_modificar]["telefono"]= entrada_nuevo_telefono
        crear_lista_usuarios(nombre_archivo, usuarios)
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
  nombre_archivo="usuarios.txt"
  usuarios= leer_lista_usuarios(nombre_archivo)
  contador=0
  for usuario in usuarios: 
    print(f" usuario numero {contador}: {usuario['nombre']}, {usuario['apellido']}, {usuario['cedula']}, {usuario['correo']}, {usuario['telefono']}")
    contador= contador+1
  try:
    print("Ingresa el numero de usuario que quieres borrar")
    entrada_borrar = int(input("Escribe el numero: "))
    print(f"Escogiste este usuario: {usuarios[entrada_borrar]}")
    usuarios.pop(entrada_borrar)
    crear_lista_usuarios(nombre_archivo, usuarios)
    print("usuario eliminado")
  except IndexError:
    print("No hay un usuario con ese numero asignado")
  except ValueError:
    print("Ingrese un numero valido")
    borrar_usuario() 


        
