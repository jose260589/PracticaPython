from tkinter import *
from tkinter import messagebox
#importar ventanas emergentes, se puede usar para errores o cosas

root=Tk()

#funciones
def infoAdicional():
    messagebox.showinfo("Jose Inoa ", "Jose ama mucho a maribel y su hija zoe")

def avisoLicencia():
    messagebox.showwarning("Licencia","producto bajo licencia GNU")

#de esta forma se crean los menus principales.
barraMenu=Menu(root)
root.config(menu=barraMenu)

#las variables con 1, son menus principales.
#con add_command se agreguan submenues
archivoMenu1=Menu(barraMenu, tearoff=0)
#tearoff=0 quita la sepacion que aparece por defecto ----- en el menu
archivoMenu1.add_command(label="Nuevo")
archivoMenu1.add_command(label="guardar")
archivoMenu1.add_command(label="editar")
archivoMenu1.add_separator() #barra para separar
archivoMenu1.add_command(label="cerrar")

archivoedicion1=Menu(barraMenu)


archivoherramientas1=Menu(barraMenu)



archivoayuda1=Menu(barraMenu)
archivoayuda1.add_command(label="acerca de", command=lambda:infoAdicional())
archivoayuda1.add_command(label="Licencia", command=lambda:avisoLicencia())

barraMenu.add_cascade(label="Archivo", menu=archivoMenu1)
barraMenu.add_cascade(label="Edicion", menu=archivoedicion1)
barraMenu.add_cascade(label="Herramientas", menu=archivoherramientas1)
barraMenu.add_cascade(label="Ayuda", menu=archivoayuda1)

#hasta aqui se crean los menues principales

root.mainloop()
