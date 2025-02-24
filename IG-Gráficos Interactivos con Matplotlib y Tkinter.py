import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar():
    datos = entry_datos.get()
    try:
        valores = list(map(int, datos.split(",")))
        fig, ax = plt.subplots()
        ax.plot(range(1, len(valores) + 1), valores, marker="o")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except ValueError:
        messagebox.showerror("Error", "Ingrese números separados por comas")

root = tk.Tk()
root.title("Gráfico de Datos")

tk.Label(root, text="Ingrese números separados por comas:").pack()
entry_datos = tk.Entry(root)
entry_datos.pack()

tk.Button(root, text="Graficar", command=graficar).pack()

root.mainloop()
