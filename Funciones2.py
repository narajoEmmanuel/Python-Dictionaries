#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 8/5/2019  8:00am 
#Fecha de última Modificación: 9/5/2019  10:00pm
#Versión: 3.7.2

#importación de librerías
import pickle

#Inicialización de variables globales
diccMcDonalds={}


#Definicion de funciones:
def lee(inventarioMc):
    """
    Entradas: nombre del archivo a leer
    Funcion: Lee un archivo previamente nombrado
    Salidas: No tiene
    """
    dicc={}
    try:
        f=open("inventarioMc","rb")
        print("Voy a leer el archivo: ")
        dicc = pickle.load(f)
        print("Voy a cerrar el archivo:")
        f.close()
    except FileNotFoundError:
        grabar(inventarioMc,diccMcDonalds)
    except:
        print("Error al leer el archivo: ", inventarioMc)
    return dicc

def grabar(inventarioMc,lista):
    """
    Entradas: nombre del archivo a grabar y el diccionario
    Funcion: Graba un archivo
    Salidas: No tiene
    """
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    try:
        f=open(inventarioMc,"wb")
        print("Voy a grabar el archivo: ")
        pickle.dump(lista,f)
        print("Voy a cerrar el archivo:\n ")
        f.close()
        
    except:
        print("Error al grabar el archivo: ",inventarioMc)
    return
#------------------------------------------------------------------------------------------------------

def agregarComida(diccMcDonalds,codigo):#1
    """
    Entradas: Variable Global llamada diccMcDonalds y codigo de la comida
    Funcion: Permite agredar la comida al diccionario
    Salidas: No tiene
    """
    try:     
        nombre=input("Nombre: ")
        precio=int(input("Precio: "))
        ingredientes=[]
        x=" "
        while x!="":
            x=input("Ingrese ingrediente, sino desea ingresar más presione enter: ")
            if x!="":
                ingredientes.append(x)
        datosComida = [nombre,precio,ingredientes]
        diccMcDonalds[codigo] = datosComida
        grabar("inventarioMc",diccMcDonalds)
        print("-------------------")
        print("Los datos han sido ingresados con éxito.")
        return diccMcDonalds
    except ValueError:
        print("El precio debe ser un numero. Intente de nuevo.")
        agregarComida(diccMcDonalds,codigo)
    except:
        print("Ha ocurrido un error inesperado.")
    return   
#------------------------------------------------------------------------------------------------------

def modificarComida(diccMcDonalds):#2
    """
    Entradas: Variable Global llamada diccMcDonalds
    Funcion: Permite modificar la comida dado un codigo
    Salidas: No tiene
    """
    codigoNuevo=input("\nIngrese el código de la comida que quiere modificar: ")
    if codigoNuevo in list(diccMcDonalds.keys()):
        mostrarComida(diccMcDonalds,codigoNuevo)
        print("-------------------")
        print("Datos a modificar:")
        agregarComida(diccMcDonalds,codigoNuevo)
    else:
        print("El codigo ingresado no ha sido encontrado.")
    return       
    
#------------------------------------------------------------------------------------------------------
#Menu secundario

def mostrarTodasComidas(diccMcDonalds):#3.1
    """
    Entradas: Variable Global llamada diccMcDonalds
    Funcion: Permite mostrar todas los datos registrados
    Salidas: No tiene
    """
    try:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Datos Registrados:\n")
        codigos=list(diccMcDonalds.keys())
        for llave in codigos:
            mostrarComida(diccMcDonalds,llave)
            print("-------------------")
    except:
        print("Ha ocurrido un error inesperado.")
    return

def mostrarComida(diccMcDonalds,codigo):#3.2
    """
    Entradas: Variable Global llamada diccMcDonalds
    Funcion: Permite mostrar la comida dado un codigo
    Salidas: El codigo, el precio, la comida y los ingredientes
    """
    print("------------------------------")
    try:
        infoComida=diccMcDonalds[codigo]
        print("Código:",codigo)
        print("Comida:",infoComida[0])
        print ("Precio:",infoComida[1])
        print("Ingredientes: ",tuple(infoComida[2]))
    except KeyError:
        print("El codigo ingresado no ha sido encontrado.")
    except:
        print("Ha ocurrido un error inesperado.")
    return
#------------------------------------------------------------------------------------------------------

def eliminarComida(diccMcDonalds,codigo):#4
    """
    Entradas: Variable Global llamada diccMcDonalds y el codigo de la comida a eliminar
    Funcion: Permite eliminar la comida registrada dado su codigo
    Salidas: Indica los datos de la comida eliminada.
    """
    if codigo in list(diccMcDonalds.keys()):
        print("------------------------------")
        print("Se va a eliminar los siguientes datos:")
        mostrarComida(diccMcDonalds,codigo)
        del(diccMcDonalds[codigo])
        grabar("inventarioMc",diccMcDonalds)
        print("Los datos fueron eliminados con éxito.")
    else:
        print("El codigo ingresado no ha sido encontrado.")
    return  


    








