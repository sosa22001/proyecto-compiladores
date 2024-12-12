# interfaz.py
import tkinter as tk
from tkinter import ttk, messagebox
from convertidor import ConvertidorDivisas
from analizador_lexico import analizar_lexico
from analizador_sintactico import analizar_sintaxis, mostrar_arbol, generar_arbol

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Divisas")
        self.root.geometry("400x400")
        self.convertidor = ConvertidorDivisas()

        # Título
        titulo = ttk.Label(root, text="Conversor de Divisas", font=("Helvetica", 16, "bold"))
        titulo.pack(pady=10)

        # Marco de Entrada
        frame_entrada = ttk.LabelFrame(root, text="Datos de Conversión", padding=(10, 10))
        frame_entrada.pack(padx=20, pady=10, fill="both", expand="yes")

        # Cantidad
        ttk.Label(frame_entrada, text="Cantidad:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.cantidad_entry = ttk.Entry(frame_entrada, width=20)
        self.cantidad_entry.grid(row=0, column=1, padx=5, pady=5)

        # Moneda de Origen
        ttk.Label(frame_entrada, text="Moneda de Origen:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.origen_combobox = ttk.Combobox(frame_entrada, values=["DólarEstadounidense", "LempiraHondureño", "Euro"])
        self.origen_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.origen_combobox.set("DólarEstadounidense")

        # Moneda de Destino
        ttk.Label(frame_entrada, text="Moneda de Destino:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.destino_combobox = ttk.Combobox(frame_entrada, values=["DólarEstadounidense", "LempiraHondureño", "Euro"])
        self.destino_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.destino_combobox.set("LempiraHondureño")

        # Botón de Conversión
        self.convertir_button = ttk.Button(root, text="Convertir", command=self.convertir)
        self.convertir_button.pack(pady=10)

        # Resultado
        self.resultado_label = ttk.Label(root, text="Resultado: ", font=("Helvetica", 12))
        self.resultado_label.pack(pady=10)

    def convertir(self):
        # Obtener la entrada de la interfaz
        try:
            cantidad = float(self.cantidad_entry.get())
            origen = self.origen_combobox.get()
            destino = self.destino_combobox.get()

            # Validar que los campos no estén vacíos
            if not cantidad or not origen or not destino:
                raise ValueError("Todos los campos son obligatorios.")

            # Realizar conversión
            resultado = self.convertidor.convertir(cantidad, origen, destino)
            self.resultado_label.config(text=f"Resultado: {resultado:.2f} {destino}")

            # Generar tokens
            entrada = f"{cantidad},{origen},{destino}"
            tokens = analizar_lexico(entrada)

            if tokens:
                if analizar_sintaxis(tokens):
                    arbol = generar_arbol(tokens)
                    mostrar_arbol(arbol)  # Mostrar árbol si la sintaxis es válida
                else:
                    messagebox.showerror("Error Sintáctico", "La sintaxis de los tokens no es válida.")
            else:
                messagebox.showerror("Error Léxico", "La entrada no generó tokens válidos.")

        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))

        try:
            cantidad = float(self.cantidad_entry.get())
            origen = self.origen_combobox.get()
            destino = self.destino_combobox.get()

            if not origen or not destino:
                raise ValueError("Debe seleccionar monedas válidas.")

            resultado = self.convertidor.convertir(cantidad, origen, destino)
            self.resultado_label.config(text=f"Resultado: {resultado:.2f} {destino}")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def mostrar_arbol_gui(self, arbol_path="arbol.png"):
        # Crear una nueva ventana para mostrar el árbol
        ventana_arbol = tk.Toplevel(self.root)
        ventana_arbol.title("Árbol Sintáctico")

        # Cargar y mostrar la imagen del árbol
        img = tk.PhotoImage(file=arbol_path)
        label_imagen = ttk.Label(ventana_arbol, image=img)
        label_imagen.image = img  # Evitar que la imagen sea recolectada por el garbage collector
        label_imagen.pack(padx=10, pady=10)
