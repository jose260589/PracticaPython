from tkinter import *

root=Tk()
root.title("Ejemplo check button")

#agregar una imagen
#foto=PhotoImage(file=ruta o nombre de imagen)
#Label(root, image=foto).pack()

Checkbutton(root, text="Playa").pack()
Checkbutton(root, text="Montaña").pack()
Checkbutton(root, text="Turismo rural").pack()

#se maneja igual que los radiobutton, por eso no
#agregue todo el ejemplo.

root.mainloop()
