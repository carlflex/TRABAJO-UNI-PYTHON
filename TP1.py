import getpass
import os
from colorama import init
init()
#Integrantes:
#Gugliermino Carlos
#Teo Valentin Garcia Queipo
#Franco Zariaga

#Variables globales
strike=3

count_indumentaria=0
count_perfumeria=0
count_comida=0
rubro_menor=""
rubro_mayor=""
mayor=0
menor=0
limite=50
tipo_user=""
cod_local=1
local_index=0

ar_base=[
    ["admin@shopping.com","12345","administrador"],
    ["localA@shopping.com","AAAA1111","dueñoLocal"],
    ["localB@shopping.com","BBBB2222","dueñoLocal"],
    ["unCliente@shopping.com","33xx33","cliente"]
]

ar_codigos=[1,4,6,9]

""" ar_locales=[
    [], #Nombre
    [], #Ubicacion
    [], #Rubro
    []  #Estado
] """

ar_locales=[["" for j in range(4)] for i in range(51)]
ar_locales_cod=[[0 for j in range(2)]for i in range(51)]
print(ar_locales_cod)

#funciones de utilidad
def ar_index(array,elemento,largo):
    ind=-1
    for i in range(largo):
        if array[i]== elemento:
            inD=i
    return ind

def ar_orden(array,largo,nivel="normal"):

    for i in range(1,largo):
        for j in range(largo-i):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

def ar_existe(array,largo,elemento):
    ind=0

    while (ind<largo) and (array[ind]!=elemento):
        ind+=1

    if array[ind]==elemento:
        return True
    else:
        return False
    


def limpiar_pantalla():
    os.system("cls")

#---------------------------
# Funciones de validacion
def valid_codigo_usuario():
    ind=0
    valid= True
    cod=int(input("Ingrese el codigo: "))

    while valid: 
        while  (ind <= 2) and (ar_codigos[ind]!=cod) :
            ind+=1

        if ar_codigos[ind]==cod:
            if ar_base[ind][2]=="dueñoLocal":
                valid=False
            else:
                print("Usted no es dueño \n")
                cod=int(input("Ingrese el codigo: "))
        else:
            print("codigo incorrecto  \n")
            cod=int(input("Ingrese el codigo: "))
    
    return cod     

def val_datos_local(data):
    global ar_locales_cod,local_index
    ind=0
    while  (ind < 49) and data !=ar_locales_cod[ind][1]:
        ind+=1
    
    if ar_locales_cod[ind][1]==data:
      local_index=ind
      return True
    else:
        return False


def val_opciones(ar,largo,error,mensaje):

    opt=input(mensaje)

    while not ar_existe(ar,largo,opt):
        print(error)
        opt=input(mensaje)
    
    return opt

        
#----------------

#Funcion de construccion
def coming_soon():
    print("\n---------------------")
    print("EN CONSTRUCCION")
    print("---------------------\n")
    input()
    limpiar_pantalla()

def operar_contadores(rubro,tipo):
    global count_comida,count_indumentaria,count_perfumeria

    match tipo:
        case "aumentar":
            match rubro:
                case "indumentaria":
                    count_indumentaria+=1
                case "comida":
                    count_comida+=1
                case "perfumeria":
                    count_perfumeria+=1
        case "restar":
            match rubro:
                case "indumentaria":
                    count_indumentaria-=1
                case "comida":
                    count_comida-=1
                case "perfumeria":
                    count_perfumeria-=1
            
            

#Funcion del menu de locales   
def DecisionMayor_Menor():
    global count_perfumeria,count_indumentaria,count_comida,mayor,menor

    ar_contadores=[count_indumentaria,count_comida,count_perfumeria]
    ar_nombres=["indumentaria","comida","perfumeria"]

    ar_copia_orden=ar_contadores.copy()
    ar_copia_orden=ar_orden(ar_copia_orden,3)

    rubro_mayor=ar_nombres[ar_index(ar_contadores,ar_copia_orden[2],3)]
    rubro_menor=ar_nombres[ar_index(ar_contadores,ar_copia_orden[0],3)]
    mayor=ar_copia_orden[2]
    menor=ar_copia_orden[0]

    return [rubro_menor,rubro_mayor]
def CreacionLocal():
    global count_perfumeria,count_indumentaria,count_comida,limite,cod_local,mayor,menor
   
    nombreLocal= input("Ingrese el nombre: ")

    while nombreLocal !="*":
        ubicacionLocal=input("Ingrese la ubicacion: ")
        rubroLocal=val_opciones(["indumentaria","comida","perfumeria"],2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")

        """ while(rubroLocal!="indumentaria") and (rubroLocal!="comida") and (rubroLocal!="perfumeria"):
            print("El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida")
            rubroLocal=input("Ingrese el rubro: ")
 """
        cod_user=valid_codigo_usuario()
        
        operar_contadores(rubroLocal,"aumentar")

        datos=DecisionMayor_Menor()
                    
        print("---------------------------")
        print(f"Se a creado con exito el local {nombreLocal} en la ubicacion {ubicacionLocal}")
        print("---------------------------")

        ar_locales[cod_local-1][0]=nombreLocal
        ar_locales[cod_local-1][1]=ubicacionLocal
        ar_locales[cod_local-1][2]=rubroLocal
        ar_locales[cod_local-1][3]='A'

        ar_locales_cod[cod_local-1][0]=cod_user
        ar_locales_cod[cod_local-1][1]=cod_local
        cod_local+=1
        if (count_indumentaria != count_comida) or (count_indumentaria != count_perfumeria) or (count_comida != count_perfumeria):
            print("Rubro con mas locales")
            print(f"El rubro de {datos[1]}, con un total de: {mayor} locales") 
            print("---------------------------")
            print("Rubro con menos locales")
            print(f"El rubro de {datos[0]}, con un total de: {menor} locales") 
            print("---------------------------\n")
        else:
            print(f"Los rubros tienen la misma cantidad de locales, con {count_indumentaria}")
        input()
        limpiar_pantalla()
        print(ar_locales)
        nombreLocal= input("Ingrese el nombre: ")   

    limpiar_pantalla()
    limite-=1
    print(f"Espacio disponible: {limite} ") 

def mod_local():
    global ar_locales,ar_locales_cod

    input_cod_local=int(input("Ingrese el codigo del local que desea modificar: \n"))

    while val_datos_local(input_cod_local):
        print("Codigo no existe\n")
        input_cod_local=int(input("Ingrese el codigo del local que desea modificar: \n"))

    print("----------------------------------------------------------------------------------------------\n")
    print(f"""Modificacion de datos del local:{input_cod_local}
          alias:{ar_locales[local_index][0]}\n""")
    print("---------------------------------------------------------------------------------------------------")
    
    nombreLocal= input("Ingrese el nombre: ")
    ubicacionLocal=input("Ingrese la ubicacion: ")
    rubroLocal=val_opciones(["indumentaria","comida","perfumeria"],2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")
    cod_user=valid_codigo_usuario()

    operar_contadores(ar_locales[local_index][2],"restar")
    operar_contadores(rubroLocal,"aumentar")
    ar_locales[local_index][0]=nombreLocal
    ar_locales[local_index][1]=ubicacionLocal
    ar_locales[local_index][2]=rubroLocal
    ar_locales_cod[local_index][0]=cod_user

def eliminar_local():
    global ar_locales

    input_cod_local=int(input("Ingrese el codigo del local que desea modificar: \n"))

    while val_datos_local(input_cod_local):
        print("Codigo no existe\n")
        input_cod_local=int(input("Ingrese el codigo del local que desea modificar: \n"))

    print("===============================")
    print("¿Desea dar de baja este local?")
    print("===============================")

    opcion=input("SI(s)/NO(N)")

    if opcion =="s":
        ar_locales[local_index][3]="B"


def limite_local():
    global limite

    if limite != 0:
        CreacionLocal()
    else:
        print("--------------------------------")
        print("No hay espacio para mas locales")
        print("--------------------------------")

def mapa_local():
    global ar_locales
    limpiar_pantalla()

    c1=0
    for i in range(10):
        print("+-"*5+"+")
        print(f"|{ar_locales_cod[c1][0]}|{ar_locales_cod[c1+1][0]}|{ar_locales_cod[c1+2][0]}|{ar_locales_cod[c1+3][0]}|{ar_locales_cod[c1+4][0]}|")
        c1+=5
    print("+-"*5+"+")


mapa_local()
#----------------------------------------------        
def menu_local(): 
    fin=True
    while fin:
        print("---------------------------")
        print("GESTION DE LOCALES")
        print("---------------------------\n")

        print("a) Crear locales")
        print("b) Modificar local")
        print("c) Eliminar locales")
        print("d) Mapa de locales")
        print("e) Volver")

        accion= val_opciones(["a","b","c","d","e"],4,"Opcion no valida \n","\nIngrese una opcion: ")
        """ while ((accion!="a") and (accion!="b") and (accion!="c") and (accion!="d") and (accion!="e")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ") """

        match accion:
            case "a":
                limpiar_pantalla()
                limite_local()
            case "b":
                coming_soon()
                
            case "c":
                coming_soon()
            case "d":
                mapa_local()
            case "e":
                fin=False

#Funcion del menu de novedades
def menu_novedades():

    fin=True
    
    while fin:
        print("\n---------------------------")
        print("GESTION DE NOVEDADES")
        print("---------------------------")

        print("a) Crear novedades")
        print("b) Modificar novedad")
        print("c) Eliminar novedad")
        print("d) Ver reporte de novedades")
        print("e) Volver")

        accion= input("Ingrese una opcion: ")
        while ((accion!="a") and (accion!="b") and (accion!="c") and (accion!="d") and (accion!="e")):
            print("Opcion no valida")
            accion=input("Ingrese una opcion: ")

        match accion:
            case "a":
                coming_soon()
                
            case "b":
                coming_soon()
                
            case "c":
                coming_soon()
                
            case "d":
                coming_soon()
                
            case "e":
                fin=False

#Funcion del menu principal
def menuAdmin():
   fin=True
   while fin:
        print("\n---------------------")
        print("1. Gestion de locales")
        print("2. Crear cuentas de dueños locales")
        print("3. Aprobar / Denegar solicitud de descuento")
        print("4. Gestion de Novedades")
        print("5. Reporte de utilización de descuentos")
        print("0. Salir")
        print("---------------------\n")
        
        accion= input("Ingrese una opcion: ")
        while ((accion!="1") and (accion!="2") and (accion!="3") and (accion!="4") and (accion!="5") and (accion!="0")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ")

        match accion:
            case "1":
                limpiar_pantalla()
                menu_local()
            case "2":
                limpiar_pantalla()
                coming_soon()
            case "3":
                limpiar_pantalla()
                coming_soon()
            case "4":
                menu_novedades()
            case "5":
                coming_soon()
            case "0":
                fin=False
                print("SALIENDO DEL PROGRAMA")

def menuDueño():
   fin=True
   while fin:
        print("\n---------------------")
        print("1. Gestión de Descuentos")
        print("   a) Crear descuento para mi local")
        print("   b) Modificar descuento de mi local")
        print("   c) Eliminar descuento de mi local")
        print("   d) Volver")
        print("2. Aceptar / Rechazar pedido de descuento")
        print("3. Reporte de uso de descuentos")
        print("0. Salir")
        print("---------------------\n")
        
        accion= input("Ingrese una opcion: ")
        while ((accion!="1") and (accion!="2") and (accion!="3") and (accion!="0")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ")

        match accion:
            case "1":
                GestionDesc()
            case "2":
                limpiar_pantalla()
                coming_soon()
            case "3":
                limpiar_pantalla()
                coming_soon()
            case "0":
                fin=False
                print("SALIENDO DEL PROGRAMA")

def GestionDesc():
    fin=True
    while fin:
        accion=val_opciones(["a","b","c","d"],3,"Opcion no valida \n","\nIngrese una opcion: ")
        """ while ((accion!="a") and (accion!="b") and (accion!="c") and (accion!="d")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ")
 """
        match accion:
            case "a":
                coming_soon()
            case "b":
                coming_soon()
            case "c":
                coming_soon()
            case "d":
                limpiar_pantalla()
                fin=False

def menuCliente():
   fin=True
   while fin:
        print("\n---------------------")
        print("1. Registrarme")
        print("2. Buscar descuentos en locales")
        print("3. Solicitar descuento")
        print("4. Ver novedades")
        print("0. Salir")
        print("---------------------\n")
        
        accion= input("Ingrese una opcion: ")
        while ((accion!="1") and (accion!="2") and (accion!="3") and (accion!="4") and (accion!="0")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ")

        match accion:
            case "1":
                limpiar_pantalla()
                coming_soon()
            case "2":
                limpiar_pantalla()
                coming_soon()
            case "3":
                limpiar_pantalla()
                coming_soon()
            case "4":
                limpiar_pantalla()
                coming_soon()
            case "0":
                fin=False
                print("SALIENDO DEL PROGRAMA")
                
#Funcion de inicio del programa
def failLogin():
    global nombreUsuario,claveUsuario,tipo_user
    valid=False
    
    for i in range(4):
        
        if nombreUsuario==ar_base[i][0] and claveUsuario== ar_base[i][1]:
            tipo_user=ar_base[i][2]
            valid=True
    
    return valid

#Programa Principal
nombreUsuario=input("Ingrese el usuario: ")
claveUsuario=getpass.getpass("Ingrese la clave: ")
print("-----------------------------------------\n")

while(strike!=0):
    check=failLogin()
    if check:
        print("Ingreso exitoso")
        print("-----------------------------------------\n")
        strike=0   
        match tipo_user:
            case "administrador":
                menuAdmin()
            case "dueñoLocal":
                menuDueño()
            case "cliente":
                menuCliente()
    else:
        strike-=1
        print("Usuario o contraseña incorrecto")
        print("-----------------------------------------\n")
        print(strike)
        nombreUsuario=input("Ingrese el usuario: ")
        claveUsuario=getpass.getpass("Ingrese la clave: ")   