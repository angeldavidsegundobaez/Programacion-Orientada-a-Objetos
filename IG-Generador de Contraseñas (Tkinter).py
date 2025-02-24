import tkinter as tk
import random
import string

def generar():
    longitud = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    entrada.delete(0, tk.END)
    entrada.insert(0, password)

root = tk.Tk()
root.title("Generador de Contraseñas")

entrada = tk.Entry(root, width=30)
entrada.pack()

tk.Button(root, text="Generar", command=generar).pack()
root.mainloop()
