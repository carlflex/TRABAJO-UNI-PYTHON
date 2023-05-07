import getpass

#Variables globales
admin="admin@shopping.com"
clave="12345"
strike=2

count_indumentaria=0
count_perfumeria=0
count_comida=0
rubro_menor=""
rubro_mayor=""
mayor=0
menor=0
limit=2

#Funcion de construccion
def coming_soon():
    print("\n---------------------")
    print("EN CONSTRUCCION")
    print("---------------------\n")

#Funcion del menu principal
def menuMain():

   end=True
   while end:
        print("\n---------------------")
        print("1. Gestion de locales")
        print("2. Crear cuentas de dueños locales")
        print("3. Aprobar / Denegar solicitud de descuento")
        print("4. Gestion de Novedades")
        print("5. Reporte de utilización de descuentos")
        print("0. Salir")
        print("---------------------\n")
        
        action= input("Ingrese una opcion: ")
        while ((action!="1") and (action!="2") and (action!="3") and (action!="4") and (action!="5") and (action!="0")):
            print("Opcion no valida")
            action= input("Ingrese una opcion: ")

        match action:
            case "1":
                menu_local()
            case "2":
                coming_soon()
            case "3":
                coming_soon()
            case "4":
                menu_novedades()
            case "5":
                coming_soon()
            case "0":
                end=False
                print("SALIENDO DEL SCRIPT")

def CreacionLocal():

    global count_perfumeria,count_indumentaria,count_comida,rubro_mayor,rubro_menor,mayor,menor,limit
    
    nombreLocal= input("Ingrese el nombre: ")
    ubicacionLocal=input("Ingrese la ubicacion: ")
    rubroLocal=input("Ingrese el rubro: ")
    print("-----------------------------------\n")

    while(rubroLocal!="indumentaria") and (rubroLocal!="comida") and (rubroLocal!="perfumeria"):
        print("El rubro no existe, tiene estas opciones: indumentaria, perfumeria, comida")
        rubroLocal=input("Ingrese el rubro: ")
                    
    match rubroLocal:
        case "indumentaria":
            count_indumentaria+=1
        case "comida":
            count_comida+=1
        case "perfumeria":
            count_perfumeria+=1
                
    if (count_comida > count_perfumeria) and (count_comida > count_indumentaria):
        mayor=count_comida
        rubro_mayor="comida"
    elif (count_perfumeria > count_comida) and (count_perfumeria > count_indumentaria):
        mayor=count_perfumeria
        rubro_mayor="perfumeria"
    elif (count_indumentaria > count_comida) and (count_indumentaria > count_perfumeria):
        mayor=count_indumentaria
        rubro_mayor="indumentaria"

    if (count_comida <= count_perfumeria) and (count_comida <= count_indumentaria):
        menor=count_comida
        rubro_menor="comida"
    elif (count_perfumeria <= count_comida) and (count_perfumeria <= count_indumentaria):
        menor=count_perfumeria
        rubro_menor="perfumeria"
    elif (count_indumentaria <= count_comida) and (count_indumentaria <= count_perfumeria):
        menor=count_indumentaria
        rubro_menor="indumentaria"
                
    print("---------------------------")
    print(f"Se a creado con exito el local {nombreLocal} en la ubicacion {ubicacionLocal}")
    print("---------------------------")

    if (count_indumentaria != count_comida) or (count_indumentaria != count_perfumeria) or (count_comida != count_perfumeria):
        print("Rubro con mas locales")
        print(f"El rubro de {rubro_mayor}, con un total de: {mayor} locales") 
        print("---------------------------")
        print("Rubro con menos locales")
        print(f"El rubro de {rubro_menor}, con un total de: {menor} locales") 
        print("---------------------------\n")
    else:
        print(f"Los rubros tienen la misma cantidad de locales, con {count_indumentaria}")   

    limit-=1
    print(f"Espacio disponibles para establecimientos: {limit} ") 

def limit_local():
    global limit

    if limit != 0:
        CreacionLocal()
    else:
        print("--------------------------------")
        print("No hay espacio para mas locales")
        print("--------------------------------")

#Funcion del menu de locales           
def menu_local(): 
    end=True
    while end:
        print("---------------------------")
        print("GESTION DE LOCALES")
        print("---------------------------\n")

        print("a) Crear locales")
        print("b) Modificar local")
        print("c) Eliminar locales")
        print("d) Volver")

        action= input("Ingrese una opcion: ")
        while ((action!="a") and (action!="b") and (action!="c") and (action!="d")):
            print("Opcion no valida")
            action= input("Ingrese una opcion: ")

        match action:
            case "a":
                limit_local()
            case "b":
                coming_soon()
                
            case "c":
                coming_soon()
                
            case "d":
                end=False

#Funcion del menu de novedades
def menu_novedades():

    end=True
    
    while end:
        print("\n---------------------------")
        print("GESTION DE NOVEDADES")
        print("---------------------------")

        print("a) Crear novedades")
        print("b) Modificar novedad")
        print("c) Eliminar novedad")
        print("d) Ver reporte de novedades")
        print("e) Volver")

        action= input("Ingrese una opcion: ")
        while ((action!="a") and (action!="b") and (action!="c") and (action!="d") and (action!="e")):
            print("Opcion no valida")
            action=input("Ingrese una opcion: ")

        match action:
            case "a":
                coming_soon()
                
            case "b":
                coming_soon()
                
            case "c":
                coming_soon()
                
            case "d":
                coming_soon()
                
            case "e":
                end=False

#Funcion de inicio del programa
def failLogin():
    global strike,nombreUsuario,claveUsuario
    
    chek=False
    while(strike!=0):
        print(strike, "Intentos")
        print("-----------------------------------------")
        nombreUsuario=input("Ingrese el usuario: ")
        claveUsuario=getpass.getpass("Ingrese la contraseña: ")
        print("-----------------------------------------")
        if (nombreUsuario==admin) and (claveUsuario==clave):
            print("Ingreso exitoso")
            print("-----------------------------------------\n")
            strike=0
            chek=True
            menuMain()
        else:
            print("Usuario o contraseña incorrecto")
            print("-----------------------------------------")
            strike-=1

    if  not chek:
        print("Ya no se permiten mas intentos")
        print("-----------------------------------------\n")
  
        

#Programa Principal
nombreUsuario=input("Ingrese el usuario: ")
claveUsuario=getpass.getpass("Ingrese la clave: ")
print("-----------------------------------------\n")

if (nombreUsuario==admin) and (claveUsuario==clave):
    print("Bienvenido")
    menuMain()
else:
    print("Usuario o contraseña incorrecto")
    print("-----------------------------------------\n") 
    failLogin()