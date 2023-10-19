from tkinter import *

raiz=Tk()
raiz.title("Ventana de Prueba")#agregar titulo
raiz.resizable(True, True)#mover tamaño de ventana por usuario
raiz.geometry("650x350")#Dar un tamaño a la pantalla.
raiz.iconbitmap("iconos/folder.ico")#agregar un icono o cambiar el por default de la aplicacion
raiz.config(bg="red")#hacer las configuraciones 

miFrame=Frame() #para usar el frame
#miFrame.pack(side="left", anchor="n") #empaquetar el frame
miFrame.pack(fill="both", expand="True") #enpaquetar el frame y expandirlo
miFrame.config(bg="blue") #background 
miFrame.config(width="650",height="350") #configuracion de tamaño
miFrame.config(bd="35") #tamaño de grosor
miFrame.config(relief="groove") #relieve

miFrame.config(cursor="pirate")#forma de cambiar el mouse, hand2


raiz.mainloop()#con este se ejecuta toda la venta. hay que colocar las demas opciones
#antes de esta o no saldran en la ventana, esta es la ultima en colocar
