class Instruccion:
    'clase abstracta'



#TIPOS DE DATO
class Tipo(Instruccion):
    def __init__(self, tipo, longitud,fila,columna):
        self.tipo = tipo
        self.longitud = longitud
        self.fila = fila
        self.columna = columna

class IdId(Instruccion):
    '''ID.ID'''
    def __init__(self, id1, id2,fila,columna):
        self.id1 = id1
        self.id2 = id2
        self.fila = fila
        self.columna = columna



        

#WHERE


#asignacion x = e
#puede venir id o id.id
class Asignacion(Instruccion):
    def __init__(self, id, expresion, fila,columna):
        self.id = id
        self.expresion = expresion
        self.fila = fila
        self.columna = columna




#SHOW DATABASE
class Show(Instruccion):
    def __init__(self, fv,fila,columna):
        self.fv = fv
        self.fila = fila
        self.columna = columna


#UPDATE


#SELECT
#-----------------------
#TIME




#COMBINACION QUERIES
class Combinacion(Instruccion):
    '''#1 union
       #2 intersect
       #3 except'''
    def __init__(self, caso, all, querie1, querie2,fila,columna):
        self.caso = caso
        self.all = all
        self.querie1 = querie1
        self.querie2 = querie2
        self.fila = fila
        self.columna = columna


 #MATH

#Trigonometrica


#Binaria

#CASE
class Case(Instruccion):
    def __init__(self, asignacion, valor,fila,columna):
        self.asignacion = asignacion
        self.valor = valor
        self.fila = fila
        self.columna = columna

class ColCase(Instruccion):
    def __init__(self, cases, id,fila,columna):
        self.cases = cases
        self.id = id
        self.fila = fila
        self.columna = columna

#TYPE
class CreateType(Instruccion):
    def __init__(self, id, lista,fila,columna):
        self.id = id
        self.lista = lista
        self.fila = fila
        self.columna = columna