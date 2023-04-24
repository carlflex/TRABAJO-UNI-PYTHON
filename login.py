from menuMain import menuMain

admin="admin@shopping.com"
contraseña="12345"

strike=3

user=input("Ingrese el Usuario: ")
user_password=input("Ingrese la contraseña: ")
print("-----------------------------------------")


def failLogin():
    global strike,user,user_password

    while(strike!=0):
        print(strike, "Intentos")
        print("-----------------------------------------")
        user=input("Ingrese el Usuario: ")
        user_password=input("Ingrese la contraseña: ")
        print("-----------------------------------------\n")
        if (admin==user) and (contraseña==user_password):
            print("Ingreso exitoso")
            print("-----------------------------------------")
            strike=0
        else:
            print("Usuario o contraseña icorrecto")
            print("-----------------------------------------")
            strike-=1


    if strike==0:
        print("Ya no se permiten mas Intentos")
        print("-----------------------------------------")
    else:
        menuMain()        
    return


if (user==admin) and (user_password==contraseña):
    print("nice")
    menuMain()
else:
    print("Usuario o contraseña icorrecto")
    print("-----------------------------------------\n") 
    failLogin()