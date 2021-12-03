from tkinter import *
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
from tkinter.ttk import Combobox
from Admin import *

# INTERFAZ DE USUARIO
class main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bitxelart")
        self.root.geometry("1000x600")
        self.Admin = Administrador()
        self.gui()


    def analizar(self):
        self.Admin.analizar()
        self.values = self.Admin.getNames()
        self.valorSeleccionado = StringVar()
        self.imgCombo = Combobox(self.root, values=self.values, textvariable=self.valorSeleccionado, justify='center', width=12, state='readonly').place(x=540, y=20)
        self.btnImagen = Button(self.root, text="Generar Imagen", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command=self.send).place(x=700, y=20)

    def send(self):
        self.nombre = self.valorSeleccionado.get()
        self.Admin.imagen(self.nombre)
    
    def drawImage(self, type):
        imagenes = self.Admin.getFiltros()
        for img in imagenes:
            if self.nombre == img.nombre:
                self.image = PIL.Image.open(self.nombre + '.png')
                if type == 'original': 
                    self.image = PIL.ImageTk.PhotoImage(self.image)
                    self.lbImage = Label(self.root, image=self.image).place(x=400, y=170)
                elif type.upper() == 'MIRRORX' and type.upper() in img.filtros:
                    self.flippedimage = PIL.ImageOps.mirror(self.image)
                    self.flippedimage = self.flippedimage.crop((1530,0,1920,345))
                    self.rgbflipped = self.flippedimage.convert('RGB')
                    self.rgbflipped.save('mirrorx' + self.nombre + '.png', quality=95)
                    self.renderx = PIL.Image.open('mirrorx' + self.nombre + '.png')
                    self.renderx = PIL.ImageTk.PhotoImage(self.renderx)
                    self.lbImage = Label(self.root, image=self.renderx).place(x=400, y=170)
                elif type.upper() == 'MIRRORY' and type.upper() in img.filtros:
                    self.flippedimage = PIL.ImageOps.flip(self.image)
                    self.flippedimage = self.flippedimage.crop((0,745,369,1080))
                    self.rgbflipped = self.flippedimage.convert('RGB')
                    self.rgbflipped.save('mirrory' + self.nombre + '.png', quality=95)
                    self.renderx = PIL.Image.open('mirrory' + self.nombre + '.png')
                    self.renderx = PIL.ImageTk.PhotoImage(self.renderx)
                    self.lbImage = Label(self.root, image=self.renderx).place(x=400, y=170)
                elif type.upper() == 'DOUBLEMIRROR' and type.upper() in img.filtros:
                    self.flippedimage = PIL.ImageOps.flip(self.image)
                    self.flippedimage = PIL.ImageOps.mirror(self.flippedimage)
                    self.flippedimage = self.flippedimage.crop((1524,744,1920,1080))
                    self.rgbflipped = self.flippedimage.convert('RGB')
                    self.rgbflipped.save('double' + self.nombre + '.png', quality=95)
                    self.renderx = PIL.Image.open('double' + self.nombre + '.png')
                    self.renderx = PIL.ImageTk.PhotoImage(self.renderx)
                    self.lbImage = Label(self.root, image=self.renderx).place(x=400, y=170)

    def gui(self):
        # BOTONES
        self.btnCargar = Button(self.root, text="Cargar", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command=self.Admin.cargar).place(x=20, y=20)
        self.btnAnalizar = Button(self.root, text="Analizar", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command=self.analizar).place(x=200, y=20)
        self.btnReportes = Button(self.root, text="Reportes", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command=self.Admin.reportes).place(x=380, y=20)
        self.btnSalir = Button(self.root, text="Salir", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command=self.root.quit).place(x=850, y=20)

        self.imgCombo = Combobox(self.root, textvariable='Seleccione', justify='center', width=12, state='readonly').place(x=540, y=20)
        self.btnImagen = Button(self.root, text="Generar Imagen", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold').place(x=700, y=20)

        self.btnOriginal = Button(self.root, text="Original", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command= lambda t = 'original': self.drawImage(t)).place(x=20, y=150)
        self.btnMirrorX = Button(self.root, text="MirrorX", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command= lambda t = 'mirrorx': self.drawImage(t)).place(x=20, y=250)
        self.btnMirrorY = Button(self.root, text="MirrorY", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command= lambda t = 'mirrory': self.drawImage(t)).place(x=20, y=350)
        self.btnDoubleMirror = Button(self.root, text="DoubleMirror", height=2, width=12, bg="#89F08F", activebackground="#71B5D9", font='Helvetica 10 bold', command= lambda t = 'doublemirror': self.drawImage(t)).place(x=20, y=450)
        
        self.root.mainloop()

if __name__ == '__main__':
    main()