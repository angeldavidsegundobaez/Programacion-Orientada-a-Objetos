import tkinter as tk
import time

def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora_actual)
    root.after(1000, actualizar_hora)

root = tk.Tk()
root.title("Reloj Digital")

etiqueta = tk.Label(root, font=("Arial", 40), fg="blue")
etiqueta.pack()

actualizar_hora()
root.mainloop()
