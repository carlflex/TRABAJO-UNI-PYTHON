import os
import pickle

class Usuario:
    def __init__(self,codigo,correo,clave,tipo):
        self.codigo=codigo
        self.correo=correo
        self.clave=clave
        self.tipo=tipo

class Local:
    def __init__(self,codigo,codUsuario,nombre,ubicacion,rubro,estado) -> None:
        self.codigo=codigo
        self.codUsuario=codUsuario
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.rubro=rubro
        self.estado=estado

        
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
