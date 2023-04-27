# Se importa la libreria tkinter con todas sus funciones
from tkinter import *

#--------------------------
#  funciones de la app
#--------------------------

#--------------------------
# Ventana principal
# -------------------------

# se declara una variable llama ventana_principal que adquiere las caracteristicas de un objeto Tk()

ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("SIstemas Uis Socorro")

# tamaño de la ventana

ventana_principal.geometry("500x500")

#deshabilitar boton de maximizar

ventana_principal.resizable(0,0)

# color de fondo
ventana_principal.config(bg="red")

#------------------------
# frame entrada datos
#------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width= 50, height = 500)
frame_entrada.place(x=150,y=0)


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width= 500, height = 50)
frame_entrada.place(x=0,y=200)



frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue", width= 35, height = 500)
frame_entrada.place(x=160,y=0)


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue", width= 500, height = 35)
frame_entrada.place(x=0,y=207)

# run
#se ejecuta la funcion (metodo) mainloop () de la clase Tk() a traves de la instancia ventana_principal. Este metodo despliega una ventana siemple en pantalla y queda a la espera de lo que el usuario haga. Cada accion del usuario se conoce como evento. El mainloop() es un bucle infinito.

ventana_principal.mainloop()

