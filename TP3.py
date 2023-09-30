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

#Carga de arreglos
f_usuarios=abrir(ruta_usuarios)
f_locales=abrir(ruta_locales)
f_promociones=abrir(ruta_promociones)

tamaño_usuarios=os.path.getsize(ruta_usuarios)
tamaño_locales=os.path.getsize(ruta_locales)
tamaño_promociones=os.path.getsize(ruta_promociones)

fila_local=Local()
fila_usuarios=Usuario()
fila_promociones=Promocion()

def carga_ar_locales():
    global ar_locales,ar_locales_cod,ar_locales_estado,ruta_locales,f_locales

    f_locales.seek(0)
    ind=0
    tamaño=os.path.getsize(ruta_locales)
    while f_locales.tell() < tamaño:
        fila=pickle.load(f_locales)
        ar_locales[ind][0]=fila.nombre
        ar_locales[ind][1]=fila.ubicacion
        ar_locales[ind][2]=fila.rubro

        ar_locales_cod[ind][0]=fila.codUsuario
        ar_locales_cod[ind][1]=fila.codigo

        ar_locales_estado[ind]=fila.estado
        ind+=1

    f_locales.seek(0)

def carga_prom():

    ind=0

    while f_promociones.tell() < tamaño_promociones:
        fila=pickle.load(f_promociones)
        ar_desc[ind][0]=fila.desc
        ar_desc[ind][1]=fila.fechaDesde
        ar_desc[ind][2]=fila.fechaHasta

        ar_desc_cod[ind][0]=fila.codProm
        ar_desc_cod[ind][1]=fila.codLoc

        ar_desc_estado[ind]=fila.estado

        dia=0
        while dia < 6:
            ar_desc_dias[ind][dia]=fila_promociones.dias[ind][dia]
            dia+=1
        
        ind+=1
    
    f_promociones.seek(0)

def guardado(ruta,objeto):
    objeto.close()
    objeto = open (ruta, "r+b")

    return objeto

def borrado():
    global f_locales,ruta_locales,ruta_auxiliar

    """ aux=open(ruta_auxiliar,"r+b") """

    os.path

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
        cod_dueño=busqDueñoActual()
        fila=pickle.load(f_promociones)
        while f_promociones.tell() < tamaño:
            cod_prom_local=fila.codLoc
            cod_prom_dueño=busqDueñoProm(cod_prom_local)
            for i in range(6):
                ar_desc_dias[i]=fila.dias[i]
            if cod_prom_dueño==cod_dueño and fila.est=="Aprobado":
                print("| Codigo Promocion: ", fila.codProm, "| Descripcion: ", fila.desc, "| Fecha de comienzo: ", fila.fechaDesde, "| Fecha de finalizacion: ", fila.fechaHasta, "| Dias: ", ar_desc_dias[0] ,"-", ar_desc_dias[1] ,"-", ar_desc_dias[2] ,"-", ar_desc_dias[3] ,"-", ar_desc_dias[4] ,"-", ar_desc_dias[5] ,"-", ar_desc_dias[6], "| Estado: ", fila.est, "| Codigo del Local: ", fila.codLoc, " |")
            fila=pickle.load(f_promociones)

def busqDueñoActual():
    global correo, ar_base, ar_codigos
    i=0
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
        
def limpiar_pantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

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
        case "inicio":
            print("BIENVENIDO")
            print("1.Ingresar como usuario registrado")
            print("2.Registrarse como cliente")
            print("3. Salir")

# Funciones de validacion
def valid_codigo_usuario():
    global f_usuarios,tamaño_locales,fila_usuarios
    valido= True

    cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))

    while valido:
        verifNombre_n(cod,"codigo")
        if fila_usuarios.codigo==cod:
            if  fila_usuarios.tipo=="Dueño de local":
                valido=False
            else:
                print(Fore.LIGHTYELLOW_EX + "Usted no es dueño")
                cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))
        else:
            print(Fore.LIGHTRED_EX + "Codigo incorrecto")
            cod=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo: " + Fore.RESET))
    
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
    print(Fore.YELLOW + "Diagramado en Chapin")
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

#Funciones de manipulacion de datos:
def guardado_locales(e):
    global f_locales,ruta_locales
    
    pickle.dump(e,f_locales)

    f_locales.flush()

def guardado_promociones(promociones,codigos,dias,estados):
    global f_promociones,ruta_promociones
    ind=0
    while promociones[ind][0]!="":
        promocion=Promocion(codigos[ind][0],promociones[ind][0],promociones[ind][1],promociones[ind][2],[dias[ind][0],dias[ind][1],dias[ind][2],dias[ind][3],dias[ind][4],dias[ind][5],dias[ind][6]],estados[ind])
        
        
        pickle.dump(promocion,f_promociones)
        ind+=1
    
    f_locales=guardado(ruta_locales,f_locales)

def guardado_promociones(e):
    global f_promociones,ruta_promociones
    
    pickle.dump(e,f_promociones)

    f_promociones.flush()

#Funcion del menu de locales   
def CreacionLocal():
    global limite,cod_local,ar_locales,ar_locales_cod,ar_rubro,ar_locales_estado,cantidadLoc,fila_local
    
    mostrar_Local()

    fila_local.nombre = val_nombre()

    while fila_local.nombre !="*":
        limpiar_pantalla()
        fila_local.ubicacion=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET)
        limpiar_pantalla()
        fila_local.rubro=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")

        limpiar_pantalla()
        fila_local.codUsuario=valid_codigo_usuario()
        
        operar_contadores(fila_local.rubro,"aumentar")
                    
        limpiar_pantalla()
        print(Fore.LIGHTGREEN_EX + "Se a creado con exito el local" + Fore.RESET, fila_local.nombre, Fore.LIGHTGREEN_EX + "la ubicacion" + Fore.RESET, fila_local.ubicacion, "\n")

        cod_local+=1
        fila_local.codigo=cod_local
        
        fila_local.estado="A"

        limite-=1
        cantidadLoc=cantidadLoc+1
        guardado_locales(fila_local)
        mostrar_tabla_rub()
        print(Back.LIGHTGREEN_EX + f"\nEspacio disponible: {limite} ")
        input()
        limpiar_pantalla()
        fila_local.nombre= val_nombre()

   
    limpiar_pantalla()

def mod_local():
    global ar_locales,ar_locales_cod,local_indice,ar_rubro, opc,ar_locales_estado,fin_cod,fila_local,pos

    opcMOD=["1","2","3","4","5","6"]
    
    limpiar_pantalla()
    mostrar_Local()

    entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea modificar: " + Fore.RESET))

    while val_datos_local(entrada_cod_local):
        print(Fore.LIGHTRED_EX + "\nCodigo no existe")
        entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea modificar: " + Fore.RESET))
    
    limpiar_pantalla()

    if fin_cod:  
        if fila_local.estado=="B":
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "El local esta dado de baja, ¿Desea activarlo?")
            print(Fore.LIGHTCYAN_EX + "\n1." + Fore.RESET + "Si")
            print(Fore.LIGHTCYAN_EX + "2." + Fore.RESET + "No")
        
            accion=val_opciones(opc,1,"Opcion no valida","\nIngrese una opcion: ")

            if accion=="1":
                ar_locales_estado[local_indice]="A"
                operar_contadores(ar_locales[local_indice][2],"aumentar")

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
            
            match accion:
                case "1":
                    limpiar_pantalla()
                    fila_local.nombre= val_nombre()
                    limpiar_pantalla()
                    fila_local.ubicacion=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET)
                    limpiar_pantalla()
                    fila_local.rubro=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ")
                    limpiar_pantalla()
                    fila_local.codUsuario=valid_codigo_usuario()
                    limpiar_pantalla()
                    operar_contadores(ar_locales[local_indice][2],"restar")
                    operar_contadores(fila_local.rubro,"aumentar")

                    ar_local_datos=[fila_local.nombre,fila_local.ubicacion,fila_local.rubro]


                    carga_locales( ar_local_datos,ar_locales,local_indice,3)
                    actualizar_fila(pos,fila_local)
                    ar_locales_cod[local_indice][0]=fila_local.codUsuario
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
            
        print(ar_locales)
            
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
    
def BusqDesc():
 global fecha_actual, fecha_desde, fecha_hasta
    
 entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local del que desea encontrar un descuento: " + Fore.RESET))

 while val_datos_local(entrada_cod_local):
        print(Fore.LIGHTRED_EX + "\nEl codigo no pertenece a ningun local.")
        entrada_cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local del que desea encontrar un descuento: " + Fore.RESET))
        
 Fecha_des= input("Ingresar fecha sobre la que desea saber: ")
 while Fecha_des < fecha_actual:
        print ("La fecha ingresada ya a pasado.")
        Fecha_des= input("Ingresar fecha sobre la que desea saber: ")
 pickle.load(Promocion.Dat)
 

def CrearDesc():
    global fecha_actual, cod_prom, ar_base, ar_codigos, ar_locales_cod, cantidadLoc, correo

    mostrar_prom()

    tamaño_prom=os.path.getsize(ruta_promociones)
    f_promociones.seek(tamaño_prom)
    fila_prom=Promocion()

    cod_local=int(input("Ingrese el codigo de local al cual desea aplicar la oferta: "))
    verif=val_cod_local(cod_local)
    while verif==True:
        cod_local=int(input("Ingrese el codigo de local al cual desea aplicar la oferta: "))
        verif=val_cod_local(cod_local)

    if tamaño_prom!=0:
        f_promociones.seek(tamaño_prom)
        fila=pickle.load(f_promociones)
        cod_prom=fila.codPromo+1
    else:
        cod_prom=1

    desc = input("Texto descriptivo de la oferta: ")

    fecha_actual = datetime.datetime.now().strftime('%d/%m/%Y')

    fecha_desde = input("Fecha cuando comienza el descuento: ")
    fecha_hasta = input("Fecha cuando termina el descuento: ")
    while fecha_desde > fecha_hasta and fecha_desde < fecha_actual:
        print("Fechas invalidas, vuelva a intentarlo")
        fecha_desde = input("Fecha cuando comienza el descuento: ")
        fecha_hasta = input("Fecha cuando termina el descuento: ")
    
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
            ar_desc_dias[dia]=input()
        dia=dia+1

    fila_prom.codProm=cod_prom
    fila_prom.desc=desc
    fila_prom.fechaDesde=fecha_desde
    fila_prom.fechaHasta=fecha_hasta
    fila_prom.est="Pendiente"
    fila_prom.codLoc=cod_local

    guardado_promociones(fila_prom)

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
                en_construccion()
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
                en_construccion()
            case "3":
                DiagramacionChapin()
            case "0":
                fin=False
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

def GestionDesc():
    ar_opciones3=["a","b","c","d"]
    fin=True
    while fin:
        limpiar_pantalla()
        print_menus("descuento")

        accion=val_opciones(ar_opciones3,3,"\nOpcion no valida","\nIngrese una opcion: ")
 
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
   ar_opciones4=["1","2","3","4","0"]
   fin=True
   while fin:
        print_menus("cliente")

        accion= val_opciones(ar_opciones4,4,"\nOpcion no valida","\nIngrese una opcion: ")
        match accion:
            case "1":
                BusqDesc()
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
def registro_usuario(tipo):
    global f_usuarios,cod_usuario,ruta_usuarios

    nuevo_usuario=Usuario()
    nuevo_usuario.correo=input("Ingrese el correo: ")


    while verifNombre_n(nuevo_usuario.correo,"correo"):
        nuevo_usuario.correo=input("Ingrese el correo: ")
    
    nuevo_usuario.clave=input("Ingrese la clave: ")

    while len(nuevo_usuario.clave) != 8:
        nuevo_usuario.clave=input("Ingrese la clave: ")


    if tipo=="cli":
        nuevo_usuario.tipo="cliente"
    else:
        nuevo_usuario.tipo="Dueño de local"
    nuevo_usuario.codigo=cod_usuario+1
    ultima_fila()
    
    pickle.dump(nuevo_usuario,f_usuarios)
    f_usuarios=guardado(ruta_usuarios,f_usuarios)


def verifNombre_n(nombre,campo):
    global tipo_usuario,f_usuarios,fila_usuarios,val_clave

    valid=False
    tamaño=os.path.getsize(ruta_usuarios)

    while f_usuarios.tell() < tamaño:
        fila_usuarios=pickle.load(f_usuarios)

        if fila_usuarios.__getattribute__(campo)==nombre:
            valid=True
            tipo_usuario=fila_usuarios.tipo
            val_clave=fila_usuarios.clave
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
                mayor=fila.codigo
            case "local":
                while archivo.tell()<tamaño:
                    fila=pickle.load(archivo)
                    if fila.codigo > mayor:
                        mayor=fila.codigo
            
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
                
                match tipo_usuario:
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
print(tamaño_usuarios)
cod_usuario=ultimo_cod(f_usuarios,tamaño_usuarios,"usuario")
cod_local=ultimo_cod(f_locales,tamaño_locales,"local")
print(cod_local)
ini()

f_locales.close()
f_usuarios.close()

