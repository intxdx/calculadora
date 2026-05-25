import tkinter as tk
from tkinter import ttk
import numexpr as ne

# Controles
control = False

#Métodos
def expresion_matematica(cadena):
    global control
    if control==True:
        pantalla.delete(0,tk.END)
        pantalla.insert(0,cadena)
        control=False
    else:    
        texto_actual = pantalla.get()
        pantalla.delete(0,tk.END)
        pantalla.insert(0,texto_actual+cadena)
        
def eliminar_caracter():
    texto_actual = pantalla.get()
    pantalla.delete(0,tk.END)
    texto_modificado = texto_actual[:-1]
    pantalla.insert(0,texto_modificado)
    
def eliminar_todo():
    pantalla.delete(0,tk.END)

def resultado_operaciones():
    global control
    texto_actual = pantalla.get()
    pantalla.delete(0,tk.END)
    try:
        resultado = ne.evaluate(texto_actual)
        pantalla.insert(0,resultado)
        control = True
    except:
        error_sintaxis = "Error al calcular."
        pantalla.insert(0, error_sintaxis)
        control = True
     


#Crear Ventana
ventana = tk.Tk()
ventana.title("Calculadora")

pantalla = tk.Entry(ventana)
pantalla.grid(row=0,column=0, columnspan=5)

#Estilos
style = ttk.Style()

# Cambiar color al pasar el mouse
style.map(
    "Custom.TButton",
    background=[("active", "#005A99")],  # Fondo cuando está activo
    foreground=[("active", "black")]     # Texto cuando está activo
)
#Estilo para DEL y AC
style.configure("Danger.TButton", foreground="red")

#Botones numerales

boton_0 = ttk.Button(ventana, text= "0", width=2,command=lambda:expresion_matematica("0"))
boton_0.grid(row=4,column=0)

boton_1 = ttk.Button(ventana, text= "1", width=2, command=lambda:expresion_matematica("1"))
boton_1.grid(row=3,column=0,padx=5,pady=5)

boton_2 = ttk.Button(ventana, text= "2", width=2, command=lambda: expresion_matematica("2"))
boton_2.grid(row=3,column=1,padx=5,pady=5)

boton_3 = ttk.Button(ventana, text= "3", width=2,command=lambda: expresion_matematica("3"))
boton_3.grid(row=3,column=2,padx=5,pady=5)

boton_4 = ttk.Button(ventana, text= "4",width=2, command=lambda: expresion_matematica("4"))
boton_4.grid(row=2,column=0,padx=5,pady=5)

boton_5 = ttk.Button(ventana, text= "5",width=2, command=lambda: expresion_matematica("5"))
boton_5.grid(row=2,column=1,padx=5,pady=5)

boton_6 = ttk.Button(ventana, text= "6", width=2, command=lambda: expresion_matematica("6"))
boton_6.grid(row=2,column=2,padx=5,pady=5)

boton_7 = ttk.Button(ventana, text= "7", width=2, command=lambda: expresion_matematica("7"))
boton_7.grid(row=1,column=0,padx=5,pady=5)

boton_8 = ttk.Button(ventana, text= "8", width=2, command=lambda: expresion_matematica("8"))
boton_8.grid(row=1,column=1,padx=5,pady=5)

boton_9 = ttk.Button(ventana, text= "9",width=2, command=lambda: expresion_matematica("9"))
boton_9.grid(row=1,column=2,padx=5,pady=5)


#Botones operaciones
boton_Del = ttk.Button(ventana, text= "Del", style="Danger.TButton", width=3,command= lambda:eliminar_caracter())
boton_Del.grid(row=1,column=3,padx=5,pady=5)

boton_AC = ttk.Button(ventana, text= "AC", style="Danger.TButton", width=3, command= lambda:eliminar_todo())
boton_AC.grid(row=1,column=4)

boton_Multiplicacion = ttk.Button(ventana, text= "X", width=2, command=lambda: expresion_matematica("*"))
boton_Multiplicacion.grid(row=2,column=3,padx=5,pady=5)

boton_division = ttk.Button(ventana, text= "/",width=2,  command=lambda: expresion_matematica("/"))
boton_division.grid(row=2,column=4,padx=5,pady=5)


boton_suma = ttk.Button(ventana, text= "+", width=2, command=lambda: expresion_matematica("+"))
boton_suma.grid(row=3,column=3,padx=5,pady=5)

boton_resta = ttk.Button(ventana, text= "-", width=2, command=lambda: expresion_matematica("-"))
boton_resta.grid(row=3,column=4,padx=5,pady=5)

boton_punto = ttk.Button(ventana, text= ".",width=2,  command=lambda: expresion_matematica("."))
boton_punto.grid(row=4,column=1,padx=5,pady=5)


boton_parentesis_abierto = ttk.Button(ventana, text= "(", width=2,  command=lambda: expresion_matematica("("))
boton_parentesis_abierto.grid(row=4,column=2,padx=5,pady=5)

boton_parentesis_cerrado = ttk.Button(ventana, text= ")",width=2,  command=lambda: expresion_matematica(")"))
boton_parentesis_cerrado.grid(row=4,column=3,padx=5,pady=5)

boton_igual = ttk.Button(ventana, text= "=", width=2, command= lambda:resultado_operaciones())
boton_igual.grid(row=4,column=4,padx=5,pady=5)


ventana.mainloop()

