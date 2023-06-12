import getpass
import os
#Integrantes:
#Gugliermino Carlos
#Teo Valentin Garcia Queipo
#Franco Zariaga
#Lucas Colalongo

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

cod_local=1
local_indice=0

ar_base=[
    [0,"admin@shopping.com","12345","administrador"],
    [1,"localA@shopping.com","AAAA1111","dueñoLocal"],
    [2,"localB@shopping.com","BBBB2222","dueñoLocal"],
    [3,"unCliente@shopping.com","33xx33","cliente"]
]

ar_locales=[
    [],
    [],
    [],
    []
]

for i in range(51):
    ar_locales[0].append("")
    ar_locales[3].append(0)

#funciones de utilidad
def ar_index(array,elemento,largo):
    for i in range(largo):
        if array[i]== elemento:
            return i
    return None

def ar_orden(array,largo,nivel="normal"):

    for i in range(1,largo):
        for j in range(largo-i):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

def limpiar_pantalla():
    os.system("cls")
#---------------------------
#Funcion de construccion
def coming_soon():
    print("\n---------------------")
    print("EN CONSTRUCCION")
    print("---------------------\n")
    input()
    limpiar_pantalla()


def DecisionMayor_Menor():
    global count_perfumeria,count_indumentaria,count_comida

    ar_contadores=[count_indumentaria,count_comida,count_perfumeria]
    ar_nombres=["indumentaria","comida","perfumeria"]

    ar_copia_orden=ar_contadores.copy()
    ar_copia_orden=ar_orden(ar_copia_orden,3)

    rubro_mayor=ar_nombres[ar_index(ar_contadores,ar_copia_orden[-1],3)]
    rubro_menor=ar_nombres[ar_index(ar_contadores,ar_copia_orden[0],3)]
    mayor=ar_copia_orden[-1]
    menor=ar_copia_orden[0]

    return [[rubro_menor,rubro_mayor],[menor,mayor]]
def CreacionLocal():

    global count_perfumeria,count_indumentaria,count_comida,limite,cod_local,local_indice
    
    nombreLocal= input("Ingrese el nombre: ")
    ubicacionLocal=input("Ingrese la ubicacion: ")
    rubroLocal=input("Ingrese el rubro: ")
    print("-----------------------------------\n")

    while(rubroLocal!="indumentaria") and (rubroLocal!="comida") and (rubroLocal!="perfumeria"):
        print("El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida")
        rubroLocal=input("Ingrese el rubro: ")

    ar_locales[0][local_indice]=nombreLocal
    ar_locales[1].append(ubicacionLocal)
    ar_locales[3][local_indice]=cod_local
    cod_local+=1

    match rubroLocal:
        case "indumentaria":
            count_indumentaria+=1
        case "comida":
            count_comida+=1
        case "perfumeria":
            count_perfumeria+=1

    datos=DecisionMayor_Menor()
                  
    print("---------------------------")
    print(f"Se a creado con exito el local {nombreLocal} en la ubicacion {ubicacionLocal}")
    print("---------------------------")

    if (count_indumentaria != count_comida) or (count_indumentaria != count_perfumeria) or (count_comida != count_perfumeria):
        print("Rubro con mas locales")
        print(f"El rubro de {datos[0][1]}, con un total de: {datos[1][1]} locales") 
        print("---------------------------")
        print("Rubro con menos locales")
        print(f"El rubro de {datos[0][0]}, con un total de: {datos[1][0]} locales") 
        print("---------------------------\n")
    else:
        print(f"Los rubros tienen la misma cantidad de locales, con {count_indumentaria}")   

    limite-=1
    print(f"Espacio disponible: {limite} ") 

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
        print(f"|{ar_locales[3][c1]}|{ar_locales[3][c1+1]}|{ar_locales[3][c1+2]}|{ar_locales[3][c1+3]}|{ar_locales[3][c1+4]}|")
        c1+=5
    print("+-"*5+"+")

mapa_local()
#Funcion del menu de locales           
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

        accion= input("Ingrese una opcion: ")
        while ((accion!="a") and (accion!="b") and (accion!="c") and (accion!="d")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ")

        match accion:
            case "a":
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
        accion= input("Ingrese una opcion: ")
        while ((accion!="a") and (accion!="b") and (accion!="c") and (accion!="d")):
            print("Opcion no valida")
            accion= input("Ingrese una opcion: ")

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
    global nombreUsuario,claveUsuario
    
    for i in range(4):
        print(i)
        if nombreUsuario==ar_base[i][1] and claveUsuario== ar_base[i][2]:
            return [True,ar_base[i][3]]
    
    return [False]
#Programa Principal
nombreUsuario=input("Ingrese el usuario: ")
claveUsuario=getpass.getpass("Ingrese la clave: ")
print("-----------------------------------------\n")

while(strike!=0):
    check=failLogin()
    if check[0]:
        print("Ingreso exitoso")
        print("-----------------------------------------\n")
        strike=0   
        match check[1]:
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