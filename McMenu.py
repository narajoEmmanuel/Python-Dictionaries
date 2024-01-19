#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 8/5/2019  8:00am 
#Fecha de última Modificación: 9/5/2019  10:00pm
#Versión: 3.7.2

#importacion de librerias
from Funciones2 import*

#Definicion de funciones:
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Diccionario Mc Donald's")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def menu():
      try:
            while True:
                  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                  print("1-Agregar Comida")
                  print("2-Modificar Comida")
                  print("3-Buscar Comida")
                  print("4-Eliminar Comida")
                  print("5-Terminar")
                  opcion=int(input("Escoja una opción: "))
                  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                  if opcion==1:
                        codigo=input("Código: ")
                        agregarComida(diccMcDonalds,codigo)
                  elif opcion==2:
                        modificarComida(diccMcDonalds)
                  elif opcion==3:
                        menuSecundario()
                  elif opcion==4:
                        codigo=input("Indique el codigo de la comida a eliminar:")
                        eliminarComida(diccMcDonalds,codigo)
                  elif opcion==5:
                        grabar("inventarioMc",diccMcDonalds)
                        break
      except ValueError:
            menu()
                                                           
def menuSecundario():
      print("------------------------------")
      print("1.Mostrar todos las comidas registradas")
      print("2.Buscar por código")
      print("------------------------------")
      try:
            opcionMenuSec=int(input("Escoja una opción: "))
            if opcionMenuSec==1:
                  mostrarTodasComidas(diccMcDonalds)
            elif opcionMenuSec==2:
                  codigo=input("Indique el codigo de la comida a mostrar:")
                  mostrarComida(diccMcDonalds,codigo)
            else:
                  menuSecundario()
      except ValueError:
            menuSecundario()


#Programa Principal
diccMcDonalds=lee("inventarioMc")
menu()
