import tkinter as tk
import random

numero_secreto = random.randint(1, 100)

def comprobar():
    intento = int(entrada.get())
    if intento < numero_secreto:
        resultado.config(text="Demasiado bajo")
    elif intento > numero_secreto:
        resultado.config(text="Demasiado alto")
    else:
        resultado.config(text="¡Correcto!")

root = tk.Tk()
root.title("Adivina el Número")

tk.Label(root, text="Adivina un número entre 1 y 100").pack()
entrada = tk.Entry(root)
entrada.pack()

tk.Button(root, text="Comprobar", command=comprobar).pack()
resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()
