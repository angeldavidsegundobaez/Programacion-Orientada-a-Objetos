import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def guardar_archivo():
    ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, "w") as file:
            file.write(text.get("1.0", tk.END))

root = tk.Tk()
root.title("Editor de Texto")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

tk.Button(root, text="Abrir", command=abrir_archivo).pack(side="left")
tk.Button(root, text="Guardar", command=guardar_archivo).pack(side="right")

root.mainloop()
