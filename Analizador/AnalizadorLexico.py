import re
from Token import Token  

class AnalizadorLexico:
    def __init__(self):
        self.tokens = []

    def analizar_codigo(self, codigo):
        self.tokens = []
        posicion = 0
        linea = 1
        '''
  # Definir patrones regulares para tokens (los mismos que mencionaste)
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

        while posicion < len(codigo):
            match = None
            for patron, categoria in [
                (patron_numero_natural, 'NUMERO_NATURAL'),
                (patron_numero_real, 'NUMERO_REAL'),
                (patron_identificador, 'IDENTIFICADOR'),
                (patron_palabra_reservada, 'PALABRA_RESERVADA'),
                (patron_operador_aritmetico, 'OPERADOR_ARITMETICO'),
                (patron_operador_comparacion, 'OPERADOR_COMPARACION'),
                (patron_operador_logico, 'OPERADOR_LOGICO'),
                (patron_operador_asignacion, 'OPERADOR_ASIGNACION'),
                (patron_operador_incremento_decremento, 'OPERADOR_INCREMENTO_DECREMENTO'),
                (patron_parentesis, 'PARENTESIS'),
                (patron_llaves, 'LLAVES'),
                (patron_terminal, 'TERMINAL'),
                (patron_separador, 'SEPARADOR'),
                (patron_cadena_caracteres, 'CADENA_CARACTERES')
            ]:
            '''
        while posicion < len(codigo):
            # Saltar espacios en blanco y contar saltos de línea
            while posicion < len(codigo) and codigo[posicion].isspace():
                if codigo[posicion] == '\n':
                    linea += 1
                posicion += 1

            match = None
            for patron, categoria in [
                (r'0[xX][0-9a-fA-F]+', 'NUMERO_HEXADECIMAL'),  # Número hexadecimal (por ejemplo, 0x1A o 0XFF)
                (r'\d+\.\d*|\.\d+', 'NUMERO_REAL'),  # Número real (por ejemplo, 0.14 o .14)
                (r'\d+', 'NUMERO_NATURAL'),  # Número natural (por ejemplo, 5)
                (r'(if|else|while|for|return|function)\b', 'PALABRA_RESERVADA'),  # Palabras reservadas
                (r'[a-zA-Z_]\w{0,9}', 'IDENTIFICADOR'),  # Identificador (por ejemplo, variable) w: Caracter
                (r'(\+\+|--)', 'OPERADOR_INCREMENTO_DECREMENTO'),  # Operadores de incremento/decremento
                (r'(==|!=|<=|>=|<|>)', 'OPERADOR_COMPARACION'),  # Operadores de comparación
                (r'[-+*/]?=', 'OPERADOR_ASIGNACION'),# Operador de asignación
                #(r'=[\+\-\*/]?', 'OPERADOR_ASIGNACION'),  
                (r'(\+|-|\*|/)', 'OPERADOR_ARITMETICO'),  # Operadores aritméticos
                (r'!\*[\s\S]*?\*!', 'COMENTARIO_EN_BLOQUE'),
                (r'!.*', 'COMENTARIO_LINEA'),  # Comentario de línea con "!"
                (r'(&&|\|\|)', 'OPERADOR_LOGICO'),  # Operadores lógicos
                (r'(\(|\))', 'PARENTESIS'),  # Paréntesis
                (r'(\{|})', 'LLAVES'),  # Llaves
                (r';', 'TERMINAL'),  # Terminal
                (r',', 'SEPARADOR'),  # Separador
                (r'"[^"]*"', 'CADENA_CARACTERES') # Cadena de caracteres
              
                
    ]:
            
                regex = re.compile(patron)
                match = regex.match(codigo, posicion)
                if match:
                    lexema = match.group(0)
                    self.tokens.append(Token(lexema, categoria, linea, match.start()))
                    posicion = match.end()
                    break

            if not match:
                # Si no se encuentra una coincidencia, se considera un token no reconocido
                error_posicion = codigo.find(' ', posicion)
                lexema = codigo[posicion:error_posicion] if error_posicion != -1 else codigo[posicion:]
                self.tokens.append(Token(lexema, 'TOKEN_NO_RECONOCIDO', linea, posicion))
                posicion += len(lexema)

            if lexema == '\n':
                linea += 1

        return self.tokens