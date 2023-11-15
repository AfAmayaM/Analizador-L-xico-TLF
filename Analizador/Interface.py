import tkinter as tk
from tkinter import ttk

from AnalizadorLexico import AnalizadorLexico

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Analizador Lexico - MyFirst")

        self.analizador = AnalizadorLexico()

        self.create_ui()

    def create_ui(self):
        self.create_input_section()
        self.create_results_section()
        self.create_buttons()

    def create_input_section(self):
        input_frame = ttk.LabelFrame(self.master, text="Entrada")
        input_frame.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.codigo_text = tk.Text(input_frame, width=40, height=10)
        self.codigo_text.grid(row=0, column=0, padx=10, pady=5)

    def create_results_section(self):
        results_frame = ttk.LabelFrame(self.master, text="Resultados")
        results_frame.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.resultados_text = tk.Text(results_frame, width=40, height=10)
        self.resultados_text.grid(row=0, column=0, padx=10, pady=5)

    def create_buttons(self):
        button_frame = ttk.Frame(self.master)
        button_frame.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        self.analizar_button = ttk.Button(button_frame, text="Analizar", command=self.analizar)
        self.analizar_button.grid(row=0, column=0, padx=5)

        self.borrar_button = ttk.Button(button_frame, text="Borrar Resultados", command=self.borrar_resultados)
        self.borrar_button.grid(row=0, column=1, padx=5)

    def analizar(self):
        codigo = self.codigo_text.get("1.0", "end-1c")
        tokens = self.analizador.analizar_codigo(codigo)
        self.mostrar_resultados(tokens)

    def borrar_resultados(self):
        self.resultados_text.delete("1.0", "end")

    def mostrar_resultados(self, tokens):
        self.resultados_text.delete("1.0", "end")
        for token in tokens:
            self.resultados_text.insert("end", f'Lexema: {token.lexema}, Categoría: {token.categoria}, '
                                               f'Posición: ({token.linea}, {token.posicion})\n')
