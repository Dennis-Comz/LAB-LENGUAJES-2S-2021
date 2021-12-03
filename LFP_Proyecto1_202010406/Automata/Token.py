
class Token:
    lexemaVal = ''
    tipo = 0
    fila = 0
    columna = 0
    
    PALABRA_RESERVADA = 1
    CADENA = 2
    NUMERO = 3
    SIGNO = 4
    BOOLEAN = 5
    HEXADECIMAL = 6
    FILTRO = 7
    DESCONOCIDO = 8
    FIN = 9

    def __init__(self, lexema, tipo, fila, columna):
        self.lexemaVal = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexemaVal

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.PALABRA_RESERVADA:
            return 'PALABRA_RESERVADA'
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.SIGNO:
            return 'SIGNO'
        elif self.tipo == self.BOOLEAN:
            return 'BOOLEANO'
        elif self.tipo == self.HEXADECIMAL:
            return 'HEXADECIMAL'
        elif self.tipo == self.FILTRO:
            return 'FILTROS'
        elif self.tipo == self.DESCONOCIDO:
            return 'DESCONOCIDO'
        elif self.tipo == self.FIN:
            return 'FIN'