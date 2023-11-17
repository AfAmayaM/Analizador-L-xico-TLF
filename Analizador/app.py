import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from AnalizadorLexico import AnalizadorLexico

class App:
    def __init__(self, root):
        self.root = root
        root.title("My First")

        self.codigo_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.codigo_text.pack(pady=10)

        self.analizar_button = tk.Button(root, text="Analizar", command=self.analizar)
        self.analizar_button.pack()

        self.tabla_tokens = ttk.Treeview(root, columns=("lexema", "categoria", "posicion"))
        self.tabla_tokens.heading("#1", text="Lexema")
        self.tabla_tokens.heading("#2", text="Categoría")
        self.tabla_tokens.heading("#3", text="Posición")
        self.tabla_tokens.pack(pady=10)

        # Configurar el ancho de las columnas
        self.tabla_tokens.column("#1", stretch=tk.YES)
        self.tabla_tokens.column("#2", stretch=tk.YES)
        self.tabla_tokens.column("#3", stretch=tk.YES)

        # Configurar el encabezado para que se ajuste al contenido
        for col in ("#1", "#2", "#3"):
            self.tabla_tokens.heading(col, anchor=tk.W)

    def analizar(self):
        codigo = self.codigo_text.get("1.0", "end-1c")
        analizador = AnalizadorLexico()
        tokens = analizador.analizar_codigo(codigo)
        self.mostrar_tokens(tokens)

    def mostrar_tokens(self, tokens):
        for item in self.tabla_tokens.get_children():
            self.tabla_tokens.delete(item)

        for token in tokens:
            self.tabla_tokens.insert("", "end", values=(token.lexema, token.categoria, f"({token.linea}, {token.posicion})"))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


     # Ejemplo de código para análisis
    codigo_de_prueba = """! Esto es un comentario de línea
    if lexema == '\n':
                linea += 1
    """
'''   ! Este es un comentario en línea
!*
Este es un comentario en bloque
Puede incluir múltiples líneas.
*!
print("Hola, mundo!")
!judfhsf'''