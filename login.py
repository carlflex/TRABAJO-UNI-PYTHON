import getpass

#global variable
admin="admin@shopping.com"
contraseña="12345"
strike=3

count_indumentaria=0
count_perfumeria=0
count_comida=0
rubro_menor=""
rubro_mayor=""
mayor=0
menor=0
#-------------------------
def coming_soon():
    print("\n---------------------")
    print("EN CONSTRUCCION")
    print("---------------------\n")
    

def menuMain():

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
            menuMain()
        case "3":
            coming_soon()
            menuMain()
        case "4":
            menu_novedades()
        case "5":
            coming_soon()
            menuMain()
        case "0":
            print("SALIENDO DEL SCRIPT")
            
def menu_local():

    global count_perfumeria,count_indumentaria,count_comida,rubro_mayor,rubro_menor,mayor,menor
    print("---------------------------")
    print("GESTION DE LOCALES")
    print("---------------------------\n")

    print("a) Crear locales")
    print("b) Modificar local")
    print("c) Crear locales")
    print("d) Volver")

    action= input("Ingrese una opcion: ")
    while action not in ["a","b","c","d"]:
        print("Opcion no valida")
        action= input("Ingrese una opcion: ")

    match action.lower():
        case "a":
            name_local= input("Ingrese el nombre: ")
            ubi_local=input("Ingrese la ubicacion: ")
            rubro_local= input("Ingrese el rubro: ")
            print("-----------------------------------\n")

            if not rubro_local in ["indumentaria","comida","perfumeria"]:
                print("El rubro no existe tiene estas opciones: ")
            else:
                
                match rubro_local:
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
            print(f"Se a creado con exito el local {name_local} en la ubicacion {ubi_local}")
            print("---------------------------")

            if (count_indumentaria != count_comida) or (count_indumentaria != count_perfumeria) or (count_comida != count_perfumeria):
                print("Rubro con mas locales")
                print(f"El rubro de {rubro_mayor}, con un total de: {mayor} locales") 
                print("---------------------------")
                print("Rubro con menos locales")
                print(f"El rubro de {rubro_menor}, con un total de: {menor} locales") 
                print("---------------------------\n")
            else:
                print("Los rubros tienen la misma cantidad de locales")

            menuMain()

        case "b":
            coming_soon()
            menu_local()
        case "c":
            coming_soon()
            menu_local()
        case "d":
            menuMain()

def menu_novedades():
    print("\n---------------------------")
    print("GESTION DE NOVEDADES")
    print("---------------------------")

    print("a) Crear novedades")
    print("b) Modificar novedad")
    print("c) Crear novedad")
    print("d) Ver reporte de novedades")
    print("e) Volver")

    action= input("Ingrese una opcion: ")
    while action not in ["a","b","c","d","e"]:
        print("Opcion no valida")
        action= input("Ingrese una opcion: ")

    match action.lower():
        case "a":
            coming_soon()
            menu_novedades()
        case "b":
            coming_soon()
            menu_novedades()
        case "c":
            coming_soon()
            menu_novedades()
        case "d":
            coming_soon()
            menu_novedades()
        case "e":
            menuMain()

def failLogin():
    global strike,user,user_password
    
    chek=False
    while(strike!=0):
        print(strike, "Intentos")
        print("-----------------------------------------")
        user=input("Ingrese el usuario: ")
        user_password=getpass.getpass("Ingrese la contraseña: ")
        print("-----------------------------------------\n")
        if (admin==user) and (contraseña==user_password):
            print("Ingreso exitoso")
            print("-----------------------------------------\n")
            strike=0
            chek=True
        else:
            print("Usuario o contraseña incorrecto")
            print("-----------------------------------------")
            strike-=1

    if  not chek:
        print("Ya no se permiten mas intentos")
        print("-----------------------------------------\n")
    else:
        menuMain()

#Programa Principal
user=input("Ingrese el usuario: ")
user_password=getpass.getpass("Ingrese la contraseña: ")
print("-----------------------------------------\n")

if (user==admin) and (user_password==contraseña):
    print("Bienvenido")
    menuMain()
else:
    print("Usuario o contraseña incorrecto")
    print("-----------------------------------------\n") 
    failLogin()