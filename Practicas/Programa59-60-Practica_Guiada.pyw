#librerias
from tkinter import *
from tkinter import messagebox as mb
import sqlite3


#raiz-----------------------
raiz=Tk()
raiz.title("Practica de BD y Grafica")
#Barra Menu
barramenu=Menu(raiz)
raiz.config(menu=barramenu)
#frame-----------------------
miframe=Frame(raiz)
miframe.pack(fill="both",expand="True")
miframe.config(width="450", height="550")

#funciones
def InfoAdicional():
    mb.showinfo("Acerca De","Jose ama mucho a su esposa Maribel y su hija Zoè")

def Licencia():
    mb.showwarning("Licencia","Producto bajo Licencia GNU")

def Salir():
    
    mensaje=BooleanVar()
    #messagebox.askquestion("Salir", "¿Deseas Salir?")
    mensaje=mb.askyesno("Salir", "¿Deseas Salir?")
    #print(mensaje)

    if(numeroconexion==1):
        miConexion.close()
    
    if (mensaje==True):
        raiz.destroy() #cerrar ventana
     
def conectar():
    global miConexion
    global miCursor
    #global numeroconexion
    miConexion=sqlite3.connect("zoe")
    miCursor=miConexion.cursor()
    numeroconexion=1

def crear_tabla():
    miCursor.execute(
        """CREATE TABLE PERSONA (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE VARCHAR(50),
                     PASSWORD VARCHAR(50),
                     APELLIDO VARCHAR(50),
                     DIRECCION VARCHAR(75),
                     COMENTARIO VARCHAR(100)
                     )""")
                     
def BorrarCampos():
    ID1.set("")
    NOMBRE.set("")
    PASSWORD.set("")
    APELLIDO.set("")
    DIRECC.set("")
    comentario.delete("1.0", END) #con este metodo se puede borrar TEXT Y scrolledtext.ScrolledText
    COMENT=""

def create():
    DIRECC.get()
    COMENT=comentario.get("1.0", END)
    print (DIRECC.get())
    miCursor.execute("insert into PERSONA values (NULL,"+
    NOMBRE.GET()+","+
    PASSWORD.get()+","+
    APELLIDO.get()+","+
    DIRECC.get()+","+
    COMENT+")")

def search():
    pass

def update():
    pass

def delete():
    pass

#variables
global numeroconexion
numeroconexion=0
ID1=StringVar()
NOMBRE=StringVar()
PASSWORD=StringVar()
APELLIDO=StringVar()
DIRECC=StringVar()
COMENT=StringVar()
global comentario
#COMENT=comentario.get("1.0", END), #CON ESTA SE Optiene datos
print(type(numeroconexion))
#menu
#Desactivar barras de menu por defecto
mBBDD=Menu(barramenu, tearoff=0)
#Desglose menu
#con el comando command se puede llamar la funciona a ejecutar
mBBDD.add_command(label="Conectar", command=lambda:conectar())
mBBDD.add_command(label="Crear Tabla Usuario", command=lambda:crear_tabla())
mBBDD.add_command(label="Salir", command=lambda:Salir())

mBorrar=Menu(barramenu, tearoff=0)
mBorrar.add_command(label="Borrar Campos", command=lambda:BorrarCampos())

mCRUD=Menu(barramenu, tearoff=0)
mCRUD.add_command(label="Crear")
mCRUD.add_command(label="Buscar")
mCRUD.add_separator() #separacion aproposito
mCRUD.add_command(label="Actualizar")
mCRUD.add_command(label="Eliminar")

mAYUDA=Menu(barramenu, tearoff=0)
mAYUDA.add_command(label="Licencia", command=lambda:Licencia())
mAYUDA.add_command(label="Acerca De...", command=lambda:InfoAdicional())


#activacion de los Menues
barramenu.add_cascade(label="BBDD", menu=mBBDD)
barramenu.add_cascade(label="BORRAR", menu=mBorrar)
barramenu.add_cascade(label="CRUD", menu=mCRUD)
barramenu.add_cascade(label="Ayuda",menu=mAYUDA)


#construccion de Ventana
#Label
milabel=Label(miframe, text="Id")
milabel.grid(column=0, row=0, padx=10, pady=10)

milabel=Label(miframe, text="Nombre")
milabel.grid(column=0, row=1, padx=10, pady=10)

milabel=Label(miframe, text="Password")
milabel.grid(column=0, row=2, padx=10, pady=10)

milabel=Label(miframe, text="Apellido")
milabel.grid(column=0, row=3, padx=10, pady=10)

milabel=Label(miframe, text="Direccion")
milabel.grid(column=0, row=4, padx=10, pady=10)

milabel=Label(miframe, text="Comentarios")
milabel.grid(column=0, row=5, padx=10, pady=10)

#Entry

id1=Entry(miframe, textvariable=ID1)
id1.grid(column=1, row=0, padx=10, pady=10, sticky="w")

nombre=Entry(miframe, textvariable=NOMBRE)
nombre.grid(column=1, row=1, padx=10, pady=10, sticky="w")

password=Entry(miframe, textvariable=PASSWORD)
password.grid(column=1, row=2, padx=10, pady=10, sticky="w")
password.config(show="*")

apellido=Entry(miframe, textvariable=APELLIDO)
apellido.grid(column=1, row=3, padx=10, pady=10, sticky="w")

direccion=Entry(miframe, textvariable=DIRECC)
direccion.grid(column=1, row=4, padx=10, pady=10, sticky="w")

#cuadro de texto con su barra - textvariable=COMENT,
comentario=Text(miframe,  width=25, height=5)
comentario.grid(column=1, row=5, padx=10, pady=10, sticky="w", columnspan=4)
barra=Scrollbar(miframe, command=comentario.yview)
barra.grid(column=1, row=5, sticky="nse", columnspan=4 )
comentario.config(yscrollcommand=barra.set)

#Botones
bcrear=Button(miframe, text="Create", justify="center", width=5, command=lambda:create())
bcrear.grid(column=0, row=6, padx=2, pady=5)

bleer=Button(miframe, text="Search", justify="center", width=5)
bleer.grid(column=1, row=6, sticky="w", padx=2, pady=5)

bactualizar=Button(miframe, text="Update", justify="center", width=7)
bactualizar.grid(column=1, row=6, sticky="e", padx=2, pady=5)

bborrar=Button(miframe, text="Delete", justify="center", width=5)
bborrar.grid(column=3, row=6, padx=2, pady=5)




raiz.mainloop()
