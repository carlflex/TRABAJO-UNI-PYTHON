#Integrantes:
#García Queipo, Teo Valentín
#Gugliermino, Carlo
#Lopez Evelyn Milagros
#Zariaga, Franco
#Comision 1k6

import pickle
import getpass
import os
from tabulate import tabulate
from colorama import init, Fore, Back, Style
from mostrar import mostrar_contenido
import datetime

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
pos=0
maxlen1=0
maxlen2=0
maxlen3=0
fin_cod=True
cod_usuario=1
cod_prom=0
cant_desc=0
val_clave=0

fecha_actual = datetime.datetime.now().strftime('%d/%m/%Y')

ar_rubro=["indumentaria","comida","perfumeria"]

ar_dias_semana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

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
ar_desc=[["" for j in range(2)] for i in range(50)]
ar_desc_cod=[[0 for j in range(2)]for i in range(50)]
ar_desc_estado=["" for  k in range(50)]
ar_desc_dias=[["" for j in range(6)] for i in range(50)]

ruta_usuarios="./db/usuarios.dat"
ruta_locales="./db/locales.dat"
ruta_auxiliar="./db/aux.dat"
ruta_promociones="./db/promociones.dat"
ruta_usoPromociones="./db/usoPromociones.dat"

def abrir(ruta):
    if not os.path.exists(ruta):   
        objeto = open (ruta, "w+b")   
    else:
        objeto = open (ruta, "r+b")

    return objeto

class Usuario:
    def __init__(self):
        self.codigo=0
        self.correo=""
        self.clave=""
        self.tipo=""

class Local:
    def __init__(self) -> None:
        self.codigo=0
        self.codUsuario=0
        self.nombre=""
        self.ubicacion=""
        self.rubro=""
        self.estado=""

class Promocion:
    def __init__(self):
        self.codProm=0
        self.desc=""
        self.fechaDesde=""
        self.fechaHasta=""
        self.dias=[""]*7
        self.est=""
        self.codLoc=0

class UsoPromocion:
    def __init__(self):
        self.codCliente=0
        self.codPromo=0
        self.fechaUsoPromo=""

#Carga de arreglos
f_usuarios=abrir(ruta_usuarios)
f_locales=abrir(ruta_locales)
f_promociones=abrir(ruta_promociones)
f_usoPromociones=abrir(ruta_usoPromociones)

tamaño_usuarios=os.path.getsize(ruta_usuarios)
tamaño_locales=os.path.getsize(ruta_locales)

fila_local=Local()
fila_usuarios=Usuario()

def actualizar_fila(pos,e):
    global f_locales,ruta_locales

    f_locales.seek(pos)
    pickle.dump(e,f_locales)
    f_locales.seek(0) 

   
#funciones de utilidad
def ultima_fila():
    global f_usuarios,ruta_usuarios

    tamaño=os.path.getsize(ruta_usuarios)
    f_usuarios.seek(tamaño)

def convertir_n(numero):
    if numero <10:
        numero="0"+str(numero)
    else:
        numero=str(numero)
    return numero

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
    
def mostrar_prom():
    global correo, ar_base, ar_codigos

    tamaño=os.path.getsize(ruta_promociones)
    if tamaño!=0:
        f_promociones.seek(0)
        cod_dueño=busqUsuarioActual()
        fila=pickle.load(f_promociones)
        while f_promociones.tell() < tamaño:
            cod_prom_local=fila.codLoc
            cod_prom_dueño=busqDueñoProm(cod_prom_local)
            for i in range(6):
                ar_desc_dias[i]=fila.dias[i]
            if cod_prom_dueño==cod_dueño and fila.est=="Aprobado":
                print("| Codigo Promocion: ", fila.codProm, "| Descripcion: ", fila.desc, "| Fecha de comienzo: ", fila.fechaDesde, "| Fecha de finalizacion: ", fila.fechaHasta, "| Dias: ", ar_desc_dias[0] ,"-", ar_desc_dias[1] ,"-", ar_desc_dias[2] ,"-", ar_desc_dias[3] ,"-", ar_desc_dias[4] ,"-", ar_desc_dias[5] ,"-", ar_desc_dias[6], "| Estado: ", fila.est, "| Codigo del Local: ", fila.codLoc, " |")
            fila=pickle.load(f_promociones)

def busqUsuarioActual():
    global correo, ar_base, ar_codigos
    f_usuarios.seek(0)
    fila=pickle.load(f_usuarios)
    while fila.correo!=correo:
        fila=pickle.load(f_usuarios)
    cod=fila.codigo
    return cod

def busqDueñoProm(codPromLoc):
        f_locales.seek(0)
        band=False
        fila=pickle.load(f_locales)
        while band==False:
            codLoc=fila.codigo
            if codLoc==codPromLoc:
                band=True
            else:
                fila=pickle.load(f_locales)
        codDueño=fila.codUsuario
        return codDueño

def CantProm():
    cont=1
    f_promociones.seek(0)
    tamaño=os.path.getsize(f_promociones)
    fila=pickle.load(f_promociones)
    while f_promociones.tell() < tamaño:
        cont+=1
        fila=pickle.load(f_promociones)
    return cont

def CantUsos(codPromo, fechaDesde, fechaHasta):
    f_usoPromociones.seek(0)
    tamaño_usoProm=os.path.getsize(ruta_usoPromociones)
    fila_usoProm=pickle.load(f_usoPromociones)
    cont=0

    while fila_usoProm.tell() < tamaño_usoProm:
        if codPromo==fila_usoProm.codPromo and fechaDesde >= fila_usoProm.fechaUsoPromo and fechaHasta <= fila_usoProm.fechaUsoPromo:
            cont+=1
        fila_usoProm=pickle.load(f_usoPromociones)

    return cont
        
def limpiar_pantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def orden_bi(arreglo,filas,columnas,co_orden):
    global ar_locales_cod,ar_locales_estado,f_locales

    tamaño=os.path.getsize()
    
    while f_locales.tell()<tamaño:
        ""

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
        case "cliente":
            print(Style.BRIGHT + Fore.MAGENTA + "MENU CLIENTES")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Buscar descuentos en local")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " Solicitar descuento")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "3." + Fore.RESET + " Ver novedades")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "0." + Fore.RESET + " Salir")
        case "dueño":
            print(Style.BRIGHT + Fore.MAGENTA + "MENU DUEÑOS DE LOCALES")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Crear descuento")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " Reporte de uso de descuentos")
            print(Style.NORMAL + Fore.LIGHTCYAN_EX + "3." + Fore.RESET + " Ver novedades")
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
        case "inicio":
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "BIENVENIDO")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + " Ingresar con usuario registrado.")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "2." + Fore.RESET + " Registrarse como cliente.")
            print(Style.DIM + Fore.LIGHTCYAN_EX + "3." + Fore.RESET + " Salir.")

# Funciones de validacion
def valid_codigo_usuario():
    global f_usuarios,tamaño_locales,fila_usuarios
    valido= True

    cod=convertir_n(int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET)))

    while valido:
        verifNombre_n(cod,"codigo")
        if fila_usuarios.codigo==cod:
            print(fila_usuarios.tipo.rstrip(" "))
            if  fila_usuarios.tipo.rstrip(" ")=="Dueño de local":
                valido=False
            else:
                print(Fore.LIGHTYELLOW_EX + "Usted no es dueño")
                cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))
        else:
            print(Fore.LIGHTRED_EX + "Codigo incorrecto")
            cod=convertir_n(int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET)))
    
    return cod     

def val_datos_local(dato):
    global local_indice,fin_cod,f_locales,tamaño_locales,fila_local,pos
    fin=True
    ind=0
    if dato==0:
        fin_cod=False
        return False

    f_locales.seek(0)

    while f_locales.tell() < tamaño_locales and fin:
        fila_local=pickle.load(f_locales)
        if fila_local.codigo==dato:
            pos=f_usuarios.tell()
            local_indice=ind
            fin=False
            fin_cod=True
        else:
            ind+=1
    
    return fin

def val_cod_local(dato):
    global local_indice,fin_cod,f_locales,tamaño_locales,fila_local,pos
    
    fin=True
    f_locales.seek(0)

    while f_locales.tell() < tamaño_locales and fin:
        fila_local=pickle.load(f_locales)
        if fila_local.codigo==dato:
            fin=False
    
    return fin

def val_cod_prom(dato):
    global fecha_actual
    
    band=True
    fin=True
    f_promociones.seek(0)
    tamaño_locales=os.path.getsize(ruta_promociones)

    while f_promociones.tell() < tamaño_locales and band:
        fila_prom=pickle.load(f_promociones)
        if fila_prom.codProm==dato:
            band=False

    if fila_prom.codProm==dato:
        if fila_prom.estado=="Aprobada":
            if fecha_actual >= fila_prom.fechaDesde and fecha_actual <= fila_prom.fechaHasta:
                dia=fecha_actual.weekday()
                if fila_prom.dias[dia]==1:
                    fin=False
                else:
                    print("Error, codigo no valido para este dia de la semana")
            else:
                print("Error, codigo no valido en esta fecha")
        else:
            print("Error, esta promocion todavia no ha sido aprobada")
    else:
        print("Codigo inexistente")
    
    return fin

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

def val_fecha(fecha):
    if datetime.datetime.strptime(fecha, '%d/%m/%Y'):
        return True
    else:
        return False
#--------------------------------------------------------------------
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

def DiagramacionChapin():
    limpiar_pantalla()
    print(Fore.YELLOW + "|￣￣￣￣￣￣￣￣￣￣￣￣￣￣|")
    print(Fore.YELLOW + "   DIAGRAMACION EN CHAPIN    ")
    print(Fore.YELLOW + "|__________________________|")
    print(Fore.YELLOW + "        \ (• ◡ •) /          ")
    print(Fore.YELLOW + "         \       /         ")
    input()
    limpiar_pantalla()
#--------------------------------------------------------
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

#Funciones de manipulacion de datos:
def guardado_locales(e):
    global f_locales,ruta_locales
    
    pickle.dump(e,f_locales)

    f_locales.flush()

def guardado_promociones(e):
    global f_promociones,ruta_promociones
    
    pickle.dump(e,f_promociones)

    f_promociones.flush()

def guardado_usoPromociones(e):
    global f_usoPromociones,ruta_usoPromociones
    
    pickle.dump(e,f_usoPromociones)

    f_usoPromociones.flush()

#Funcion del menu de locales   
def CreacionLocal():
    global limite,cod_local,ar_locales,ar_locales_cod,ar_rubro,ar_locales_estado,cantidadLoc,fila_local
    
    mostrar_Local()

    fila_local.nombre = val_nombre().ljust(50)

    while fila_local.nombre !="*".ljust(50):
        limpiar_pantalla()
        fila_local.ubicacion=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET).ljust(50)
        limpiar_pantalla()
        fila_local.rubro=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ").ljust(50)
        
        limpiar_pantalla()
        print(len(fila_local.rubro))
        fila_local.codUsuario=valid_codigo_usuario()
        
        operar_contadores(fila_local.rubro.rsplit(" "),"aumentar")
                    
        limpiar_pantalla()
        print(Fore.LIGHTGREEN_EX + "Se a creado con exito el local" + Fore.RESET, fila_local.nombre, Fore.LIGHTGREEN_EX + "la ubicacion" + Fore.RESET, fila_local.ubicacion, "\n")

        cod_local+=1
        print(cod_local)
        print(convertir_n(cod_local))
        fila_local.codigo=convertir_n(cod_local)
        
        fila_local.estado="A"

        limite-=1
        cantidadLoc=cantidadLoc+1
        guardado_locales(fila_local)
        mostrar_tabla_rub()
        print(Back.LIGHTGREEN_EX + f"\nEspacio disponible: {limite} ")
        input()
        limpiar_pantalla()
        fila_local.nombre= val_nombre().ljust(50)

   
    limpiar_pantalla()

def mod_local():
    global ar_locales,ar_locales_cod,local_indice,ar_rubro, opc,ar_locales_estado,fin_cod,fila_local,pos

    opcMOD=["1","2","3","4","5","6"]
    
    limpiar_pantalla()
    mostrar_Local()

    entrada_cod_local=convertir_n(int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea modificar: " + Fore.RESET)))

    while val_datos_local(entrada_cod_local):
        print(Fore.LIGHTRED_EX + "\nCodigo no existe")
        entrada_cod_local=convertir_n(int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea modificar: " + Fore.RESET)))
    
    limpiar_pantalla()

    if fin_cod:  
        if fila_local.estado=="B":
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "El local esta dado de baja, ¿Desea activarlo?")
            print(Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + "Si")
            print(Fore.LIGHTCYAN_EX + "2." + Fore.RESET + "No")
        
            accion=val_opciones(opc,1,"Opcion no valida","\nIngrese una opcion: ")

            if accion=="1":
                fila_local.estado="A"
                operar_contadores(fila_local.rubro.strip(" "),"aumentar")
                actualizar_fila(pos,fila_local)

        if fila_local.estado=="A":
            limpiar_pantalla()
            print(Fore.LIGHTGREEN_EX + "Modificacion de datos del local" + Fore.RESET, entrada_cod_local, Fore.LIGHTGREEN_EX + "alias" + Fore.RESET, ar_locales[local_indice][0])

            print(Fore.LIGHTCYAN_EX + "\n1. " + Fore.RESET +  "Modificar todo")
            print(Fore.LIGHTCYAN_EX + "2. " + Fore.RESET + "Modificar nombre")
            print(Fore.LIGHTCYAN_EX + "3. " + Fore.RESET + "Modificar ubicacion")
            print(Fore.LIGHTCYAN_EX + "4. " + Fore.RESET + "Modificar rubro")
            print(Fore.LIGHTCYAN_EX + "5. " + Fore.RESET + "Modificar codigo de usuario")
            print(Fore.LIGHTCYAN_EX + "6. " + Fore.RESET + "Volver")

            accion=val_opciones(opcMOD,5,"Opcion no valida","\nIngrese una opcion: ")
            aux=fila_local.rubro
            match accion:
                case "1":
                    limpiar_pantalla()
                    fila_local.nombre= val_nombre()
                    limpiar_pantalla()
                    fila_local.ubicacion=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET).ljust(50)
                    limpiar_pantalla()
                  
                    fila_local.rubro=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ").ljust(50)
                    limpiar_pantalla()
                    fila_local.codUsuario=valid_codigo_usuario()
                    limpiar_pantalla()
                    operar_contadores(aux.rstrip(" "),"restar")
                    operar_contadores(fila_local.rubro.rstrip(" "),"aumentar")

                    actualizar_fila(pos,fila_local)
                   
                    orden_bi(ar_locales,50,4,0)
                case "2":
                    limpiar_pantalla()
                    fila_local.nombre= val_nombre()

                    actualizar_fila(pos,fila_local)

                    orden_bi(ar_locales,50,4,0)
                case "3":
                    limpiar_pantalla()
                    fila_local.ubicacion=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET).ljust(50)
                   
                    actualizar_fila(pos,fila_local)
                case "4":
                    limpiar_pantalla()
                    fila_local.rubro=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ").ljust(50)
                    operar_contadores(aux.rstrip(" "),"restar")
                    operar_contadores(fila_local.rubro.rstrip(" "),"aumentar")

                    actualizar_fila(pos,fila_local)

                case "5":
                    limpiar_pantalla()
                    fila_local.codUsuario=valid_codigo_usuario()

                    actualizar_fila(pos,fila_local)
               
        print(ar_locales)
            
def eliminar_local():
    global ar_locales, opc,ar_locales_estado,fin_cod,fila_local

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
            fila_local.estado="B"
            operar_contadores(fila_local.rubro.rstrip(" "),"restar")

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

def ReporteAdmin():
    global fecha_actual

    f_locales.seek(0)
    tamaño_loc=os.path.getsize(ruta_locales)
    fila_loc=pickle.load(f_locales)

    f_promociones.seek(0)
    tamaño_prom=os.path.getsize(ruta_promociones)

    print("Ingrese un rango de fechas para generar el reporte: ")
    verif=True
    while verif:
        try:
            fecha_desde = input("Fecha inicial: ")
            fecha_hasta = input("Fecha final: ")
            datetime.datetime.strptime(fecha_desde,'%d/%m/%Y')
            datetime.datetime.strptime(fecha_hasta,'%d/%m/%Y')
            verif=False
        except ValueError or fecha_desde > fecha_hasta and fecha_desde < fecha_actual: 
            print("Fechas invalidas")

    limpiar_pantalla()

    print("Titulo del Informe")
    print("Fecha Desde: ", fecha_desde, "   ", "Fecha Hasta: ", fecha_hasta)
    while fila_loc.tell() < tamaño_loc:
        print("|Codigo Promo|Texto|Fecha desde|Fecha hasta|Cantidad de usos|")
        fila_prom=pickle.load(f_promociones)
        while fila_prom.tell() < tamaño_prom:
            cant=CantUsos(fila_prom.codProm, fecha_desde, fecha_hasta)
            if fila_loc.codigo==fila_prom.codLoc and fila_prom.fechaDesde>=fecha_desde and fila_prom.fechaHasta>=fecha_hasta and fila_prom.estado=="Aprobado":
                print("|", fila_prom.codProm, "|" , fila_prom.desc, "|" , fila_prom.fechaDesde, "|" , fila_prom.fechaHasta, "|" , cant, "|")
            fila_prom=pickle.load(f_promociones)
        fila_loc=pickle.load(f_locales)
    
def BusqDesc():
    global fecha_actual
        
    cod_local_des=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local del que desea encontrar un descuento: " + Fore.RESET))

    while val_datos_local(cod_local_des):
            print(Fore.LIGHTRED_EX + "\nEl codigo no pertenece a ningun local.")
            cod_local_des=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local del que desea encontrar un descuento: " + Fore.RESET))
            
    verif=True
    while verif:
        try:
            fechaDes = input("Ingresa la fecha en la que desea buscar un descuento en formato DD/MM/AAAA")
            datetime.datetime.strptime(fechaDes,'%d/%m/%Y')
            verif=False
        except ValueError or fechaDes<fecha_actual:
            print("Fecha invalida o ya pasada.")

    tamaño_prom=os.path.getsize(ruta_promociones)
    f_promociones.seek(tamaño_prom)

def SolDesc():
    global fecha_actual

    tamaño_usoProm=os.path.getsize(ruta_usoPromociones)
    f_usoPromociones.seek(tamaño_usoProm)
    fila_usoProm=UsoPromocion()
    
    cod=int(input("Codigo de la promocion que quiere utilizar: "))
    verif=val_cod_prom(cod)
    while verif==True:
        print("Vuelva a intentarlo")
        cod=int(input("Codigo de la promocion que quiere utilizar: "))
        verif=val_cod_prom(cod)
    
    codCliente=busqUsuarioActual
    
    fila_usoProm.codCliente=convertir_n(codCliente)
    fila_usoProm.codPromo=convertir_n(cod)
    fila_usoProm.fechaUsoPromo=fecha_actual

    guardado_usoPromociones(fila_usoProm)

def CrearDesc():
    global fecha_actual, ar_base, ar_codigos, ar_locales_cod, cantidadLoc, correo

    mostrar_prom()

    tamaño_prom=os.path.getsize(ruta_promociones)
    f_promociones.seek(tamaño_prom)
    fila_prom=Promocion()

    cod_local=int(input("Ingrese el codigo de local al cual desea aplicar la oferta: "))
    verif=val_cod_local(cod_local)
    while verif==True:
        print("Error, vuelva a intentarlo")
        cod_local=int(input("Ingrese el codigo de local al cual desea aplicar la oferta: "))
        verif=val_cod_local(cod_local)

    cod_prom=CantProm()

    desc = input("Texto descriptivo de la oferta: ").ljust(200)
    
    verif=True
    while verif:
        try:
            fecha_desde = input("Fecha cuando comienza el descuento: ")
            fecha_hasta = input("Fecha cuando termina el descuento: ")
            datetime.datetime.strptime(fecha_desde,'%d/%m/%Y')
            datetime.datetime.strptime(fecha_hasta,'%d/%m/%Y')
            verif=False
        except ValueError or fecha_desde > fecha_hasta and fecha_desde < fecha_actual: 
            print("Fechas invalidas")
    
    dia=0
    while dia < 7:
        print("Dias de la semana que estara vigente el descuento")
        print(ar_dias_semana[dia])
        print("¿Se encuentra vigente?")
        print("1. Si")
        print("0. No")
        fila_prom.dias[dia]=input()
        while fila_prom.dias[dia]!="1" and fila_prom.dias[dia]!="0":
            print("Error, vuelva a intentarlo")
            fila_prom.dias[dia]=input()
        dia=dia+1

    fila_prom.codProm=convertir_n(cod_prom)
    fila_prom.desc=desc
    fila_prom.fechaDesde=fecha_desde
    fila_prom.fechaHasta=fecha_hasta
    fila_prom.est="Pendiente".ljust(10)
    fila_prom.codLoc=convertir_n(cod_local)

    guardado_promociones(fila_prom)

def ReporteDueño():
    global fecha_actual

    f_locales.seek(0)
    tamaño_loc=os.path.getsize(ruta_locales)
    fila_loc=pickle.load(f_locales)

    f_promociones.seek(0)
    tamaño_prom=os.path.getsize(ruta_promociones)

    print("Ingrese un rango de fechas para generar el reporte: ")
    verif=True
    while verif:
        try:
            fecha_desde = input("Fecha inicial: ")
            fecha_hasta = input("Fecha final: ")
            datetime.datetime.strptime(fecha_desde,'%d/%m/%Y')
            datetime.datetime.strptime(fecha_hasta,'%d/%m/%Y')
            verif=False
        except ValueError or fecha_desde > fecha_hasta and fecha_desde < fecha_actual: 
            print("Fechas invalidas")

    limpiar_pantalla()

    print("Titulo del Informe")
    print("Fecha Desde: ", fecha_desde, "   ", "Fecha Hasta: ", fecha_hasta)
    while fila_loc.tell() < tamaño_loc:
        dueño=busqUsuarioActual()
        if dueño==fila_loc.codUsuario:
            cod_loc=fila_loc.codigo
            nom=fila_loc.nombre
            print("\nLocal ", cod_local, ": ", nom, "\n")
            print("|Codigo Promo|Texto|Fecha desde|Fecha hasta|Cantidad de usos|")
            fila_prom=pickle.load(f_promociones)
            while fila_prom.tell() < tamaño_prom:
                cant=CantUsos(fila_prom.codProm, fecha_desde, fecha_hasta)
                if cod_loc==fila_prom.codLoc and fila_prom.fechaDesde>=fecha_desde and fila_prom.fechaHasta>=fecha_hasta and fila_prom.estado=="Aprobado":
                    print("|", fila_prom.codProm, "|" , fila_prom.desc, "|" , fila_prom.fechaDesde, "|" , fila_prom.fechaHasta, "|" , cant, "|")
                fila_prom=pickle.load(f_promociones)
        fila_loc=pickle.load(f_locales)

#----------------------------------------------        
def menu_local(): 
    global menu,ar_locales
    fin=True
    while fin:
        limpiar_pantalla()
        print_menus("local")

        print(ar_locales)
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
        

def controlar_promocion():
    global f_usuarios
    

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
   ar_opciones1=["1","2","3","4","5","0"]
   fin=True
   while fin:
        print_menus("admin")

        accion= val_opciones(ar_opciones1,5,"\nOpcion no valida","\nIngrese una opcion: ")
        match accion:
            case "1":
                menu_local()
            case "2":
                registro_usuario("dueño")
            case "3":
                controlar_promocion()
            case "4":
                menu_novedades()
            case "5":
                ReporteAdmin()
            case "0":
                fin=False
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

def menuDueño():
   ar_opciones2=["1","2","3","0"]
   fin=True
   while fin:
        print_menus("dueño")

        accion= val_opciones(ar_opciones2,3,"\nOpcion no valida","\nIngrese una opcion: ")

        match accion:
            case "1":
                CrearDesc()
            case "2":
                ReporteDueño()
            case "3":
                DiagramacionChapin()
            case "0":
                fin=False
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")


def menuCliente():
   ar_opciones4=["1","2","3","4","0"]
   fin=True
   while fin:
        print_menus("cliente")

        accion= val_opciones(ar_opciones4,4,"\nOpcion no valida","\nIngrese una opcion: ")
        match accion:
            case "1":
                BusqDesc()
            case "2":
                SolDesc()
            case "3":
                DiagramacionChapin()
            case "0":
                fin=False
                limpiar_pantalla()
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")
                
#Funcion de inicio del programa
def registro_usuario(tipo):
    global f_usuarios,cod_usuario,ruta_usuarios

    nuevo_usuario=Usuario()
    nuevo_usuario.correo=input("Ingrese el correo: ").ljust(100)


    while verifNombre_n(nuevo_usuario.correo,"correo"):
        nuevo_usuario.correo=input("Ingrese el correo: ").ljust(100)
    
    nuevo_usuario.clave=input("Ingrese la clave: ")

    while nuevo_usuario.clave=="":
        nuevo_usuario.clave=input("Ingrese la clave: ")

    nuevo_usuario.clave=nuevo_usuario.clave.ljust(8)
    if tipo=="cli":
        nuevo_usuario.tipo="cliente".ljust(20)
    else:
        nuevo_usuario.tipo="Dueño de local".ljust(20)
    cod_usuario+=1
    
    print("len ",len(nuevo_usuario.tipo))
    nuevo_usuario.codigo=convertir_n(cod_usuario)

    ultima_fila()
    
    pickle.dump(nuevo_usuario,f_usuarios)
    f_usuarios.flush()


def verifNombre_n(nombre,campo):
    global tipo_usuario,f_usuarios,fila_usuarios,val_clave

    valid=False
    tamaño=os.path.getsize(ruta_usuarios)

    while f_usuarios.tell() < tamaño:
        fila_usuarios=pickle.load(f_usuarios)

        if fila_usuarios.__getattribute__(campo).rstrip(" ")==nombre:
            valid=True
            tipo_usuario=fila_usuarios.tipo
            val_clave=fila_usuarios.clave.rstrip(" ")
            f_usuarios.seek(tamaño)
    
    f_usuarios.seek(0)
  
    return valid

def ultimo_cod(archivo,tamaño,tipo):

    mayor=0
    if tamaño==0:
        return mayor
    else:
       match tipo:
            case "usuario":
                while archivo.tell()<tamaño:
                    fila=pickle.load(archivo)
                print(fila.codigo)
                mayor=int(fila.codigo)
            case "local":
                while archivo.tell()<tamaño:
                    fila=pickle.load(archivo)
                    if int(fila.codigo) > mayor:
                        mayor=int(fila.codigo)
            
    archivo.seek(0)
    
    return mayor
    

def login():
    global intentos, correo, val_clave
    nombreUsuario=input(Style.BRIGHT + Fore.CYAN + "Ingrese el usuario: " + Fore.RESET)

    while(intentos!=0):
        chequeo=verifNombre_n(nombreUsuario,"correo")
        correo=nombreUsuario
        if chequeo:
            
            chequeo2=False
            q=True

            while  q:
                claveUsuario=getpass.getpass(Style.BRIGHT + Fore.CYAN + "Ingrese la clave: " + Fore.RESET)
                if claveUsuario!= val_clave:
                    limpiar_pantalla()
                    intentos-=1
                    print(Style.BRIGHT + Fore.RED + "Clave incorrecta")
                    if intentos!=0:
                        print(Fore.YELLOW + "\nIntentos restantes: " + Fore.RESET, intentos, "\n")
                        claveUsuario=getpass.getpass(Style.BRIGHT + Fore.CYAN + "Ingrese la clave: " + Fore.RESET)
                    else:
                        q=False
                        print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")
                else:
                    chequeo2=True
                    q=False
            
            if chequeo2:
                limpiar_pantalla()
                print(Style.BRIGHT + Fore.GREEN + "Ingreso exitoso\n")
                intentos=0 
                
                match tipo_usuario.rstrip(" "):
                    case "administrador":
                        menuAdmin()
                    case "Dueño de local":
                        menuDueño()
                    case "cliente":
                        menuCliente()

        else:
            limpiar_pantalla()
            intentos-=1
            print(Style.BRIGHT + Fore.RED + "Usuario inexistente")
            if intentos!=0:
                print(Fore.YELLOW + "\nIntentos restantes: " + Fore.RESET, intentos, "\n")
                nombreUsuario=input(Style.BRIGHT + Fore.CYAN + "Ingrese el usuario: " + Fore.RESET)
            else: 
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

def ini():

    fin=True
    while fin:

        print_menus("inicio")
        accion=val_opciones(["1","2","3"],2,"\nOpcion no valida","\nIngrese una opcion: ")

        match accion:
            case "1":
                login()
                fin=False   
            case "2":
                registro_usuario("cli")
            case "3":
                fin=False

#Programa Principal

cod_usuario=ultimo_cod(f_usuarios,tamaño_usuarios,"usuario")
cod_local=ultimo_cod(f_locales,tamaño_locales,"local")
print(cod_local)
ini()

f_locales.close()
f_usuarios.close()