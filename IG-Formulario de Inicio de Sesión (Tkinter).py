import tkinter as tk
from tkinter import messagebox

def login():
    user = entry_user.get()
    password = entry_pass.get()
    if user == "admin" and password == "123":
        messagebox.showinfo("Éxito", "Inicio de sesión correcto")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Usuario:").grid(row=0, column=0)
tk.Label(root, text="Contraseña:").grid(row=1, column=0)

entry_user = tk.Entry(root)
entry_pass = tk.Entry(root, show="*")
entry_user.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

tk.Button(root, text="Ingresar", command=login).grid(row=2, columnspan=2)

root.mainloop()
