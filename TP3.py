#Integrantes:
#García Queipo, Teo Valentín
#Gugliermino, Carlo
#Lopez Evelyn Milagros
#Zariaga, Franco
#Comision 1k6

import pickle
import getpass
import os
from colorama import init, Fore, Back, Style
import datetime

init(autoreset=True)

#Correos y contraseñas de los usuarios guardados en el archivo usuarios.dat
#ADMIN: admin@shopping.com, 12345
#DUEÑOS LOCALES: gonzalo@gmail.com, 12345 ; carmen@gmail.com, 1234
#CLIENTES: malena@gmail.com, 12345 ; ricardo@gmail.com, 1234

#Variables globales
intentos=3
cont_indumentaria=0
cont_perfumeria=0
cont_comida=0
cantidadLoc=0
tipo_usuario=""
cod_local=1
local_indice=0
pos=0
maximo=0
maxlen1=0
maxlen2=0
maxlen3=0
fin_cod=True
cod_usuario=1
cod_prom=0
cant_desc=0
val_clave=0
posicion=0
fecha_actual_aux = datetime.datetime.now().strftime('%d/%m/%Y')
fecha_actual = datetime.datetime.strptime(fecha_actual_aux, '%d/%m/%Y').date()

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
ar_desc_dias=[[0 for j in range(6)] for i in range(50)]

ruta_usuarios="./usuarios.dat"
ruta_locales="./locales.dat"
ruta_auxiliar="./aux.dat"
ruta_promociones="./promociones.dat"
ruta_usoPromociones="./usoPromociones.dat"

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
        self.codPromo=0
        self.textoPromo=""
        self.fechaDesdePromo=""
        self.fechaHastaPromo=""
        self.diasSemana=[0]*7
        self.estado=""
        self.codLocal=0

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

    f_locales.seek(pos-274)

    pickle.dump(e,f_locales)
    f_locales.seek(0)

    f_locales.flush() 

   
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

def dico(elemento):
    global ruta_locales,f_locales,ruta_locales
    
    tamaño=os.path.getsize(ruta_locales)

    f_locales.seek(0)

    """ fila=pickle.load(f_locales) """
    t_fila=f_locales.tell()
    q = False
    inicio = 1
    fin = int(tamaño/274)
    while q == False and inicio <= fin:
        medio = (inicio + fin) // 2
        f_locales.seek((274*medio)-274)        
        fila=pickle.load(f_locales)

        if fila.nombre.rstrip(" ") == elemento:
            q = True
        else:
            if fila.nombre > elemento:
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
        tablaLOC()
        input()
        limpiar_pantalla()
    else:
        limpiar_pantalla()

def tablaLOC():
    global f_locales,ruta_locales
    tamaño_loc=os.path.getsize(ruta_locales)
    band=True
    if tamaño_loc!=0:
        f_locales.seek(0)
        fila=pickle.load(f_locales)
        maxlen1=0
        maxlen2=0
        maxlen3=0
        while f_locales.tell() <= tamaño_loc and band==True:
            if maxlen1<len(fila.nombre.strip(" ")):
                maxlen1=len(fila.nombre.strip(" "))
            if maxlen2<len(fila.ubicacion.strip(" ")):
                maxlen2=len(fila.ubicacion.strip(" "))
            if maxlen3<len(fila.rubro.strip(" ")):
                maxlen3=len(fila.rubro.strip(" "))
            if f_locales.tell() < tamaño_loc:
                fila=pickle.load(f_locales)
            else:
                band=False

        f_locales.seek(0)
        fila=pickle.load(f_locales)
        band=True
        while f_locales.tell() <= tamaño_loc and band==True: 
            print(Fore.LIGHTMAGENTA_EX + "|| Nombre: " + Fore.RESET , fila.nombre.strip(" ") ," " *(maxlen1-len(fila.nombre.strip(" "))), Fore.LIGHTMAGENTA_EX + "| Ubicación: " + Fore.RESET, fila.ubicacion.strip(" ") ," " *(maxlen2-len(fila.ubicacion.strip(" "))), Fore.LIGHTMAGENTA_EX + "| Rubro: " + Fore.RESET , fila.rubro.strip(" ") ," " *(maxlen3-len(fila.rubro.strip(" "))), Fore.LIGHTMAGENTA_EX + "| Codigo del usuario: " + Fore.RESET, fila.codUsuario , Fore.LIGHTMAGENTA_EX + "| Codigo de local: " + Fore.RESET , fila.codigo , Fore.LIGHTMAGENTA_EX + "| Estado: " + Fore.RESET, fila.estado, Fore.LIGHTMAGENTA_EX + "||" + Fore.RESET)
            if f_locales.tell() < tamaño_loc:
                fila=pickle.load(f_locales)
            else:
                band=False
    else:
        print(Fore.LIGHTYELLOW_EX + "No se encuentran locales cargados")
    
def mostrar_prom():
    global correo, ar_base, ar_codigos

    limpiar_pantalla()
    cont=0
    tamaño=os.path.getsize(ruta_promociones)
    if tamaño!=0:
        f_promociones.seek(0)
        cod_dueño=busqUsuarioActual()
        fila=pickle.load(f_promociones)
        band1=True
        maxlen=0
        while f_promociones.tell() <= tamaño and band1==True:
            if maxlen<len(fila.textoPromo.strip(" ")):
                maxlen=len(fila.textoPromo.strip(" "))
            if f_promociones.tell() < tamaño:
                fila=pickle.load(f_promociones)
            else:
                band1=False

        f_promociones.seek(0)
        fila=pickle.load(f_promociones)
        band2=True
        while f_promociones.tell() <= tamaño and band2==True:
            cod_prom_local=int(fila.codLocal)
            cod_prom_dueño=busqDueñoProm(cod_prom_local)
            for i in range(7):
                ar_desc_dias[i]=fila.diasSemana[i]
            if cod_prom_dueño==cod_dueño:
                cont=1
                print(Fore.LIGHTCYAN_EX + "| Codigo Promocion: " + Fore.RESET, fila.codPromo, Fore.LIGHTCYAN_EX + "| Descripcion: " + Fore.RESET, fila.textoPromo.strip(" "), " " * (maxlen-len(fila.textoPromo.strip(" "))), Fore.LIGHTCYAN_EX + "| Fecha de comienzo: " + Fore.RESET, fila.fechaDesdePromo, Fore.LIGHTCYAN_EX + "| Fecha de finalizacion: " + Fore.RESET, fila.fechaHastaPromo, Fore.LIGHTCYAN_EX + "| Dias: " + Fore.RESET, ar_desc_dias[0] ,Fore.LIGHTCYAN_EX + "-" + Fore.RESET, ar_desc_dias[1] ,Fore.LIGHTCYAN_EX + "-" + Fore.RESET, ar_desc_dias[2] ,Fore.LIGHTCYAN_EX + "-" + Fore.RESET, ar_desc_dias[3] ,Fore.LIGHTCYAN_EX + "-" + Fore.RESET, ar_desc_dias[4] ,Fore.LIGHTCYAN_EX + "-" + Fore.RESET, ar_desc_dias[5] ,Fore.LIGHTCYAN_EX + "-" + Fore.RESET, ar_desc_dias[6], Fore.LIGHTCYAN_EX + "| Estado: " + Fore.RESET, fila.estado, Fore.LIGHTCYAN_EX + "| Codigo del Local: " + Fore.RESET, fila.codLocal, Fore.LIGHTCYAN_EX + " |" + Fore.RESET)
            if f_promociones.tell() < tamaño:
                fila=pickle.load(f_promociones)
            else:
                band2=False
    if cont==0:
        print(Fore.LIGHTYELLOW_EX + "No se encuentran promociones que cumplan" + Fore.RESET)
    input()

def busqUsuarioActual():
    global correo

    f_usuarios.seek(0)
    fila=pickle.load(f_usuarios)
    tamaño=os.path.getsize(ruta_usuarios)
    band=True
    while f_usuarios.tell() <= tamaño and band==True:
        if fila.correo.strip(" ")==correo:
            band=False
        if f_usuarios.tell() < tamaño and band==True:
            fila=pickle.load(f_usuarios)
        else:
            band=False
    cod=int(fila.codigo)
    return cod

def busqDueñoProm(codPromLoc):
        f_locales.seek(0)
        band=False
        fila=pickle.load(f_locales)
        while band==False:
            codLoc=int(fila.codigo)
            if codLoc==codPromLoc:
                band=True
            else:
                fila=pickle.load(f_locales)
        codDueño=int(fila.codUsuario)
        return codDueño

def CantProm():
    global f_promociones
    cont=1
    tamaño=os.path.getsize(ruta_promociones)
    
    if tamaño!=0:
        f_promociones.seek(0)
        fila=pickle.load(f_promociones)
        f_promociones.seek(tamaño-f_promociones.tell())
        fila=pickle.load(f_promociones)
        cont=int(fila.codPromo)+1
    return cont

def CantUsos(codPromo, fechaDesde, fechaHasta):
    f_usoPromociones.seek(0)
    tamaño_usoProm=os.path.getsize(ruta_usoPromociones)

    cont=0
    band=True
    if tamaño_usoProm!=0:
        fila_usoProm=pickle.load(f_usoPromociones)

        while f_usoPromociones.tell() <= tamaño_usoProm and band==True:
            codUsoProm=int(fila_usoProm.codPromo)
            fechaUsoPromo = datetime.datetime.strptime(fila_usoProm.fechaUsoPromo,'%d/%m/%Y').date()
            if codPromo==codUsoProm and fechaDesde <= fechaUsoPromo and fechaHasta >= fechaUsoPromo:
                cont+=1
            if f_usoPromociones.tell() < tamaño_usoProm:
                fila_usoProm=pickle.load(f_usoPromociones)
            else:
                band=False

    return cont
        
def limpiar_pantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def orden_bi():
    global ar_locales_cod,ar_locales_estado,f_locales,ruta_locales

    tamaño=os.path.getsize(ruta_locales)
    f_locales.seek(0)
    cant_filas=int(tamaño/274)
    for i in range(1,cant_filas):
        for j in range(0,cant_filas-i):
            f_locales.seek(j*274)
            aux=pickle.load(f_locales)
          
            f_locales.seek((j+1)*274)
            fila=pickle.load(f_locales)
          
            if aux.nombre>fila.nombre:
                f_locales.seek(j*274)
                pickle.dump(fila,f_locales)
                f_locales.seek((j + 1)*274)
                pickle.dump(aux,f_locales)
                f_locales.flush()
                
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
    
def carga_locales():
    global f_locales,ar_locales_estado,ar_locales_cod,ruta_locales

    tamaño=os.path.getsize(ruta_locales)
    ind=0

    f_locales.seek(0)

    while f_locales.tell()<tamaño:
        fila=pickle.load(f_locales)

        ar_locales_cod[ind][1]=int(fila.codigo)
        ar_locales_estado[ind]=fila.estado
        ind+=1
    f_locales.seek(0)

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
            if  fila_usuarios.tipo.rstrip(" ")=="Dueno de local":
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
            pos=f_locales.tell()
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
    tamaño_loc=os.path.getsize(ruta_locales)
    band=True
    fila_local=pickle.load(f_locales)
    while f_locales.tell() <= tamaño_loc and band==True:
        cod=int(fila_local.codigo)
        if cod==dato:
            fin=False
            band=False
        if f_locales.tell() < tamaño_loc:
            fila_local=pickle.load(f_locales)
        else:
            band=False
    return fin

def val_cod_prom(dato):
    global fecha_actual,posicion
    
    band=True
    fin=True
    f_promociones.seek(0)
    tamaño_promo=os.path.getsize(ruta_promociones)

    fila_prom=pickle.load(f_promociones)
    while f_promociones.tell() <= tamaño_promo and band:
        codProm=int(fila_prom.codPromo)
        if codProm==dato:
            band=False

        if f_promociones.tell() < tamaño_promo and band==True:
            fila_prom=pickle.load(f_promociones)
        else:
            band=False

    if codProm==dato:
        estado=fila_prom.estado.strip(" ")
        if estado=="Aprobada":
            fechaDesde=datetime.datetime.strptime(fila_prom.fechaDesdePromo, '%d/%m/%Y').date()
            fechaHasta=datetime.datetime.strptime(fila_prom.fechaHastaPromo, '%d/%m/%Y').date()
            if fecha_actual >= fechaDesde and fecha_actual <= fechaHasta:
                dia=fecha_actual.weekday()
                if fila_prom.diasSemana[dia]==1:
                    fin=False
                else:
                    print(Fore.LIGHTRED_EX + "Error, codigo no valido para este dia de la semana\n" + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + "Error, codigo no valido en esta fecha\n" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "Error, esta promocion todavia no ha sido aprobada\n" + Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX + "Codigo inexistente\n" + Fore.RESET)
    
    return fin

def val_nombre():
    global ar_locales
    nombre=input(Fore.LIGHTCYAN_EX + "Ingrese el nombre: " + Fore.RESET)

    while dico(nombre) and nombre !="*" or nombre=="":
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

def DiagramacionChapin():
    limpiar_pantalla()
    print(Fore.YELLOW + "|￣￣￣￣￣￣￣￣￣￣￣￣￣|")
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
    
    tamaño=os.path.getsize(ruta_locales)
    f_locales.seek(tamaño)

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
    global cod_local,ar_locales,ar_locales_cod,ar_rubro,ar_locales_estado,cantidadLoc,fila_local, maximo
    
    mostrar_Local()

    fila_local.nombre = val_nombre().ljust(50)

    while fila_local.nombre !="*".ljust(50):
        limpiar_pantalla()
        fila_local.ubicacion=input(Fore.LIGHTCYAN_EX + "Ingrese la ubicacion: " + Fore.RESET).ljust(50)
        limpiar_pantalla()
        fila_local.rubro=val_opciones(ar_rubro,2,"El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida","Ingrese el rubro: ").ljust(50)
        
        limpiar_pantalla()
        
        fila_local.codUsuario=valid_codigo_usuario()
        
        operar_contadores(fila_local.rubro.rstrip(" "),"aumentar")
                    
        limpiar_pantalla()
        print(Fore.LIGHTGREEN_EX + "Se a creado con exito el local" + Fore.RESET, fila_local.nombre, Fore.LIGHTGREEN_EX + "la ubicacion" + Fore.RESET, fila_local.ubicacion, "\n")

        cod_local+=1

        fila_local.codigo=convertir_n(cod_local)
        
        fila_local.estado="A"

        cantidadLoc=cantidadLoc+1
        guardado_locales(fila_local)
        mostrar_tabla_rub()
        print(Back.LIGHTGREEN_EX + f"\nEspacio disponible: {maximo} ")
        input()
        limpiar_pantalla()
        fila_local.nombre= val_nombre().ljust(50)

    orden_bi()
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
            print(Fore.LIGHTGREEN_EX + "Modificacion de datos del local" + Fore.RESET, entrada_cod_local, Fore.LIGHTGREEN_EX + "alias" + Fore.RESET, fila_local.nombre)

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
                    fila_local.nombre= val_nombre().ljust(50)
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
                   
                    orden_bi()
                case "2":
                    limpiar_pantalla()
                    fila_local.nombre= val_nombre().ljust(50)

                    actualizar_fila(pos,fila_local)

                    orden_bi()
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
               
            
def eliminar_local():
    global ar_locales, opc,ar_locales_estado,fin_cod,fila_local,pos

    limpiar_pantalla()
    mostrar_Local()

    entrada_cod_local=convertir_n(int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local que desea eliminar: " + Fore.RESET)))

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
            actualizar_fila(pos,fila_local)

def limite_local():
    global maximo

    tamaño=os.path.getsize(ruta_locales)
    maximo=int(tamaño/274)
    if maximo < 50:
        CreacionLocal()
    else:
        print(Style.BRIGHT + Fore.YELLOW + "No hay espacio para mas locales")
        input()

def mapa_local():
    global ar_locales_cod,ar_locales_estado
    limpiar_pantalla()

    c1=0
    for i in range(10):
        print("+--"*5+"+")
        for j in range(0,5):
            if ar_locales_cod[c1+j][1]<10:
                if  ar_locales_estado[c1+j]=="B":
                    print(f"|{Fore.LIGHTRED_EX}0{ar_locales_cod[c1+j][1]}" + Fore.RESET,end="")
                else:
                    print(f"|{Fore.LIGHTGREEN_EX}0{ar_locales_cod[c1+j][1]}" + Fore.RESET,end="")
            else:
                if  ar_locales_estado[c1+j]=="B":
                    print(f"|{Fore.LIGHTRED_EX}{ar_locales_cod[c1+j][1]}" + Fore.RESET,end="")
                else:
                    print(f"|{Fore.LIGHTGREEN_EX}{ar_locales_cod[c1+j][1]}" + Fore.RESET,end="")
        print("|")
        
        c1+=5
    print("+--"*5+"+")
    
    getpass.getpass("")


def valid_cod_promocion(cod,tamaño_prom):
        global f_promociones,posicion

        band=True
        fin=True
        f_promociones.seek(0)
        fila_prom=pickle.load(f_promociones)
        while f_promociones.tell() <= tamaño_prom and band==True:
            codProm=int(fila_prom.codPromo)
            if codProm==cod:
                band=False
            if f_promociones.tell() < tamaño_prom and band==True:
                fila_prom=pickle.load(f_promociones)
            else:
                band=False
        if codProm==cod:
            estado=fila_prom.estado.strip(" ")
            if estado=="Pendiente":
                fin=False
                posicion=f_promociones.tell()
            else:
                print(Fore.LIGHTRED_EX + "Error, esta promocion ya ha sido actualizada\n" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "Codigo inexistente\n" + Fore.RESET)
    
        return fin

def controlar_promocion():
    global f_usuarios,f_promociones,ruta_promociones,posicion
    limpiar_pantalla()

    tamaño_loc=os.path.getsize(ruta_locales)
    tamaño_prom=os.path.getsize(ruta_promociones)
    if tamaño_prom!=0:
        f_promociones.seek(0)
        fila_prom=pickle.load(f_promociones)
        band1=True
        maxlen1=5
        while f_promociones.tell() <= tamaño_prom and band1==True:
            if maxlen1<len(fila_prom.textoPromo.strip(" ")):
                maxlen1=len(fila_prom.textoPromo.strip(" "))
            if f_promociones.tell() < tamaño_prom:
                fila_prom=pickle.load(f_promociones)
            else:
                band1=False

        f_locales.seek(0)
        fila_loc=pickle.load(f_locales)
        band4=True
        maxlen2=12
        while f_locales.tell() <= tamaño_loc and band4==True:
            if maxlen2<len(fila_loc.nombre.strip(" ")):
                maxlen2=len(fila_loc.nombre.strip(" "))
            if f_locales.tell() < tamaño_loc:
                fila_loc=pickle.load(f_locales)
            else:
                band4=False

        print(Fore.LIGHTGREEN_EX + "| Codigo Promo |" + Fore.RESET, " " * (((maxlen1-5)//2)+((maxlen1-5)%2)), Fore.LIGHTGREEN_EX + "Texto" + Fore.RESET, " " * ((maxlen1-5)//2) , Fore.LIGHTGREEN_EX + "|  Fecha desde  |  Fecha hasta  |            Dias           |    Estado   |  Codigo local  |" + Fore.RESET, " " * (((maxlen2-12)//2)+((maxlen2-12)%2)),Fore.LIGHTGREEN_EX + "Nombre local" + Fore.RESET, " " * ((maxlen2-12)//2), Fore.LIGHTGREEN_EX + "|" + Fore.RESET)
        f_promociones.seek(0)
        fila_prom=pickle.load(f_promociones)
        band2=True
        while f_promociones.tell() <= tamaño_prom and band2==True:
            band3=True
            codProm=int(fila_prom.codLocal)
            
            f_locales.seek(0)
            fila_loc=pickle.load(f_locales)
            while f_locales.tell() <= tamaño_loc and band3==True:
                codLoc=int(fila_loc.codigo)
                if codLoc==codProm:
                    band3=False
                if f_locales.tell() < tamaño_loc:
                    fila_loc=pickle.load(f_locales)
                else:
                    band3=False
            nom=fila_loc.nombre.strip(" ")

            for i in range(7):
                ar_desc_dias[i]=fila_prom.diasSemana[i]
            estado=fila_prom.estado.strip(" ")
            if estado=="Pendiente":
                print(Fore.LIGHTGREEN_EX + "|     " + Fore.RESET, fila_prom.codPromo, Fore.LIGHTGREEN_EX + "     |" + Fore.RESET, " " * (((maxlen1-len(fila_prom.textoPromo.strip(" ")))//2)+((maxlen1-len(fila_prom.textoPromo.strip(" ")))%2)) , fila_prom.textoPromo.strip(" "), " " * ((maxlen1-len(fila_prom.textoPromo.strip(" ")))//2) , Fore.LIGHTGREEN_EX + "| " + Fore.RESET , fila_prom.fechaDesdePromo, Fore.LIGHTGREEN_EX + "  | " + Fore.RESET , fila_prom.fechaHastaPromo, Fore.LIGHTGREEN_EX + "  |" + Fore.RESET , ar_desc_dias[0] ,Fore.LIGHTGREEN_EX + "-" + Fore.RESET, ar_desc_dias[1] ,Fore.LIGHTGREEN_EX + "-" + Fore.RESET, ar_desc_dias[2] ,Fore.LIGHTGREEN_EX + "-" + Fore.RESET, ar_desc_dias[3] ,Fore.LIGHTGREEN_EX + "-" + Fore.RESET, ar_desc_dias[4] ,Fore.LIGHTGREEN_EX + "-" + Fore.RESET, ar_desc_dias[5] ,Fore.LIGHTGREEN_EX + "-" + Fore.RESET, ar_desc_dias[6], Fore.LIGHTGREEN_EX + "| " + Fore.RESET, fila_prom.estado, Fore.LIGHTGREEN_EX + "|      " + Fore.RESET, fila_prom.codLocal, Fore.LIGHTGREEN_EX + "      |" + Fore.RESET," " * ((((maxlen2-len(nom)))//2)+((maxlen2-len(nom))%2)),nom ," " * ((maxlen2-len(nom))//2),Fore.LIGHTGREEN_EX + "|" + Fore.RESET)
            if f_promociones.tell() < tamaño_prom:
                fila_prom=pickle.load(f_promociones)
            else:
                band2=False

        cod=int(input(Fore.LIGHTCYAN_EX + "\nCodigo de la promocion que desea actualizar: \n" + Fore.RESET))
        while valid_cod_promocion(cod, tamaño_prom):
            cod=int(input(Fore.LIGHTCYAN_EX + "\nCodigo de la promocion que desea actualizar: \n" + Fore.RESET))
            
        limpiar_pantalla()

        print(Fore.LIGHTCYAN_EX + "Ingrese la opcion que desea realizar\n" + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + "1." + Fore.RESET, "Aprobar")
        print(Fore.LIGHTCYAN_EX + "2." + Fore.RESET, "Rechazar")

        opc=input(Fore.LIGHTCYAN_EX + "\nIngrese una opcion: " + Fore.RESET)
        while opc!="1" and opc!="2":
            print(Fore.LIGHTRED_EX + "\nOpcion no valida, vuelva a intentarlo" + Fore.RESET)
            opc=input(Fore.LIGHTCYAN_EX + "\nIngrese una opcion: " + Fore.RESET)

        f_promociones.seek(posicion-408)
        fila_prom=pickle.load(f_promociones)
        if opc=="1":
            fila_prom.estado="Aprobada".ljust(10)
        else:
            fila_prom.estado="Rechazada".ljust(10)
        
        f_promociones.seek(posicion-408)
        pickle.dump(fila_prom,f_promociones)
        f_promociones.flush() 
        f_promociones.seek(0)

        limpiar_pantalla()

def ReporteAdmin():
    global fecha_actual

    tamaño_prom=os.path.getsize(ruta_promociones)

    limpiar_pantalla()

    print(Fore.LIGHTMAGENTA_EX + "Ingrese un rango de fechas para generar el reporte\n" + Fore.RESET)
    verif=True
    while verif:
        try:
            fecha_des = input(Fore.LIGHTCYAN_EX + "Fecha inicial: " + Fore.RESET)
            fecha_has = input(Fore.LIGHTCYAN_EX + "Fecha final: " + Fore.RESET)
            limpiar_pantalla()
            datetime.datetime.strptime(fecha_des,'%d/%m/%Y')
            datetime.datetime.strptime(fecha_has,'%d/%m/%Y')
            verif=False
        except ValueError: 
            print(Fore.LIGHTRED_EX + "Fechas invalidas\n" + Fore.RESET)
    
    fecha_desde = datetime.datetime.strptime(fecha_des,'%d/%m/%Y').date()
    fecha_hasta = datetime.datetime.strptime(fecha_has,'%d/%m/%Y').date()
    while fecha_desde > fecha_hasta:
        limpiar_pantalla()
        print(Fore.LIGHTRED_EX + "Error, vuelva a intentarlo\n" + Fore.RESET)
        verif=True
        while verif:
            try:
                fecha_des = input(Fore.LIGHTCYAN_EX + "Fecha inicial: " + Fore.RESET)
                fecha_has = input(Fore.LIGHTCYAN_EX + "Fecha final: " + Fore.RESET)
                limpiar_pantalla()
                datetime.datetime.strptime(fecha_des,'%d/%m/%Y')
                datetime.datetime.strptime(fecha_has,'%d/%m/%Y')
                verif=False
            except ValueError: 
                print(Fore.LIGHTRED_EX + "Fechas invalidas\n" + Fore.RESET)
        fecha_desde = datetime.datetime.strptime(fecha_des,'%d/%m/%Y').date()
        fecha_hasta = datetime.datetime.strptime(fecha_has,'%d/%m/%Y').date()

    limpiar_pantalla()

    f_promociones.seek(0)
    fila_prom=pickle.load(f_promociones)
    maxlen=5
    band1=True
    while f_promociones.tell() <= tamaño_prom and band1==True:
        fechaDesdePromo = datetime.datetime.strptime(fila_prom.fechaDesdePromo,'%d/%m/%Y').date()
        fechaHastaPromo = datetime.datetime.strptime(fila_prom.fechaHastaPromo,'%d/%m/%Y').date()
        estado=fila_prom.estado.strip(" ")
        if fechaDesdePromo>=fecha_desde and fechaHastaPromo<=fecha_hasta and estado=="Aprobada":
            if maxlen<len(fila_prom.textoPromo.strip(" ")):
                maxlen=len(fila_prom.textoPromo.strip(" "))
        if f_promociones.tell() < tamaño_prom:
            fila_prom=pickle.load(f_promociones)
        else:
            band1=False

    print(Fore.LIGHTGREEN_EX + "| Codigo Promo |" + Fore.RESET, " " * (((maxlen-5)//2)+((maxlen-5)%2)), Fore.LIGHTGREEN_EX + "Texto" + Fore.RESET, " " * ((maxlen-5)//2) , Fore.LIGHTGREEN_EX + "|  Fecha desde  |  Fecha hasta  | Cantidad de usos |" + Fore.RESET)
    f_promociones.seek(0)
    fila_prom=pickle.load(f_promociones)
    band2=True
    while f_promociones.tell() <= tamaño_prom and band2==True:
        codProm=int(fila_prom.codPromo)
        cant=CantUsos(codProm, fecha_desde, fecha_hasta)
        fechaDesdePromo = datetime.datetime.strptime(fila_prom.fechaDesdePromo,'%d/%m/%Y').date()
        fechaHastaPromo = datetime.datetime.strptime(fila_prom.fechaHastaPromo,'%d/%m/%Y').date()
        estado=fila_prom.estado.strip(" ")
        if fechaDesdePromo>=fecha_desde and fechaHastaPromo<=fecha_hasta and estado=="Aprobada":
            print(Fore.LIGHTGREEN_EX + "|     " + Fore.RESET, fila_prom.codPromo, Fore.LIGHTGREEN_EX + "     |" + Fore.RESET, " " * (((maxlen-len(fila_prom.textoPromo.strip(" ")))//2)+((maxlen-len(fila_prom.textoPromo.strip(" ")))%2)) , fila_prom.textoPromo.strip(" "), " " * ((maxlen-len(fila_prom.textoPromo.strip(" ")))//2) , Fore.LIGHTGREEN_EX + "| " + Fore.RESET , fila_prom.fechaDesdePromo, Fore.LIGHTGREEN_EX + "  | " + Fore.RESET , fila_prom.fechaHastaPromo, Fore.LIGHTGREEN_EX + "  |        " + Fore.RESET , cant, Fore.LIGHTGREEN_EX + "       |" + Fore.RESET)
        if f_promociones.tell() < tamaño_prom:
            fila_prom=pickle.load(f_promociones)
        else:
            band2=False
    
    input()
    limpiar_pantalla()
    
def BusqDesc():
    global fecha_actual
    
    limpiar_pantalla()

    cod_local_des=convertir_n(int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local del que desea encontrar un descuento: " + Fore.RESET)))

    while val_datos_local(cod_local_des):
            print(Fore.LIGHTRED_EX + "\nEl codigo no pertenece a ningun local.")
            cod_local_des=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo del local del que desea encontrar un descuento: " + Fore.RESET))
    
    limpiar_pantalla()
    
    verif=True
    while verif:
        try:
            fechaDesc = input(Fore.LIGHTCYAN_EX + "Ingresa la fecha en la que desea buscar un descuento (DD/MM/AAAA): " + Fore.RESET)
            datetime.datetime.strptime(fechaDesc,'%d/%m/%Y')
            verif=False
        except ValueError:
            print(Fore.LIGHTRED_EX + "Fecha invalida" + Fore.RESET)
    fechaDesc=datetime.datetime.strptime(fechaDesc,'%d/%m/%Y').date()
    while fechaDesc < fecha_actual:
        verif=True
        while verif:
            try:
                fechaDesc = input(Fore.LIGHTCYAN_EX + "Ingresa la fecha en la que desea buscar un descuento (DD/MM/AAAA): " + Fore.RESET)
                datetime.datetime.strptime(fechaDesc,'%d/%m/%Y')
                verif=False
            except ValueError:
                print(Fore.LIGHTRED_EX + "Fecha invalida" + Fore.RESET)
        fechaDesc=datetime.datetime.strptime(fechaDesc,'%d/%m/%Y').date()

    limpiar_pantalla()

    tamaño=os.path.getsize(ruta_promociones)
    if tamaño!=0:

        f_promociones.seek(0)
        fila_prom=pickle.load(f_promociones)
        maxlen=5
        band1=True
        dia=fechaDesc.weekday()
        while f_promociones.tell() < tamaño and band1==True:
            fechaDesdePromo = datetime.datetime.strptime(fila_prom.fechaDesdePromo,'%d/%m/%Y').date()
            fechaHastaPromo = datetime.datetime.strptime(fila_prom.fechaHastaPromo,'%d/%m/%Y').date()
            if fechaDesc >= fechaDesdePromo and fechaDesc <= fechaHastaPromo and fila_prom.diasSemana[dia]==1:
                if maxlen<len(fila_prom.textoPromo.strip(" ")):
                    maxlen=len(fila_prom.textoPromo.strip(" "))
            if f_promociones.tell() < tamaño:
                fila_prom=pickle.load(f_promociones)
            else:
                band1=False
        print(Fore.LIGHTGREEN_EX + "| Codigo Promo |" + Fore.RESET, " " * (((maxlen-5)//2)+((maxlen-5)%2)), Fore.LIGHTGREEN_EX + "Texto" + Fore.RESET, " " * ((maxlen-5)//2) , Fore.LIGHTGREEN_EX + "|  Fecha desde  |  Fecha hasta  |" + Fore.RESET)
        
        band=True
        f_promociones.seek(0)
        fila_prom=pickle.load(f_promociones)
        while f_promociones.tell() <= tamaño and band==True:
            estado=fila_prom.estado.strip(" ")
            if cod_local_des==fila_prom.codLocal and estado=="Aprobada":
                fechaDesdePromo = datetime.datetime.strptime(fila_prom.fechaDesdePromo,'%d/%m/%Y').date()
                fechaHastaPromo = datetime.datetime.strptime(fila_prom.fechaHastaPromo,'%d/%m/%Y').date()
                if fechaDesc >= fechaDesdePromo and fechaDesc <= fechaHastaPromo and fila_prom.diasSemana[dia]==1:
                    print(Fore.LIGHTGREEN_EX + "|     " + Fore.RESET, fila_prom.codPromo, Fore.LIGHTGREEN_EX + "     |" + Fore.RESET, " " * (((maxlen-len(fila_prom.textoPromo.strip(" ")))//2)+((maxlen-len(fila_prom.textoPromo.strip(" ")))%2)) , fila_prom.textoPromo.strip(" "), " " * ((maxlen-len(fila_prom.textoPromo.strip(" ")))//2) , Fore.LIGHTGREEN_EX + "| " + Fore.RESET , fila_prom.fechaDesdePromo, Fore.LIGHTGREEN_EX + "  | " + Fore.RESET , fila_prom.fechaHastaPromo, Fore.LIGHTGREEN_EX + "  |")
            if f_promociones.tell() < tamaño:
                fila_prom=pickle.load(f_promociones)
            else:
                band=False
        input()
    limpiar_pantalla()

def SolDesc():
    global fecha_actual

    limpiar_pantalla()

    tamaño_usoProm=os.path.getsize(ruta_usoPromociones)
    f_usoPromociones.seek(tamaño_usoProm)
    fila_usoProm=UsoPromocion()
    
    cod=int(input(Fore.LIGHTCYAN_EX + "Codigo de la promocion que quiere utilizar: " + Fore.RESET))
    verif=val_cod_prom(cod)
    while verif==True:
        print(Fore.LIGHTYELLOW_EX + "\nVuelva a intentarlo\n" + Fore.RESET)
        cod=int(input(Fore.LIGHTCYAN_EX + "Codigo de la promocion que quiere utilizar: " + Fore.RESET))
        verif=val_cod_prom(cod)
    
    codCliente=busqUsuarioActual()
    
    fila_usoProm.codCliente=convertir_n(codCliente)
    fila_usoProm.codPromo=convertir_n(cod)
    fila_usoProm.fechaUsoPromo=fecha_actual.strftime('%d/%m/%Y')

    guardado_usoPromociones(fila_usoProm)

    limpiar_pantalla()

def CrearDesc():
    global fecha_actual, ar_base, ar_codigos, ar_locales_cod, cantidadLoc, correo

    mostrar_prom()

    tamaño_prom=os.path.getsize(ruta_promociones)
    f_promociones.seek(tamaño_prom)
    fila_prom=Promocion()

    limpiar_pantalla()
    cod_local=int(input(Fore.LIGHTCYAN_EX + "Ingrese el codigo de local al cual desea aplicar la oferta: " + Fore.RESET))
    verif=val_cod_local(cod_local)
    while verif==True:
        print(Fore.LIGHTRED_EX + "Error, vuelva a intentarlo" + Fore.RESET)
        cod_local=int(input(Fore.LIGHTCYAN_EX + "\nIngrese el codigo de local al cual desea aplicar la oferta: " + Fore.RESET))
        verif=val_cod_local(cod_local)

    cod_prom=CantProm()

    limpiar_pantalla()
    desc = input(Fore.LIGHTCYAN_EX + "Texto descriptivo de la oferta: " + Fore.RESET).ljust(200)
    
    limpiar_pantalla()
    verif=True
    while verif:
        try:
            fecha_des = input(Fore.LIGHTCYAN_EX + "Fecha cuando comienza el descuento: " + Fore.RESET)
            fecha_has = input(Fore.LIGHTCYAN_EX + "Fecha cuando termina el descuento: " + Fore.RESET)
            limpiar_pantalla()
            datetime.datetime.strptime(fecha_des,'%d/%m/%Y')
            datetime.datetime.strptime(fecha_has,'%d/%m/%Y')
            verif=False
        except ValueError: 
            print(Fore.LIGHTRED_EX + "Fechas invalidas\n" + Fore.RESET)
    
    fecha_desde = datetime.datetime.strptime(fecha_des,'%d/%m/%Y').date()
    fecha_hasta = datetime.datetime.strptime(fecha_has,'%d/%m/%Y').date()
    while fecha_desde > fecha_hasta or fecha_desde < fecha_actual:
        limpiar_pantalla()
        print(Fore.LIGHTRED_EX + "Error, vuelva a intentarlo\n" + Fore.RESET)
        verif=True
        while verif:
            try:
                fecha_des = input(Fore.LIGHTCYAN_EX + "Fecha cuando comienza el descuento: " + Fore.RESET)
                fecha_has = input(Fore.LIGHTCYAN_EX + "Fecha cuando termina el descuento: " + Fore.RESET)
                limpiar_pantalla()
                datetime.datetime.strptime(fecha_des,'%d/%m/%Y')
                datetime.datetime.strptime(fecha_has,'%d/%m/%Y')
                verif=False
            except ValueError: 
                print(Fore.LIGHTRED_EX + "Fechas invalidas\n" + Fore.RESET)
        fecha_desde = datetime.datetime.strptime(fecha_des,'%d/%m/%Y').date()
        fecha_hasta = datetime.datetime.strptime(fecha_has,'%d/%m/%Y').date()
    
    dia=0
    while dia < 7:
        limpiar_pantalla()
        print(Fore.LIGHTMAGENTA_EX + "Dias de la semana que estara vigente el descuento\n" + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + ar_dias_semana[dia] + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + "\n¿Se encuentra vigente?" + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + "1." + Fore.RESET + " Si")
        print(Fore.LIGHTCYAN_EX + "0." + Fore.RESET + " No")
        fila_prom.diasSemana[dia]=int(input())
        while fila_prom.diasSemana[dia]!=1 and fila_prom.diasSemana[dia]!=0:
            print(Fore.LIGHTYELLOW_EX + "\nError, vuelva a intentarlo\n" + Fore.RESET)
            fila_prom.diasSemana[dia]=int(input())
        dia=dia+1

    fila_prom.codPromo=convertir_n(cod_prom)
    fila_prom.textoPromo=desc
    fila_prom.fechaDesdePromo=fecha_desde.strftime('%d/%m/%Y')
    fila_prom.fechaHastaPromo=fecha_hasta.strftime('%d/%m/%Y')
    fila_prom.estado=str("Pendiente").ljust(10)
    fila_prom.codLocal=convertir_n(cod_local)

    guardado_promociones(fila_prom)

    limpiar_pantalla()

def ReporteDueño():
    global fecha_actual

    f_locales.seek(0)
    tamaño_loc=os.path.getsize(ruta_locales)

    tamaño_prom=os.path.getsize(ruta_promociones)

    limpiar_pantalla()

    print(Fore.LIGHTMAGENTA_EX + "Ingrese un rango de fechas para generar el reporte\n" + Fore.RESET)
    verif=True
    while verif:
        try:
            fecha_des = input(Fore.LIGHTCYAN_EX + "Fecha inicial: " + Fore.RESET)
            fecha_has = input(Fore.LIGHTCYAN_EX + "Fecha final: " + Fore.RESET)
            limpiar_pantalla()
            datetime.datetime.strptime(fecha_des,'%d/%m/%Y')
            datetime.datetime.strptime(fecha_has,'%d/%m/%Y')
            verif=False
        except ValueError: 
            print(Fore.LIGHTRED_EX + "Fechas invalidas\n" + Fore.RESET)
    
    fecha_desde = datetime.datetime.strptime(fecha_des,'%d/%m/%Y').date()
    fecha_hasta = datetime.datetime.strptime(fecha_has,'%d/%m/%Y').date()
    while fecha_desde > fecha_hasta:
        limpiar_pantalla()
        print(Fore.LIGHTRED_EX + "Error, vuelva a intentarlo\n" + Fore.RESET)
        verif=True
        while verif:
            try:
                fecha_des = input(Fore.LIGHTCYAN_EX + "Fecha inicial: " + Fore.RESET)
                fecha_has = input(Fore.LIGHTCYAN_EX + "Fecha final: " + Fore.RESET)
                limpiar_pantalla()
                datetime.datetime.strptime(fecha_des,'%d/%m/%Y')
                datetime.datetime.strptime(fecha_has,'%d/%m/%Y')
                verif=False
            except ValueError: 
                print(Fore.LIGHTRED_EX + "Fechas invalidas\n" + Fore.RESET)
        fecha_desde = datetime.datetime.strptime(fecha_des,'%d/%m/%Y').date()
        fecha_hasta = datetime.datetime.strptime(fecha_has,'%d/%m/%Y').date()

    limpiar_pantalla()

    print(Fore.LIGHTBLUE_EX + "Titulo del Informe" + Fore.RESET)
    print("\nFecha Desde: ", fecha_desde, "   ", "Fecha Hasta: ", fecha_hasta)
    dueño=busqUsuarioActual()
    fila_loc=pickle.load(f_locales)
    band=True
    while f_locales.tell() <= tamaño_loc and band==True:
        codUsuario=int(fila_loc.codUsuario)
        if dueño==codUsuario:
            cod_loc=int(fila_loc.codigo)
            nom=fila_loc.nombre

            f_promociones.seek(0)
            fila_prom=pickle.load(f_promociones)
            maxlen=5
            band1=True
            while f_promociones.tell() <= tamaño_prom and band1==True:
                cod_loc2=int(fila_prom.codLocal)
                fechaDesdePromo = datetime.datetime.strptime(fila_prom.fechaDesdePromo,'%d/%m/%Y').date()
                fechaHastaPromo = datetime.datetime.strptime(fila_prom.fechaHastaPromo,'%d/%m/%Y').date()
                estado=fila_prom.estado.strip(" ")
                if cod_loc==cod_loc2 and fechaDesdePromo>=fecha_desde and fechaHastaPromo<=fecha_hasta and estado=="Aprobada":
                    if maxlen<len(fila_prom.textoPromo.strip(" ")):
                        maxlen=len(fila_prom.textoPromo.strip(" "))
                if f_promociones.tell() < tamaño_prom:
                    fila_prom=pickle.load(f_promociones)
                else: 
                    band1=False

            print(Fore.LIGHTCYAN_EX + "\nLocal" + Fore.RESET, cod_loc, Fore.LIGHTCYAN_EX + ":" + Fore.RESET, nom, "\n")
            print(Fore.LIGHTGREEN_EX + "| Codigo Promo |" + Fore.RESET, " " * (((maxlen-5)//2)+((maxlen-5)%2)), Fore.LIGHTGREEN_EX + "Texto" + Fore.RESET, " " * ((maxlen-5)//2) , Fore.LIGHTGREEN_EX + "|  Fecha desde  |  Fecha hasta  | Cantidad de usos |" + Fore.RESET)
            f_promociones.seek(0)
            fila_prom=pickle.load(f_promociones)
            band2=True
            while f_promociones.tell() <= tamaño_prom and band2==True:
                codPromo=int(fila_prom.codPromo)
                cant=CantUsos(codPromo, fecha_desde, fecha_hasta)
                cod_loc2=int(fila_prom.codLocal)
                fechaDesdePromo = datetime.datetime.strptime(fila_prom.fechaDesdePromo,'%d/%m/%Y').date()
                fechaHastaPromo = datetime.datetime.strptime(fila_prom.fechaHastaPromo,'%d/%m/%Y').date()
                estado=fila_prom.estado.strip(" ")
                if cod_loc==cod_loc2 and fechaDesdePromo>=fecha_desde and fechaHastaPromo<=fecha_hasta and estado=="Aprobada":
                    print(Fore.LIGHTGREEN_EX + "|     " + Fore.RESET, fila_prom.codPromo, Fore.LIGHTGREEN_EX + "     |" + Fore.RESET, " " * (((maxlen-len(fila_prom.textoPromo.strip(" ")))//2)+((maxlen-len(fila_prom.textoPromo.strip(" ")))%2)) , fila_prom.textoPromo.strip(" "), " " * ((maxlen-len(fila_prom.textoPromo.strip(" ")))//2) , Fore.LIGHTGREEN_EX + "| " + Fore.RESET , fila_prom.fechaDesdePromo, Fore.LIGHTGREEN_EX + "  | " + Fore.RESET , fila_prom.fechaHastaPromo, Fore.LIGHTGREEN_EX + "  |        " + Fore.RESET , cant, Fore.LIGHTGREEN_EX + "       |" + Fore.RESET)
                if f_promociones.tell() < tamaño_prom:
                    fila_prom=pickle.load(f_promociones)
                else:
                    band2=False
        if f_locales.tell() < tamaño_loc:
            fila_loc=pickle.load(f_locales)
        else:
            band=False
    
    input()
    limpiar_pantalla()

#----------------------------------------------        
def menu_local(): 
    global menu,ar_locales
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
                carga_locales()
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
                DiagramacionChapin()
            case "b":
                DiagramacionChapin()
            case "c":
                DiagramacionChapin()
            case "d":
                DiagramacionChapin()
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

    limpiar_pantalla()
    nuevo_usuario=Usuario()
    nuevo_usuario.correo=input(Fore.LIGHTCYAN_EX + "Ingrese el correo: " + Fore.RESET).ljust(100)


    while verifNombre_n(nuevo_usuario.correo.rstrip(" "),"correo"):
        print("error")
        nuevo_usuario.correo=input(Fore.LIGHTCYAN_EX + "Ingrese el correo: " + Fore.RESET).ljust(100)
    
    nuevo_usuario.clave=getpass.getpass(Fore.LIGHTCYAN_EX + "Ingrese la clave: " + Fore.RESET)
    
    limpiar_pantalla()

    while nuevo_usuario.clave=="":
        nuevo_usuario.clave=getpass.getpass(Fore.LIGHTCYAN_EX + "Ingrese la clave: " + Fore.RESET)

    nuevo_usuario.clave=nuevo_usuario.clave.ljust(8)
    if tipo=="cli":
        nuevo_usuario.tipo="cliente".ljust(20)
    else:
        nuevo_usuario.tipo="Dueno de local".ljust(20)
    cod_usuario+=1
    
    nuevo_usuario.codigo=convertir_n(cod_usuario)

    ultima_fila()
    
    pickle.dump(nuevo_usuario,f_usuarios)
    f_usuarios.flush()
    os.fsync(f_usuarios.fileno())


def verifNombre_n(nombre,campo):
    global tipo_usuario,f_usuarios,fila_usuarios,val_clave

    valid=False
    tamaño=os.path.getsize(ruta_usuarios)
    f_locales.seek(0)
    while f_usuarios.tell() < tamaño:
        fila_usuarios=pickle.load(f_usuarios)
        
        match campo:
            case "correo":
                if fila_usuarios.correo.rstrip(" ")==nombre:
                    valid=True
                    tipo_usuario=fila_usuarios.tipo

                    val_clave=fila_usuarios.clave.rstrip(" ")
                    f_usuarios.seek(tamaño)
            case "codigo":
                if fila_usuarios.codigo.rstrip(" ")==nombre:
                    valid=True
                    f_usuarios.seek(tamaño)
  
    f_usuarios.seek(0)

    return valid

def control_admin():
    global tamaño_usuarios,fila_usuarios,cod_usuario

    if tamaño_usuarios==0:
        fila_usuarios.codigo="01"
        fila_usuarios.correo="admin@shopping.com".ljust(100)
        fila_usuarios.clave="12345".ljust(8)
        fila_usuarios.tipo="administrador".ljust(20)

        pickle.dump(fila_usuarios,f_usuarios)
        cod_usuario+=1
        f_usuarios.flush()



def ultimo_cod(archivo,tamaño,tipo):

    mayor=0
    if tamaño==0:
        return mayor
    else:
       match tipo:
            case "usuario":
                fila=pickle.load(archivo)
                archivo.seek(tamaño-archivo.tell())
                fila=pickle.load(archivo)
                mayor=int(fila.codigo)
            case "local":
                while archivo.tell()<tamaño:
                    fila=pickle.load(archivo)

                    if fila.estado=="A":
                        operar_contadores(fila.rubro.rstrip(" "),"aumentar")
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
            claveUsuario=getpass.getpass(Style.BRIGHT + Fore.CYAN + "Ingrese la clave: " + Fore.RESET)
            while q and  claveUsuario!=val_clave:
                    intentos-=1
                    print(Style.BRIGHT + Fore.RED + "Clave incorrecta")
                    if intentos!=0:
                        print(Fore.YELLOW + "\nIntentos restantes: " + Fore.RESET, intentos, "\n")
                        claveUsuario=getpass.getpass(Style.BRIGHT + Fore.CYAN + "Ingrese la clave: " + Fore.RESET)
                    else:
                        print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")
                        q=False
            
            if claveUsuario==val_clave:
                chequeo2=True

            if chequeo2:
                limpiar_pantalla()
                print(Style.BRIGHT + Fore.GREEN + "Ingreso exitoso\n")
                intentos=0 
                
                match tipo_usuario.rstrip(" "):
                    case "administrador":
                        menuAdmin()
                    case "Dueno de local":
                        menuDueño()
                    case "cliente":
                        menuCliente()

        else:
            limpiar_pantalla()
            intentos-=1
            print(Style.BRIGHT + Fore.RED + "Usuario inexistente" + Fore.RESET)
            if intentos!=0:
                print(Fore.YELLOW + "\nIntentos restantes: " + Fore.RESET, intentos, "\n")
                nombreUsuario=input(Style.BRIGHT + Fore.CYAN + "Ingrese el usuario: " + Fore.RESET)
            else: 
                print(Style.BRIGHT + Fore.BLUE + "\nSALIENDO DEL PROGRAMA\n")

def ini():

    fin=True
    while fin:

        print_menus("inicio")
        accion=val_opciones(["1","2","3"],2,"\nOpcion no valida","\n Por favor ingrese una opcion válida: ")

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
control_admin()
cod_local=ultimo_cod(f_locales,tamaño_locales,"local")
ini()

f_locales.close()
f_usuarios.close()
f_promociones.close()
f_usoPromociones.close()