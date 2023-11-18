import re
from .Token import Token


class AnalizadorLexico:
    """
    Clase que representa un analizador léxico para un lenguaje de programación.
    """

    def __init__(self):
        # Inicializa una lista vacía para guardar los tokens 
        self.tokens = []

    def analizar_codigo(self, codigo):
        """
        Analiza el código fuente y devuelve una lista de tokens encontrados.

        Args:
            codigo (str): El código fuente a analizar.

        Returns:
            list: Una lista de objetos Token que representan los tokens encontrados en el código.
        """
        
        # Inicializa la lista de tokens
        self.tokens = []
        
        # Posición actual en el codigo
        posicion = 0
        
        # Número de línea actual
        linea = 1
        
        '''
        # Comentarios con ejemplos de patrones regulares para los tokens
        
        patron_numero_natural = r'\d+'
        patron_numero_real = r'\d+\.\d+'
        patron_identificador = r'[a-zA-Z_]\w{0,9}'
        patron_palabra_reservada = r'(if|else|while|for|return|function)'
        patron_operador_aritmetico = r'(\+|-|\*|/)'
        patron_operador_comparacion = r'(==|!=|<|>|<=|>=)'
        patron_operador_logico = r'(&&|\|\|)'
        patron_operador_asignacion = r'='
        patron_operador_incremento_decremento = r'(\+\+|--)'
        patron_parentesis = r'(\(|\))'
        patron_llaves = r'(\{|})'
        patron_terminal = r';'
        patron_separador = r','
        patron_cadena_caracteres = r'"[^"]*"'
        patron_comentario_linea = r'//.*'
        patron_comentario_bloque_inicio = r'/\*'
        patron_comentario_bloque_fin = r'\*/'
        '''
        
        # Bucle principal que recorre el código caracter por caracter
        while posicion < len(codigo):
            
            # esta porsion de codigo se encarga de Saltar espacios en blanco y contar saltos de línea
            while posicion < len(codigo) and codigo[posicion].isspace():
                if codigo[posicion] == '\n':
                    linea += 1
                posicion += 1

            # Inicializar coincidencias en los patrones 
            match = None
            
            # Lista de pares patrón - categoría 
            for patron, categoria in [
                
                # aqui estam las expresiones regulares

                
                # expresion regular para Número hexadecimal (por ejemplo, 0x1A o 0XFF)
                (r'0[xX][0-9a-fA-F]+', 'NUMERO_HEXADECIMAL'),

                # expresion regular para Número real (por ejemplo, 0.14 o .14)
                (r'\d+\.\d*|\.\d+', 'NUMERO_REAL'),
                
                # expresion regular para Número natural (por ejemplo, 5) 
                (r'\d+', 'NUMERO_NATURAL'),
                
                # expresion regular para las palabras reservadas
                (r'(if|else|while|for|return|function)\b', 'PALABRA_RESERVADA'),

                # expresion regular para Identificador (por ejemplo, variable)
                (r'[a-zA-Z_]\w{0,9}', 'IDENTIFICADOR'),


                # expresion regular para Operadores de incremento/decremento
                (r'(\+\+|--)', 'OPERADOR_INCREMENTO_DECREMENTO'),


                # expresion regular para Operadores de comparación
                (r'(==|!=|<=|>=|<|>)', 'OPERADOR_COMPARACION'),
                

                # expresion regular para Operador de asignación 
                (r'[-+*/]?=', 'OPERADOR_ASIGNACION'),
                

                # expresion regular para Operadores aritméticos
                (r'(\+|-|\*|/)', 'OPERADOR_ARITMETICO'),
                

                # expresion regular para Comentario de múltiples líneas
                (r'!\*[\s\S]*?\*!', 'COMENTARIO_EN_BLOQUE'),
                

                # expresion regular para Comentario de línea con "!"
                (r'!.*', 'COMENTARIO_LINEA'),
                

                # expresion regular para Operadores lógicos
                (r'(&&|\|\|)', 'OPERADOR_LOGICO'),
                

                # expresion regular para Paréntesis  
                (r'(\(|\))', 'PARENTESIS'),
                

                # expresion regular para Llaves
                (r'(\{|})', 'LLAVES'),
                
                # expresion regular para Punto y coma 
                (r';', 'TERMINAL'),
                

                # expresion regular para Coma
                (r',', 'SEPARADOR'),
                

                # expresion regular para Cadena de caracteres
                (r'"[^"]*"', 'CADENA_CARACTERES')
              
            ]:
                
                # Compila la expresión regular
                regex = re.compile(patron)
                
                # Busca la coincidencia desde la posición actual
                match = regex.match(codigo, posicion)
                
                # Si encuentra coincidencia
                if match:
                
                    # Obtiene el lexema
                    lexema = match.group(0)
                    
                    # Crea un token con los datos del match
                    self.tokens.append(Token(lexema, categoria, linea, match.start()))
                    
                    # Actualiza la posición después de la coincidencia
                    posicion = match.end()
                    
                    # Rompe el bucle interior
                    break

            # Si no hubo coincidencia
            if not match:
                
                # Busca espacio después de posición para lexema erróneo
                error_posicion = codigo.find(' ', posicion)  
                lexema = codigo[posicion:error_posicion] if error_posicion != -1 else codigo[posicion:]
                
                # Crea token erróneo
                self.tokens.append(Token(lexema, 'TOKEN_NO_RECONOCIDO', linea, posicion))
                
                # Actualiza posición 
                posicion += len(lexema)

            # Incrementa línea si encuentra salto 
            if lexema == '\n':
                linea += 1

        # Retorna lista de tokens 
        return self.tokens
    


    