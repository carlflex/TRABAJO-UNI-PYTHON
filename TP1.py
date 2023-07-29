#Integrantes:
#Gugliermino Carlos
#Teo Valentin Garcia Queipo
#Franco Zariaga
#Comision 1k6

import getpass
import os
from tabulate import tabulate
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Variables globales
intentos=3
cont_indumentaria=0
cont_perfumeria=0
cont_comida=0
cantidadLoc=0
limite=50
tipo_usuario=""
cod_local=1
local_indice=0
maxlen1=0
maxlen2=0
maxlen3=0
fin_cod=True

ar_rubro=["indumentaria","comida","perfumeria"]

opc=["1","2"]

menu=["a","b","c","d","e"]

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

ar_locales=[["" for j in range(3)] for i in range(50)]
ar_locales_estado=["" for  k in range(50)]
ar_locales_cod=[[0 for j in range(2)]for i in range(50)]

#funciones de utilidad
def ar_orden(arreglo,largo,ar2):

    for i in range(1,largo):
        for j in range(largo-i):
            if arreglo[j]>arreglo[j+1]:
                temp=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=temp
                temp2=ar2[j]
                ar2[j]=ar2[j+1]
                ar2[j+1]=temp2
  

def ar_existe(arreglo,largo,elemento):
    ind=0

    while (ind<largo) and (arreglo[ind]!=elemento):
        ind+=1

    if arreglo[ind]==elemento:
        return True
    else:
        return False
    
def dico(arreglo, elemento):
    q = False
    inicio = 0
    fin = len(arreglo) - 1
    while q == False and inicio <= fin:
        medio = (inicio + fin) // 2
        if arreglo[medio][0] == elemento:
            q = True
        else:
            if arreglo[medio][0] > elemento:
                fin = medio - 1
            else:
                inicio = medio + 1

    return q

def mostrar_Local():
    global opc,ar_locales
    print(Fore.LIGHTMAGENTA_EX + "¿Desea ver los locales cargados?")
    print(Style.DIM + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Si")
    print(Style.DIM + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " No")

    verLocales=val_opciones(opc,1,"Opcion no valida","\nIngrese una opcion: ")
    
    if verLocales=="1":
        limpiar_pantalla()
        tablaLOC(ar_locales,ar_locales_estado,ar_locales_cod)
        input()
        limpiar_pantalla()
    else:
        limpiar_pantalla()

def tablaLOC(ar1,ar2,ar3):
    global cantidadLoc,maxlen1,maxlen2,maxlen3
    if ar2[0]!="":
        for i in range(cantidadLoc):
            if maxlen1<len(ar1[i][0]):
                maxlen1=len(ar1[i][0])
            if maxlen2<len(ar1[i][1]):
                maxlen2=len(ar1[i][1])
            if maxlen3<len(ar1[i][2]):
                maxlen3=len(ar1[i][2])
    
        for i in range(cantidadLoc):
            if (ar2[i] == "A"):
                print(Fore.LIGHTMAGENTA_EX + "| Nombre: " + Fore.RESET , f"{ar1[i][0]}"+" " *(maxlen1-len(ar1[i][0])), Fore.LIGHTMAGENTA_EX + "| Ubicación: " + Fore.RESET, f"{ar1[i][1]}"+" " *(maxlen2-len(ar1[i][1])), Fore.LIGHTMAGENTA_EX + "| Rubro: " + Fore.RESET , f"{ar1[i][2]}"+" " *(maxlen3-len(ar1[i][2])), Fore.LIGHTMAGENTA_EX + "| Codigo del usuario: " + Fore.RESET, ar3[i][0], Fore.LIGHTMAGENTA_EX + "| Codigo de local: " + Fore.RESET , ar3[i][1] , Fore.LIGHTMAGENTA_EX + "| Estado: " + Fore.RESET + "Activo" + Fore.LIGHTMAGENTA_EX + "   |")
            elif(ar2[i] == "B"):
                print(Fore.LIGHTMAGENTA_EX + "| Nombre: " + Fore.RESET , f"{ar1[i][0]}"+" " *(maxlen1-len(ar1[i][0])), Fore.LIGHTMAGENTA_EX + "| Ubicación: " + Fore.RESET, f"{ar1[i][1]}"+" " *(maxlen2-len(ar1[i][1])), Fore.LIGHTMAGENTA_EX + "| Rubro: " + Fore.RESET , f"{ar1[i][2]}"+" " *(maxlen3-len(ar1[i][2])), Fore.LIGHTMAGENTA_EX + "| Codigo del usuario: " + Fore.RESET, ar3[i][0], Fore.LIGHTMAGENTA_EX + "| Codigo de local: " + Fore.RESET , ar3[i][1] , Fore.LIGHTMAGENTA_EX + "| Estado: " + Fore.RESET + "Inactivo" + Fore.LIGHTMAGENTA_EX + " |")
    else:
        print(Fore.LIGHTYELLOW_EX + "No se encuentran locales cargados")

def limpiar_pantalla():
    os.system("cls")

def orden_bi(arreglo,filas,columnas,co_orden):
    global ar_locales_cod,ar_locales_estado
    for i in range(filas-1):
        for j in range(i+1,filas):
            if arreglo[i][co_orden]>arreglo[j][co_orden] and arreglo[j][co_orden] !="" :
                for k in range(columnas):
                    temp=arreglo[i][k]
                    arreglo[i][k]=arreglo[j][k]
                    arreglo[j][k]=temp
                for w in range(2):
                    temp=ar_locales_cod[i][w]
                    ar_locales_cod[i][w]=ar_locales_cod[j][w]
                    ar_locales_cod[j][w]=temp
                temp=ar_locales_estado[i]
                ar_locales_estado[i]=ar_locales_estado[j]
                ar_locales_estado[j]=temp

def mostrar_tabla_rub():
    global cont_perfumeria,cont_indumentaria,cont_comida,ar_rubro
    
    ar_contadores=[cont_indumentaria,cont_comida,cont_perfumeria]
    ar_copia_orden=ar_contadores[:]
    ar_rubro_orden=ar_rubro[:]
    ar_orden(ar_copia_orden,3,ar_rubro_orden)

    rubro_mayor=ar_rubro_orden[2]
    rubro_medio=ar_rubro_orden[1]
    rubro_menor=ar_rubro_orden[0]

    mayor=ar_copia_orden[2]
    medio=ar_copia_orden[1]
    menor=ar_copia_orden[0]

    print("===========================")
    print("|" + Fore.LIGHTMAGENTA_EX + " Rubro " + Fore.RESET +" "*(len("indumentaria")-len("rubro"))+ "| " + Fore.LIGHTMAGENTA_EX + "Cantidad " + Fore.RESET + "|")
    print("|--"+"-"*len("indumentaria")+"|----------|")
    print(f"| {rubro_mayor} "+" "*(len("indumentaria")-len(rubro_mayor))+"|"+f"     {mayor}    |")
    print(f"| {rubro_medio} "+" "*(len("indumentaria")-len(rubro_medio))+"|"+f"     {medio}    |")
    print(f"| {rubro_menor} "+" "*(len("indumentaria")-len(rubro_menor))+"|"+f"     {menor}    |")
    
def carga_locales(ar_datos,ar_destino,fila,col):

    for i in range(col):
        ar_destino[fila][i]=ar_datos[i]

def print_menus(tipo):
    match tipo:
        case "admin":
            print(Style.BRIGHT + Fore.MAGENTA + "MENU ADMINISTRADORES")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Gestion de locales")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " Crear cuentas de dueños locales")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "3." + Fore.RESET + " Aprobar / Denegar solicitud de descuento")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "4." + Fore.RESET + " Gestion de Novedades")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "5." + Fore.RESET + " Reporte de utilización de descuentos")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "0." + Fore.RESET + " Salir")
        case "descuento":
            print(Style.BRIGHT + Fore.MAGENTA + "MENU DUEÑOS DE LOCALES")
            print(Style.NORMAL + Fore.LIGHTMAGENTA_EX + "\n1." + Fore.RESET + " Gestión de Descuentos")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "   a)" + Fore.RESET + " Crear descuento para mi local")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "   b)" + Fore.RESET + " Modificar descuento de mi local")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "   c)" + Fore.RESET + " Eliminar descuento de mi local")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "   d)" + Fore.RESET + " Volver")
            print(Style.NORMAL + Fore.LIGHTMAGENTA_EX + "2." + Fore.RESET + " Aceptar / Rechazar pedido de descuento")
            print(Style.NORMAL + Fore.LIGHTMAGENTA_EX + "3." + Fore.RESET + " Reporte de uso de descuentos")
            print(Style.NORMAL + Fore.LIGHTMAGENTA_EX + "0." + Fore.RESET + " Salir")
        case "cliente":
            print(Style.BRIGHT + Fore.MAGENTA + "MENU CLIENTES")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Registrarme")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " Buscar descuentos en locales")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "3." + Fore.RESET + " Solicitar descuento")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "4." + Fore.RESET + " Ver novedades")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "0." + Fore.RESET + " Salir")
        case "dueño":
            print(Style.BRIGHT + Fore.MAGENTA + "MENU DUEÑOS DE LOCALES")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Gestión de Descuentos")
            print(Style.DIM + Fore.LIGHTMAGENTA_EX + "   a)" + Fore.RESET + " Crear descuento para mi local")
            print(Style.DIM + Fore.LIGHTMAGENTA_EX + "   b)" + Fore.RESET + " Modificar descuento de mi local")
            print(Style.DIM + Fore.LIGHTMAGENTA_EX + "   c)" + Fore.RESET + " Eliminar descuento de mi local")
            print(Style.DIM + Fore.LIGHTMAGENTA_EX + "   d)" + Fore.RESET + " Volver")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " Aceptar / Rechazar pedido de descuento")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "3." + Fore.RESET + " Reporte de uso de descuentos")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "0." + Fore.RESET + " Salir")
        case "novedades":
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "GESTION DE NOVEDADES")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "\na)" + Fore.RESET + " Crear novedades")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "b)" + Fore.RESET + " Modificar novedad")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "c)" + Fore.RESET + " Eliminar novedad")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "d)" + Fore.RESET + " Ver reporte de novedades")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "e)" + Fore.RESET + " Volver")
        case "local":
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "GESTION DE LOCALES")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "\na)" + Fore.RESET + " Crear locales")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "b)" + Fore.RESET + " Modificar local")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "c)" + Fore.RESET + " Eliminar locales")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "d)" + Fore.RESET + " Mapa de locales")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "e)" + Fore.RESET + " Volver")

# Funciones de validacion
def valid_codigo_usuario():
    valido= True

    cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))

    while valido:
        ind=0
        while  (ind <= 2) and (ar_codigos[ind]!=cod) :
            ind+=1

        if ar_codigos[ind]==cod:
            if ar_base[ind][2]=="dueñoLocal":
                valido=False
            else:
                print(Fore.LIGHTYELLOW_EX + "Usted no es dueño")
                cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))
        else:
            print(Fore.LIGHTRED_EX + "Codigo incorrecto")
            cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))
    
    return cod     

def val_datos_local(dato):
    global ar_locales_cod,local_indice,fin_cod
    ind=0

    if dato==0:
        fin_cod=False
        return False

    while  (ind < 49) and dato !=ar_locales_cod[ind][1]:
        ind+=1
    
    if ar_locales_cod[ind][1]==dato:
      fin_cod=True
      local_indice=ind
      return False
    else:
        return True

def val_nombre():
    global ar_locales
    nombre=input(Fore.LIGHTCYAN_EX + "Ingrese el nombre: " + Fore.RESET)

    while dico(ar_locales,nombre) and nombre !="*" or nombre=="":
        print(Fore.LIGHTRED_EX + "Nombre ya existente o es invalido, elija otro")
        nombre=input(Fore.LIGHTCYAN_EX + "Ingrese el nombre: " + Fore.RESET)

    return nombre

def val_opciones(ar,largo,error,mensaje):

    opt=input(Fore.LIGHTCYAN_EX + mensaje + Fore.RESET)

    while not ar_existe(ar,largo,opt):
        print(Fore.LIGHTRED_EX + error)
        opt=input(Fore.LIGHTCYAN_EX + mensaje + Fore.RESET)
    return opt
        

#Funcion de construccion
def en_construccion():
    limpiar_pantalla()
    print(Fore.YELLOW + "|￣￣￣￣￣￣￣￣￣￣￣￣￣￣|")
    print(Fore.YELLOW + "      EN CONTRUCCION        ")
    print(Fore.YELLOW + "|__________________________|")
    print(Fore.YELLOW + "        \ (• ◡ •) /          ")
    print(Fore.YELLOW + "         \       /         ")
    input()
    limpiar_pantalla()

def operar_contadores(rubro,tipo):
    global cont_comida,cont_indumentaria,cont_perfumeria

    match tipo:
        case "aumentar":
            match rubro:
                case "indumentaria":
                    cont_indumentaria+=1
                case "comida":
                    cont_comida+=1
                case "perfumeria":
                    cont_perfumeria+=1
        case "restar":
            match rubro:
                case "indumentaria":
                    cont_indumentaria-=1
                case "comida":
                    cont_comida-=1
                case "perfumeria":
                    cont_perfumeria-=1

#Funcion del menu de locales   
def CreacionLocal():
    global limite,cod_local,ar_locales,ar_locales_cod,ar_rubro,ar_locales_estado,cantidadLoc
    
    mostrar_Local()

    nombreLocal = val_nombre()

    while nombreLocal !="*":
        limpiar_pantalla()
        ubicacionLocal=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET)
        limpiar_pantalla()
        rubroLocal=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")

        limpiar_pantalla()
        cod_usuario=valid_codigo_usuario()
        
        operar_contadores(rubroLocal,"aumentar")
                    
        limpiar_pantalla()
        print(Fore.LIGHTGREEN_EX + "Se a creado con exito el local" + Fore.RESET, nombreLocal, Fore.LIGHTGREEN_EX + "la ubicacion" + Fore.RESET, ubicacionLocal, "\n")

        ar_local_datos=[nombreLocal,ubicacionLocal,rubroLocal]
        
        carga_locales(ar_local_datos,ar_locales,cod_local-1,3)
        ar_locales_estado[cod_local-1]="A"
        ar_locales_cod[cod_local-1][0]=cod_usuario
        ar_locales_cod[cod_local-1][1]=cod_local
        cod_local+=1
        limite-=1
        cantidadLoc=cantidadLoc+1
        orden_bi(ar_locales,50,3,0)
        print(ar_locales)
        mostrar_tabla_rub()
        print(Back.LIGHTGREEN_EX + f"\nEspacio disponible: {limite} ")
        input()
        limpiar_pantalla()
        nombreLocal= val_nombre()

    limpiar_pantalla()

def mod_local():
    global ar_locales,ar_locales_cod,local_indice,ar_rubro, opc,ar_locales_estado,fin_cod

    opcMOD=["1","2","3","4","5","6"]
    
    limpiar_pantalla()
    mostrar_Local()

    entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea modificar: " + Fore.RESET))

    while val_datos_local(entrada_cod_local):
        print(Fore.LIGHTRED_EX + "\nCodigo no existe")
        entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea modificar: " + Fore.RESET))
    
    limpiar_pantalla()

    if fin_cod:  
        if ar_locales_estado[local_indice]=="B":
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "El local esta dado de baja, ¿Desea activarlo?")
            print(Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + "Si")
            print(Fore.LIGHTCYAN_EX + "2." + Fore.RESET + "No")
        
            accion=val_opciones(opc,1,"Opcion no valida","\nIngrese una opcion: ")

            if accion=="1":
                ar_locales_estado[local_indice]="A"
                operar_contadores(ar_locales[local_indice][2],"aumentar")

        if ar_locales_estado[local_indice]=="A":
            limpiar_pantalla()
            print(Fore.LIGHTGREEN_EX + "Modificacion de datos del local" + Fore.RESET, entrada_cod_local, Fore.LIGHTGREEN_EX + "alias" + Fore.RESET, ar_locales[local_indice][0])

            print(Fore.LIGHTCYAN_EX + "\n1. " + Fore.RESET +  "Modificar todo")
            print(Fore.LIGHTCYAN_EX + "2. " + Fore.RESET + "Modificar nombre")
            print(Fore.LIGHTCYAN_EX + "3. " + Fore.RESET + "Modificar ubicacion")
            print(Fore.LIGHTCYAN_EX + "4. " + Fore.RESET + "Modificar rubro")
            print(Fore.LIGHTCYAN_EX + "5. " + Fore.RESET + "Modificar codigo de usuario")
            print(Fore.LIGHTCYAN_EX + "6. " + Fore.RESET + "Volver")

            accion=val_opciones(opcMOD,5,"Opcion no valida","\nIngrese una opcion: ")
            
            match accion:
                case "1":
                    limpiar_pantalla()
                    nombreLocal= val_nombre()
                    limpiar_pantalla()
                    ubicacionLocal=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET)
                    limpiar_pantalla()
                    rubroLocal=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")
                    limpiar_pantalla()
                    cod_usuario=valid_codigo_usuario()
                    limpiar_pantalla()
                    operar_contadores(ar_locales[local_indice][2],"restar")
                    operar_contadores(rubroLocal,"aumentar")

                    ar_datos=[nombreLocal,ubicacionLocal,rubroLocal]
                    carga_locales(ar_datos,ar_locales,local_indice,3)
                    ar_locales_cod[local_indice][0]=cod_usuario
                    orden_bi(ar_locales,50,4,0)
                case "2":
                    limpiar_pantalla()
                    nombreLocal= val_nombre()
                    ar_locales[local_indice][0]=nombreLocal
                    orden_bi(ar_locales,50,4,0)
                case "3":
                    limpiar_pantalla()
                    ubicacionLocal=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET)
                    ar_locales[local_indice][1]=ubicacionLocal
                case "4":
                    limpiar_pantalla()
                    rubroLocal=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")
                    operar_contadores(ar_locales[local_indice][2],"restar")
                    operar_contadores(rubroLocal,"aumentar")
                    ar_locales[local_indice][2]=rubroLocal
                case "5":
                    limpiar_pantalla()
                    cod_usuario=valid_codigo_usuario()
                    ar_locales_cod[local_indice][0]=cod_usuario
                case "6":
                    ""
            
def eliminar_local():
    global ar_locales, opc,ar_locales_estado,fin_cod

    limpiar_pantalla()
    mostrar_Local()

    entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea eliminar: " + Fore.RESET))

    while val_datos_local(entrada_cod_local):
        print(Fore.LIGHTRED_EX + "\nCodigo no existe")
        entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea eliminar: " + Fore.RESET))

    limpiar_pantalla()

    if fin_cod:
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "¿Desea dar de baja este local?")
        print(Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + "Si")
        print(Fore.LIGHTCYAN_EX + "2." + Fore.RESET + "No")

        opcion=val_opciones(opc,1,"Opcion no valida","\nIngrese una opcion: ")

        if opcion =="1":
            ar_locales_estado[local_indice]="B"
            operar_contadores(ar_locales[local_indice][2],"restar")

def limite_local():
    global limite

    if limite != 0:
        CreacionLocal()
    else:
        print(Style.BRIGHT + Fore.YELLOW + "No hay espacio para mas locales")
        input()

def mapa_local():
    global ar_locales_cod
    limpiar_pantalla()

    c1=0
    for i in range(10):
        print("+--"*5+"+")
        for j in range(0,5):
            if ar_locales_cod[c1+j][1]<10:
                print(f"|0{ar_locales_cod[c1+j][1]}",end="")
            else:
                print(f"|{ar_locales_cod[c1+j][1]}",end="")
        print("|")
        
        c1+=5
    print("+--"*5+"+")
    
    getpass.getpass("")
#----------------------------------------------        
def menu_local(): 
    global menu
    fin=True
    while fin:
        limpiar_pantalla()
        print_menus("local")

        accion= val_opciones(menu,4,"\nOpcion no valida","\nIngrese una opcion: ")
       
        match accion:
            case "a":
                limpiar_pantalla()
                limite_local()
            case "b":
                mod_local()
            case "c":
                eliminar_local()
            case "d":
                mapa_local()
            case "e":
                limpiar_pantalla()
                fin=False

#Funcion del menu de novedades
def menu_novedades():
    global menu
    fin=True
    while fin:
        limpiar_pantalla()
        print_menus("novedades")

        accion= val_opciones(menu,4,"\nOpcion no valida","\nIngrese una opcion: ")
        match accion:
            case "a":
                en_construccion()
            case "b":
                en_construccion()
            case "c":
                en_construccion()
            case "d":
                en_construccion()
            case "e":
                limpiar_pantalla()
                fin=False

#Funcion del menu principal
def menuAdmin():
   ar_opciones=["1","2","3","4","5","0"]
   fin=True
   while fin:
        print_menus("admin")

        accion= val_opciones(ar_opciones,5,"\nOpcion no valida","\nIngrese una opcion: ")
        match accion:
            case "1":
                menu_local()
            case "2":
                en_construccion()
            case "3":
                en_construccion()
            case "4":
                menu_novedades()
            case "5":
                en_construccion()
            case "0":
                fin=False
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

def menuDueño():
   ar_opciones=["1","2","3","0"]
   fin=True
   while fin:
        print_menus("dueño")

        accion= val_opciones(ar_opciones,3,"\nOpcion no valida","\nIngrese una opcion: ")

        match accion:
            case "1":
                GestionDesc()
            case "2":
                en_construccion()
            case "3":
                en_construccion()
            case "0":
                fin=False
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

def GestionDesc():
    ar_opciones=["a","b","c","d"]
    fin=True
    while fin:
        limpiar_pantalla()
        print_menus("descuento")

        accion=val_opciones(ar_opciones,3,"\nOpcion no valida","\nIngrese una opcion: ")
 
        match accion:
            case "a":
                en_construccion()
            case "b":
                en_construccion()
            case "c":
                en_construccion()
            case "d":
                limpiar_pantalla()
                fin=False

def menuCliente():
   ar_opciones=["1","2","3","4","0"]
   fin=True
   while fin:
        print_menus("cliente")

        accion= val_opciones(ar_opciones,4,"\nOpcion no valida","\nIngrese una opcion: ")
        match accion:
            case "1":
                en_construccion()
            case "2":
                en_construccion()
            case "3":
                en_construccion()
            case "4":
                en_construccion()
            case "0":
                fin=False
                limpiar_pantalla()
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")
                
#Funcion de inicio del programa
def verifNombre():
    global nombreUsuario,tipo_usuario
    verif=False
    
    for i in range(4):
        if nombreUsuario==ar_base[i][0]:
            verif=True
    return verif

def verifClave():
    global nombreUsuario,tipo_usuario
    verif=False
    
    for i in range(4):
        if claveUsuario== ar_base[i][1] and nombreUsuario==ar_base[i][0]:
            tipo_usuario=ar_base[i][2]
            verif=True
    return verif

#Programa Principal
nombreUsuario=input(Style.BRIGHT + Fore.CYAN + "Ingrese el usuario: " + Fore.RESET)

while(intentos!=0):
    chequeo=verifNombre()
    if chequeo:
        claveUsuario=getpass.getpass(Style.BRIGHT + Fore.CYAN + "Ingrese la clave: " + Fore.RESET)
        chequeo2=verifClave()
        if chequeo2:
            limpiar_pantalla()
            print(Style.BRIGHT + Fore.GREEN + "Ingreso exitoso\n")
            intentos=0   
            match tipo_usuario:
                case "administrador":
                    menuAdmin()
                case "dueñoLocal":
                    menuDueño()
                case "cliente":
                    menuCliente()
        else:
            limpiar_pantalla()
            intentos-=1
            print(Style.BRIGHT + Fore.RED + "Clave incorrecta")
            if intentos!=0:
                print(Fore.YELLOW + "\nIntentos restantes: " + Fore.RESET, intentos, "\n")
            else:
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

    else:
        limpiar_pantalla()
        intentos-=1
        print(Style.BRIGHT + Fore.RED + "Usuario incorrecto")
        if intentos!=0:
            print(Fore.YELLOW + "\nIntentos restantes: " + Fore.RESET, intentos, "\n")
            nombreUsuario=input(Style.BRIGHT + Fore.CYAN + "Ingrese el usuario: " + Fore.RESET)
        else: 
            print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")