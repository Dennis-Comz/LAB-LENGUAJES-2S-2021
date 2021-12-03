import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from Reportes import Reporte
from Automata.Analizador import Analizador
from Pintar import Imagen, Pintar

entrada = ''
lexico = Analizador()
imagesList = list()
html = Pintar()
nombres = []

class Administrador:
    def __init__(self):
        self.entrada = ''
        self.lexico = Analizador()
        self.imageList = list()
        self.html = Pintar()
        self.nombres = []

    # Funciones para procesar informacion
    def cargar(self):
        filename = askopenfilename()
        self.entrada
        if os.path.exists(filename) == True:
            self.entrada = open(filename, 'r')
            self.entrada = self.entrada.read()
            messagebox.showinfo("Exito", "Archivo encontrado: \n" + str(filename))
        else:
            messagebox.showerror("Error", "No se ha encontrado el archivo, intente de nuevo.")

    def obtenerImagenes(self):
        i, contadorArrobas = 0, 0
        nombre = ''
        ancho, alto, filas, columnas = 0,0,0,0
        pintar, fila, columna, hexadecimal, filtros = [],[],[],[],[]
        ingresarA, ingresarAT, ingresarF, ingresarC, ingresarCD, ingresarFT, final = False, False, False, False, False, False, False
        for token in self.lexico.getTokens():
            if token.getTipo() == 'CADENA':
                for letras in token.getLexema():
                    if letras != '"':
                        nombre += letras
            elif token.getLexema().upper() == 'ANCHO' or ingresarA == True:
                ingresarA = True
                if token.getTipo() == 'NUMERO':
                    ancho = int(token.getLexema())
                    ingresarA = False
                # continue
            elif token.getLexema().upper() == 'ALTO' or ingresarAT == True:
                ingresarAT = True
                if token.getTipo() == 'NUMERO':
                    alto = int(token.getLexema())
                    ingresarAT = False
                # continue
            elif token.getLexema().upper() == 'FILAS' or ingresarF == True:
                ingresarF = True
                if token.getTipo() == 'NUMERO':
                    filas = int(token.getLexema())
                    ingresarF = False
                # continue
            elif token.getLexema().upper() == 'COLUMNAS' or ingresarC == True:
                ingresarC = True
                if token.getTipo() == 'NUMERO':
                    columnas = int(token.getLexema())
                    ingresarC = False
                # continue
            elif token.getLexema().upper() == 'CELDAS' or ingresarCD == True:
                ingresarCD = True
                if token.getTipo() == 'NUMERO' and i == 0:
                    columna.append(int(token.getLexema()))
                    i = 1
                elif token.getTipo() == 'NUMERO' and i == 1:
                    fila.append(int(token.getLexema()))
                    i = 0
                elif token.getTipo() == 'BOOLEANO':
                    pintar.append(token.getLexema())
                elif token.getTipo() == 'HEXADECIMAL':
                    hexadecimal.append(token.getLexema())
                elif token.getLexema() == '}':
                    ingresarCD = False
            elif token.getLexema().upper() == 'FILTROS' or ingresarFT == True:
                ingresarFT = True
                if token.getLexema().upper() == 'MIRRORX':
                    filtros.append(token.getLexema())
                elif token.getLexema().upper() == 'MIRRORY':
                    filtros.append(token.getLexema())
                elif token.getLexema().upper() == 'DOUBLEMIRROR':
                    filtros.append(token.getLexema())
                elif token.getLexema() == ';':
                    ingresarFT = False
            elif token.getLexema() == '@' or token.getLexema() == '$':
                if token.getLexema() == '@':
                    contadorArrobas += 1
                elif token.getLexema() == '$':
                    final = True
                if contadorArrobas == 4 or final == True:
                    image = Imagen(nombre, ancho, alto, filas, columnas, columna, fila, pintar, hexadecimal, filtros)
                    self.nombres.append(nombre)
                    self.imageList.append(image)
                    i = 0
                    contadorArrobas = 0
                    nombre = ''
                    ancho, alto, filas, columnas = 0,0,0,0
                    pintar, fila, columna, hexadecimal, filtros = [],[],[],[],[]
                    ingresarA, ingresarAT, ingresarF, ingresarC, ingresarCD = False, False, False, False, False   
        html.generarHtml(self.imageList)
        print(self.nombres)

    def analizar(self):
        if self.entrada != '':
            self.lexico.lector(self.entrada)
            if self.lexico.canGenerate() == True:
                messagebox.showinfo("Exito", "Analisis terminado.")
                self.obtenerImagenes()
            else:
                messagebox.showerror("Error", "Estructura del archivo invalida, no se puede generar la imagen.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado un archivo.")

    def reportes(self):
        Reporte(self.lexico)

    def getNames(self):
        return self.nombres

    def getFiltros(self):
        return self.imageList

    def imagen(self, name):
        html.takeImage(name)
        # Pintar(imagesList)