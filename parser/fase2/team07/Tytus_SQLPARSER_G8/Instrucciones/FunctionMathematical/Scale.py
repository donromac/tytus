import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Scale(Instruccion):
    def __init__(self, valor, strGram,tipo, linea, columna,strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram,strSent)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')