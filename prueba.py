import tkinter as tk

def mi_funcion():
    print("¡Hola la primera prueba funciona!")

ventana = tk.Tk()
ventana.title("Botón con función personalizada")

boton_personalizado = tk.Button(ventana, text="Haz clic aquí", command=mi_funcion)
boton_personalizado.pack()

ventana.mainloop()