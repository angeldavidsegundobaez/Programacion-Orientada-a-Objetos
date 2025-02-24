import tkinter as tk

def click(boton):
    entrada.insert(tk.END, boton)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def borrar():
    entrada.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora")

entrada = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row, col = 1, 0
for boton in botones:
    tk.Button(root, text=boton, width=5, height=2, font=("Arial", 14), 
              command=lambda b=boton: click(b) if b != "=" else calcular()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=borrar).grid(row=row, column=0, columnspan=2)
root.mainloop()
