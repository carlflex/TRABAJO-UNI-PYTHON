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

            name_local= input("Ingrese el nombre: ")
            ubi_local=input("Ingrese la ubicacion: ")
            rubro_local= input("Ingrese el local: ")

            if not rubro_local in ["indumentaria","perfumería","comida"]:
                print("El rubro no exis,te tiene estas opciones: ")

                
        case "b":
            coming_soon()
        case "c":
            coming_soon()
        case "d":
            from menuMain import menuMain
            menuMain()