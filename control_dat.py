import os
import pickle

ruta_usuarios="./db/usuarios.dat"

if not os.path.exists(ruta_usuarios):   
	alPiezas = open (ruta_usuarios, "w+b")   
else:
	alPiezas = open (ruta_usuarios, "r+b")
	

class Usuario:
    def __init__(self,codigo,correo,clave,tipo):
        self.codigo=codigo
        self.correo=correo
        self.clave=clave
        self.tipo=tipo
	
	    
user=Usuario(1,"admin@shopping.com","12345","administrador")


""" pickle.dump(user,alPiezas)
pickle.load(alPiezas) """
""" pickle.dump(user2,alPiezas) """


def mostrar_contenido(ruta):
    objeto = open (ruta, "r+b") 
    tamaño=os.path.getsize(ruta)

    """ print(tamaño) """
    while objeto.tell() < tamaño:

        pepe=pickle.load(objeto) #Carga el valor en un indice especifico y aumenta el indice en 1
        valores=vars(pepe) #retorna un diccionario con la clave-valor del objeto, similar al object.values de javaScript
        print("Tamaño fila", objeto.tell())
        for r1,r2 in zip(valores.keys(),valores.values()): #Recorre 2 arrays al mismo tiempo
             print(f"|| {r1}: ",r2, end=" ")
        print("")
        print("")

mostrar_contenido(ruta_usuarios)

def buscar_file(ruta,e,col):
    objeto = open (ruta, "r+b") 
    tamaño=os.path.getsize(ruta)
    pos_fila=0
    print(tamaño)
    while objeto.tell() < tamaño:
        fila=pickle.load(objeto)

        if fila.__getattribute__(col)==e:
             pos_fila=objeto.tell()
             print(objeto.tell())
             objeto.seek(tamaño)

""" buscar_file(ruta_usuarios,6,"codigo") """
""" alPiezas.seek(121)

pepe=pickle.load(alPiezas)
print(pepe) """

""" pepe=pickle.load(alPiezas)
print(pepe.__getattribute__("codigo")) """