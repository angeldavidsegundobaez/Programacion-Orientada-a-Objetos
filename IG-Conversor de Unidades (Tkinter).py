import tkinter as tk

def convertir():
    km = float(entrada.get())
    millas = km * 0.621371
    resultado.config(text=f"{millas:.2f} millas")

root = tk.Tk()
root.title("Conversor de Km a Millas")

tk.Label(root, text="Kilómetros:").pack()
entrada = tk.Entry(root)
entrada.pack()

tk.Button(root, text="Convertir", command=convertir).pack()
resultado = tk.Label(root, text="0 millas")
resultado.pack()

root.mainloop()
