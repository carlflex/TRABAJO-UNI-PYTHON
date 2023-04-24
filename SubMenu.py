from coming_soon import coming_soon


def menu_local():
    print("---------------------------")
    print("GESTION DE LOCALES")
    print("---------------------------\n")

    print("a) Crear locales")
    print("b) Modificar local")
    print("c) Crear locales")
    print("d) volver")

    action= input("Ingrese una opcion: ")

    match action.lower():
        case "a":

            count_indumentaria=0
            count_perfumeria=0
            count_comida=0

            mayor=None
            menor=None
            rubro_menor=None
            rubro_mayor=None

            name_local= input("Ingrese el nombre: ")
            ubi_local=input("Ingrese la ubicacion: ")
            rubro_local= input("Ingrese el rubro: ")
            print("-----------------------------------\n")
            

            if not rubro_local in ["indumentaria","comida","perfumeria"]:
                print("El rubro no existe tiene estas opciones: ")
            else:
                
                if rubro_local == "comida":
                    count_comida+=1
                elif rubro_local == "perfumeria":
                    count_perfumeria+=1
                elif rubro_local== "indumentaria":
                    count_indumentaria+=1
            
                if (count_comida > count_perfumeria) and (count_comida>count_indumentaria):
                    mayor=count_comida
                    rubro_mayor="comida"
                elif (count_perfumeria > count_comida) and (count_perfumeria>count_indumentaria):
                    mayor=count_perfumeria
                    rubro_mayor="perfumeria"
                elif (count_indumentaria > count_comida) and (count_indumentaria>count_perfumeria):
                    mayor=count_indumentaria
                    rubro_mayor="indumentaria"
            
            
            
            print("---------------------------")
            print("Rubro con mayores locales")
            print(f"El rubro de {rubro_mayor}, con un total de: {mayor} locales") 
            print("---------------------------\n")

            from menuMain import menuMain
            menuMain()

        case "b":
            coming_soon()
        case "c":
            coming_soon()
        case "d":
            from menuMain import menuMain
            menuMain()