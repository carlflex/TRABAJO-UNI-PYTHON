from SubMenu import menu_local
from coming_soon import coming_soon


def menuMain():
    print("---------------------")
    print("1. Gestion de locales")
    print("2. Crear cuntas de dueños locales")
    print("3. Aprobar/ Denegar solicitud de descuento")
    print("4. Gestion de Novedades")
    print("5. Reporte de utilización de descuentos")
    print("0. Salir")
    print("---------------------")
    action= input("Ingrese una opcion: ")

    match action:
        case "1":
            menu_local()
        case "2":
            coming_soon()
        case "3":
            coming_soon()
        case "4":
            coming_soon()
        case "5":
            coming_soon()
        case "0":
            print("SALIENDO DEL SCRIPT")
        