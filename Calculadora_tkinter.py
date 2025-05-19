import tkinter as tk

def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(valor))

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))

    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Entrada de la calculadora
entrada = tk.Entry(ventana, width=20, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (texto, fila, columna) in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14), command=calcular)
    else:
        
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14), command=lambda t=texto: click_boton(t))
    boton.grid(row=fila, column=columna, padx=2, pady=2)

# Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Cero", width=5, height=2, font=("Arial", 14), command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=4, sticky="we", padx=2, pady=2)

ventana.mainloop()