import tkinter as tk

def agregar():
    tarea = entrada.get()
    if tarea:
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

def eliminar():
    lista.delete(tk.ANCHOR)

root = tk.Tk()
root.title("Lista de Tareas")

entrada = tk.Entry(root, width=40)
entrada.pack()

tk.Button(root, text="Agregar", command=agregar).pack()
tk.Button(root, text="Eliminar", command=eliminar).pack()

lista = tk.Listbox(root, width=50)
lista.pack()

root.mainloop()
