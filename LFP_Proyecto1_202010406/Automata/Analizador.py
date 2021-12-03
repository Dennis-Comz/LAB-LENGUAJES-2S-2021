from os import path
from Automata.Token import Token

lexema = ''
tokens = []
estado = 0
fila = 1
columna = 1
generar = False

tipos = Token("lexema", -1, -1, -1)

class Analizador:
    def lector(self, entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens = []
        self.fila = 1
        self.columna = 1
        self.generar = True

        entrada += '$'
        actual = ''
        long = len(entrada)
        i = 0
        while i < long:
            actual = entrada[i]

            if self.estado == 0:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual.isdigit():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '#':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '"':
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '=':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == '{':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == '}':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == '[':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == ']':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == ',':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == ';':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == '@':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.SIGNO)
                    i += 1
                elif actual == ' ':
                    self.columna += 1
                    self.estado = 0
                    i += 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 0
                    self.columna = 1
                    i += 1
                elif actual  == '\r':
                    self.estado = 0
                    i += 1
                elif actual == '\t':
                    self.columna += 8
                    self.estado = 0
                    i += 1
                elif actual == '$' and i == long - 1:
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.FIN)
                    i += 1
                else:
                    self.lexema += actual
                    self.agregarToken(tipos.DESCONOCIDO)
                    self.columna += 1
                    self.generar = False
                    i += 1

            elif self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                else:
                    if self.palabraReservada(self.lexema):
                        self.agregarToken(tipos.PALABRA_RESERVADA)
                    elif self.booleano(self.lexema):
                        self.agregarToken(tipos.BOOLEAN)
                    elif self.filtro(self.lexema):
                        self.agregarToken(tipos.FILTRO)
                    else:
                        self.agregarToken(tipos.DESCONOCIDO)
                        self.generar = False

            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                else:
                    self.agregarToken(tipos.NUMERO)

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '"':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.CADENA)
                    i += 1

            elif self.estado == 5:
                if actual.isalpha():
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual.isdigit():
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                else:
                    self.agregarToken(tipos.HEXADECIMAL)
    
    def agregarToken(self, tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ''
        self.estado = 0
    
    def palabraReservada(self, entrada = ''):
        entrada = entrada.upper()
        valor = False
        palabras = ['TITULO', 'ANCHO', 'ALTO', 'FILAS', 'COLUMNAS', 'CELDAS', 'FILTROS']

        if entrada in palabras:
            valor = True
        return valor

    def filtro(self, entrada = ''):
        entrada = entrada.upper()
        valor = False
        filtros = ['MIRRORX', 'MIRRORY', 'DOUBLEMIRROR']
        if entrada in filtros:
            valor = True
        return valor

    def booleano(self, entrada = ''):
        entrada = entrada.upper()
        valor = False
        booleanos = ['TRUE', 'FALSE']
        if entrada in booleanos:
            valor = True
        return valor

    def canGenerate(self):
        if self.generar == True:
            return True
        else:
            return False

    def getTokens(self):
        return self.tokens
        
    def imprimir(self):
        print("=== LECTURA DE TOKENS VALIDOS ===")
        for i in self.tokens:
            if i.tipo != tipos.DESCONOCIDO:
                print(i.getLexema(), " --> ", i.getFila(), ' --> ', i.getColumna(), ' --> ', i.getTipo())
        print("=== FIN DE LECTURA DE TOKENS ===\n")
        print("=== LECTURA DE TOKENS CON ERROR ===")
        for i in self.tokens:
            if i.tipo == tipos.DESCONOCIDO:
                print(i.getLexema(), ' --> ', i.getFila(), ' --> ', i.getColumna(), ' --> Error Lexico')
        print("=== FIN DE LECTURA DE TOKENS CON ERROR ===")