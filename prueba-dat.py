import os
import pickle
ruta_usuarios="./db/aux.dat"

class Usuario:
    def __init__(self,cod,cor,cla,tip):
        self.codigo=cod
        self.correo=cor
        self.clave=cla
        self.tipo=tip.ljust(20)

def abrir(ruta):
    if not os.path.exists(ruta):   
        objeto = open (ruta, "w+b")   
    else:
        objeto = open (ruta, "r+b")

    return objeto

f_aux=abrir(ruta_usuarios)

fil=Usuario("01","".ljust(100),"".ljust(8),"admin".ljust(20," "))

pickle.dump(fil,f_aux)
fil=Usuario("01","".ljust(100),"".ljust(8),str("duenio de local").ljust(20," "))
pickle.dump(fil,f_aux)


f_aux.close()

print("dueño".ljust(20),"|")
print("Dueño de local".ljust(20-len("Dueño de local")),"|")