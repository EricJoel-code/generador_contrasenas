import tkinter as tk
from tkinter import messagebox
from password_generator import transformar_texto_a_contraseña, generar_contraseña, guardar_contraseña

def generar():
    try:
        tipo = int(tipo_var.get())
        if tipo not in range(1, 9):
            raise ValueError
        if tipo == 8:
            texto = referencia_entry.get()
            contraseña = transformar_texto_a_contraseña(texto)
        else:
            longitud = int(longitud_entry.get())
            if longitud <= 0:
                raise ValueError
            referencia = referencia_entry.get() if tipo in [4, 5] else ""
            include_symbols = include_symbols_var.get()
            include_digits = include_digits_var.get()
            contraseña = generar_contraseña(longitud, tipo, referencia, include_symbols, include_digits)
        
        result_label.config(text=f"La contraseña generada es: {contraseña}")

        if guardar_var.get():
            guardar_contraseña(contraseña)
            messagebox.showinfo("Información", "La contraseña se ha guardado en 'contraseñas.txt'.")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def limpiar_campos():
    longitud_entry.delete(0, tk.END)
    referencia_entry.delete(0, tk.END)
    include_symbols_var.set(False)
    include_digits_var.set(False)
    result_label.config(text="")

def mostrar_opciones_adicionales():
    tipo = int(tipo_var.get())

    # Ocultar todas las opciones adicionales
    longitud_label.pack_forget()
    longitud_entry.pack_forget()
    referencia_label.pack_forget()
    referencia_entry.pack_forget()
    include_symbols_check.pack_forget()
    include_digits_check.pack_forget()

    if tipo in [1, 2, 3, 4, 5, 6, 7]:
        longitud_label.pack()
        longitud_entry.pack()
        if tipo in [4, 5]:
            referencia_label.pack()
            referencia_entry.pack()
        if tipo == 6:
            include_symbols_check.pack()
            include_digits_check.pack()
    elif tipo == 8:
        referencia_label.pack()
        referencia_entry.pack()

# Configurar la ventana principal de Tkinter
root = tk.Tk()
root.title("Generador de Contraseñas")

tk.Label(root, text="Seleccione el tipo de contraseña que desea generar:").pack()

tipo_var = tk.StringVar(value="1")
tk.Radiobutton(root, text="1. Solo minúsculas", variable=tipo_var, value="1", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="2. Solo mayúsculas", variable=tipo_var, value="2", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="3. Solo números", variable=tipo_var, value="3", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="4. Con una referencia específica", variable=tipo_var, value="4", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="5. Mezcla de letras (mayúsculas y minúsculas) con referencia", variable=tipo_var, value="5", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="6. Personalizada (letras, símbolos, y/o números)", variable=tipo_var, value="6", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="7. Mezcla de todos los caracteres", variable=tipo_var, value="7", command=mostrar_opciones_adicionales).pack(anchor='w')
tk.Radiobutton(root, text="8. A partir de un texto proporcionado", variable=tipo_var, value="8", command=mostrar_opciones_adicionales).pack(anchor='w')

longitud_label = tk.Label(root, text="Ingrese el tamaño de la contraseña:")
longitud_entry = tk.Entry(root)

referencia_label = tk.Label(root, text="Referencia (si aplica):")
referencia_entry = tk.Entry(root)

include_symbols_var = tk.BooleanVar()
include_symbols_check = tk.Checkbutton(root, text="Incluir símbolos", variable=include_symbols_var)

include_digits_var = tk.BooleanVar()
include_digits_check = tk.Checkbutton(root, text="Incluir números", variable=include_digits_var)

guardar_var = tk.BooleanVar()
tk.Checkbutton(root, text="Guardar contraseña en archivo", variable=guardar_var).pack(anchor='w')

tk.Button(root, text="Generar", command=generar).pack()
tk.Button(root, text="Generar otra contraseña", command=limpiar_campos).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
