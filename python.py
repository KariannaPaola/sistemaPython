from funciones import leer_lista_usuarios
from funciones import crear_lista_usuarios
from funciones import enviar_mensaje
from funciones import crear_nombre
from funciones import crear_apellido
from funciones import crear_cedula
from funciones import crear_correo
from funciones import crear_numeroTelefono
from funciones import buscar_usuario
from funciones import actualizar_usuario
from funciones import borrar_usuario

nombre_archivo="usuarios.txt"
usuarios = leer_lista_usuarios(nombre_archivo)

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
      nombre_archivo="usuarios.txt"
      usuarios.append(usuario)
      crear_lista_usuarios(nombre_archivo,usuarios)
      print("Usuario agregado correctamente.")
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

