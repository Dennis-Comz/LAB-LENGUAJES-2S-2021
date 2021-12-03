import os
from html2image import Html2Image
hti = Html2Image()

class Imagen:
    def __init__(self, nombre, ancho, alto, filasN, columnasM, columna, fila, pintar, hexa, filtros):
        self.nombre = nombre
        self.ancho = ancho
        self.alto = alto
        self.filasN = filasN
        self.columnasM = columnasM
        self.filasN
        self.fila = fila
        self.columna = columna
        self.pintar = pintar
        self.hexa = hexa
        self.filtros = filtros

class Pintar():
    def generarHtml(self, images):
        self.imagenes = []

        for img in images:
            html = '<table>\n'
            contador = 0
            height = int(img.alto)/int(img.filasN)
            width = int(img.ancho)/int(img.columnasM)
            nombre  = img.nombre
            contador = 0
            self.bubblesort(img.fila, img.columna, img.hexa, img.pintar)
            self.imagenes.append(nombre)
            for i in range(img.filasN):
                html += "\t<tr>\n"
                for j in range(img.columnasM):
                    if contador < len(img.columna):
                        if j != img.columna[contador]:
                            html += "\t\t<td bgcolor = \"white\" height = \"" + str(height) + "\" width = \"" + str(width) + "\"></td>\n"
                        elif j == img.columna[contador]:
                            if i == img.fila[contador] and j == img.columna[contador] and img.pintar[contador].upper() == 'TRUE':
                                html += "\t\t<td bgcolor = \"" + img.hexa[contador] + "\" height = \"" + str(height) + "\" width = \"" + str(width) + "\"></td>\n"
                                contador += 1
                            else:
                                html += "\t\t<td bgcolor = \"white\" height = \"" + str(height) + "\" width = \"" + str(width) + "\"></td>\n"
                                contador += 1
                    else:
                        html += "\t\t<td bgcolor = \"white\" height = \"" + str(height) + "\" width = \"" + str(width) + "\"></td>\n"
                        
                html += "\t</tr>\n"
            html += '</table>'
            file = open(nombre + ".html", 'w')
            file.write(html)
            file.close
            os.startfile(nombre + ".html")

    def bubblesort(self, filas, columnas, hexa, pintar):
        for n in range(len(filas) - 1, 0, -1):
            for i in range(n):
                if filas[i] > filas[i + 1]:
                    filas[i], filas[i+1] = filas[i+1], filas[i]
                    columnas[i], columnas[i+1] = columnas[i+1], columnas[i]
                    hexa[i], hexa[i+1] = hexa[i+1], hexa[i]
                    pintar[i], pintar[i+1] = pintar[i+1], pintar[i]
        self.bubbleColumnas(filas, columnas, hexa, pintar)
    
    def bubbleColumnas(self, filas,columnas, hexa, pintar):
        for n in range(len(columnas) -1 , 0, -1):
            for i in range(n):
                if filas[i] == filas[i+1] and columnas[i] > columnas[i+1]:
                    filas[i], filas[i+1] = filas[i+1], filas[i]
                    columnas[i], columnas[i+1] = columnas[i+1], columnas[i]
                    hexa[i], hexa[i+1] = hexa[i+1], hexa[i]
                    pintar[i], pintar[i+1] = pintar[i+1], pintar[i]

    
    def takeImage(self, name):
        if name in self.imagenes:
            entrada = name + '.html'
            salida =  name + '.png'
            hti.screenshot(html_file=entrada, save_as=salida)