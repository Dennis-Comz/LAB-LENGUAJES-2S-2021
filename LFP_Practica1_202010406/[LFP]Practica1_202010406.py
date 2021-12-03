import sys, os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#VARIABLES GLOBALES
cursos = list()
paramAplicados = list()
datosSinOrd = ""

#MENU INICIAL DE APLICACION
Tk().iconify()
menu = "============== Menu =============\n| 1. Cargar Archivo             |\n| 2. Mostrar Reporte en Consola |\n| 3. Exportar Reporte           |\n| 4. Salir                      |\n=================================\nQue desea realizar?"
print(menu)
option = int(input())

#CLASE CURSO QUE ALMACENA ALUMNOS POR CURSO
#==================================================
class Curso:
    def __init__(self, nombreCurso, alumnos, notas, parametros):
        self.nombreCurso = nombreCurso
        self.alumnos = alumnos
        self.notas = notas
        self.parametros = parametros
        
#FUNCION CARGAR ARCHIVOS
#==================================================
def cargarArchivo(path):
    contenido = None
    try:
        contenido = open(path)
    except:
        print("Archivo No Encontrado")
        
    if contenido != None:
        nota = []
        nombre = []
        for linea in contenido:
            linea = linea.strip()
            if not linea.startswith("<") and not linea.startswith("}"):
                nombreCurso = linea.translate({ord(i): None for i in '={'}).strip()
            elif linea.startswith("<"):
                linea = linea.translate({ord(i): None for i in '<"",>'}).strip()
                nombreNota = linea.split(';', 1)
                nombre.append(nombreNota[0].strip())
                nota.append(int(nombreNota[1].strip()))
            elif linea.startswith("}"):
                linea = linea.translate({ord(i): None for i in '} '}).strip()
                param = linea.split(',')
        cursos.append(Curso(nombreCurso, nombre, nota, param))
        print("Archivo Cargado")
                
#FUNCIONES PARA LOS PARAMETROS
#==================================================
def aplicarParametros(curso):
    datos = []
    global datosSinOrd
    print("==========================")
    print("|          CURSO         |")
    print("==========================")
    print(curso.nombreCurso)
    print("============================================")
    print("Cantidad de Estudiantes: " + str(len(curso.alumnos)))
    print("============================================")
    print("Estudiantes y Notas sin Ordenar")
    print("============================================")
    
    datosSinOrd = "<h2>Datos sin Ordenar</h2><table border=\"1\" style = \"margin-left: 44%;\"><tr><th>Alumnos</th><th>Notas</th></tr>"
    for i in range(len(curso.alumnos)):
        print(curso.alumnos[i] + " " + str(curso.notas[i]))
        if curso.notas[i] >= 61:
            color = " style=\"background-color: blue;\""
        elif curso.notas[i] < 61:
            color = " style=\"background-color: red;\""
        newRw = "<tr><td>" + curso.alumnos[i] + "</td><td " + color + ">" + str(curso.notas[i]) + "</td></tr>"
        datosSinOrd = datosSinOrd + newRw
        
    for pm in curso.parametros:
        if pm == "ASC":
            curso = ascendente(curso)
            print("=======================")
            print("Ordenados por Orden Ascendente")
            print("=======================")
            print("| ESTUDIANTES Y NOTAS |")
            print("=======================")
            for i in range(len(curso.alumnos)):
                print(curso.alumnos[i] + " " + str(curso.notas[i]))
        elif pm == "DESC":
            curso = descendente(curso)
            print("=======================")
            print("Ordenados por Orden Descendente")
            print("=======================")
            print("| ESTUDIANTES Y NOTAS |")
            print("=======================")
            for i in range(len(curso.alumnos)):
                print(curso.alumnos[i] + " " + str(curso.notas[i]))
        elif pm == "AVG":
            prom = promedio(curso.notas)
            print("======================")
            print("|    PROMEDIO        |")
            print("======================")
            print(prom)
            datos.append("Promedio: " + str(prom))
        elif pm == "MIN":
            min = minima(curso)
            print("======================")
            print("|    NOTA MINIMA     |")
            print("======================")
            print(min)
            datos.append("Nota Minima: " + str(min))
        elif pm == "MAX":
            max = maxima(curso)
            print("======================")
            print("|    NOTA MAXIMA     |")
            print("======================")
            print(max)
            datos.append("Nota Maxima: " + str(max))
        elif pm == "APR":
            apr = aprobados(curso.notas)
            print("======================")
            print("|ESTUDIANTES APROBADOS|")
            print("======================")
            print(apr)
            datos.append("Estudiantes Aprobados: " + str(apr))
        elif pm == "REP":
            rep = reprobados(curso.notas)
            print("========================")
            print("|ESTUDIANTES REPROBADOS|")
            print("========================")
            print(rep)
            datos.append("Estudiantes Reprobados: " + str(rep))
    paramAplicados.append(datos)
    
def ascendente(listado):
    for i in range(len(listado.notas)):
        for j in range(len(listado.notas) - 1):
            if listado.notas[j] > listado.notas[j+1]:
                listado.notas[j], listado.notas[j+1] = listado.notas[j+1], listado.notas[j]
                listado.alumnos[j], listado.alumnos[j+1] = listado.alumnos[j+1], listado.alumnos[j]
    return listado

def descendente(listado):
    for i in range(len(listado.notas)):
        for j in range(len(listado.notas) - 1):
            if listado.notas[j] < listado.notas[j+1]:
                listado.notas[j], listado.notas[j+1] = listado.notas[j+1], listado.notas[j]
                listado.alumnos[j], listado.alumnos[j+1] = listado.alumnos[j+1], listado.alumnos[j]
    return listado

def promedio(listado):
    sum = 0
    prom = 0
    for i in range(len(listado)):
        sum += listado[i]
    prom = int(sum/len(listado))
    return prom

def minima(listado):
    valorMin = 0
    for i in range(len(listado.notas)):
        if listado.notas[i] < listado.notas[0]:
            valorMin = listado.notas[i]
        else:
            valorMin = listado.notas[0]
    return valorMin     

def maxima(listado):
    valorMax = 0
    for i in range(len(listado.notas)):
        if listado.notas[i] > listado.notas[0]:
            valorMax = listado.notas[i]
        else:
            valorMax = listado.notas[0]
    return valorMax     

def aprobados(listado):
    aprobados = 0
    for i in range(len(listado)):
        if listado[i] >= 61:
            aprobados += 1
    return aprobados

def reprobados(listado):
    reprobados = 0
    for i in range(len(listado)):
        if listado[i] < 61:
            reprobados += 1
    return reprobados
        
#FUNCION MOSTRAR REPORTE EN CONSOLA
#==================================================
def mostrarConsola():
    print("GENERANDO REPORTE...\n")
    contador = 1
    for datos in cursos:
        print("*************************************")
        print("REPORTE No " + str(contador))
        aplicarParametros(datos)
        contador += 1
    print("\nFIN DE REPORTES")

#FUNCION EXPORTAR REPORTE
#==================================================
def exportarReporte():
    print("EXPORTANDO REPORTE...")
    contador = 0
    for dato in cursos:
        nombreArchivo = dato.nombreCurso + " Reporte.html"
        color = ""
        orden = ""
        inicio = "<html style = \"background-color: skyblue;\"><body style = \"text-align: center;\"><h1>" + dato.nombreCurso + "</h1>"
        inicio += "<h4>Parametros Aplicados: "
        
        for pm in dato.parametros:
            inicio += str(pm) + ", "
            if pm == "ASC":
                orden = "Ascendente"
            elif pm == "DESC":
                orden = "Descendente"
        inicio += "</h4>"
        inicio += "<h4>Cantidad de Alumnos: " + str(len(dato.alumnos)) + "</h4>"
        
        for pmA in paramAplicados[contador]:
            # print(pmA)
            inicio += "<p>" + str(pmA) + "</p>"
        
        tabla2 = inicio + datosSinOrd + "</table><h2>Datos ordenados " + orden + "</h2><table border=\"1\" style = \"margin-left: 44%;\"><tr><th>Alumnos</th><th>Notas</th></tr>"
        for i in range(len(dato.alumnos)):
            if dato.notas[i] >= 61:
                color = " style=\"background-color: blue;\""
            elif dato.notas[i] < 61:
                color = " style=\"background-color: red;\""
            strRw = "<tr><td>" + dato.alumnos[i] + "</td><td" + color + ">" + str(dato.notas[i]) + "</td></tr>"
            tabla2 += strRw
        tabla2 += "</table></body></html>"
        
        contenidoFinal = tabla2
        
        if os.path.exists(nombreArchivo):
            contenidoFinal = ""
        else:
            hs = open(nombreArchivo, 'w')
            hs.write(contenidoFinal)
            hs.close()
            os.startfile(nombreArchivo)
        contador += 1

#WHILE PARA COMPARAR EL INPUT Y DESPLEGAR EL MENU
while option != 4:
    if option == 1:
        filename = askopenfilename()
        cargarArchivo(filename)
    elif option == 2:
        mostrarConsola()
    elif option == 3:
        exportarReporte()
    elif option == 4:
        sys.exit()    
    print(menu)
    option = int(input())