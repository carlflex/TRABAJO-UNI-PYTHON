import os
import pickle
from datetime import datetime as dt
cadena="PEPE"
cadena=cadena.ljust(50)

cad2="PEPE"
ruta_usuarios="c:\\tp3\pepe.dat\\"
def abrir(ruta):
    if not os.path.exists(ruta):   
        objeto = open (ruta, "w+b")   
    else:
        objeto = open (ruta, "r+b")

    return objeto

class Usuario:
    def __init__(self,cod,cor,cla,tip):
        self.codigo=cod
        self.correo=cor
        self.clave=cla
        self.tipo=tip

af=abrir(ruta_usuarios)


""" f=Usuario("01","admin@shopping.com".ljust(100),"12345".ljust(8),"administrador".ljust(20))

pickle.dump(f,af)

af.close()

print("04".rstrip(" ")) """

pepe=int("01")
print(f"|{pepe}")

""" f=pickle.load(af)
pepe="admin@shopping.com"


print(f.correo.rstrip(" ")==pepe) """


