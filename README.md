# Analizador-Lexico-TLF
Este proyecto es un Analizador Léxico, una parte fundamental de los compiladores que se encarga de leer el código fuente y convertirlo en tokens. Los tokens son las unidades más pequeñas de significado que son útiles para el compilador.

## Estructura del Proyecto

El proyecto está estructurado en varios módulos:

- `main.py`: Este es el punto de entrada del programa. Crea una instancia de la aplicación y la ejecuta.
- `gui/app.py`: Este módulo define la interfaz gráfica de usuario (GUI) de la aplicación.
- `analizador_lexico/AnalizadorLexico.py`: Este módulo define el Analizador Léxico. Lee el código fuente y lo convierte en tokens.
- `analizador_lexico/Token.py`: Este módulo define la clase Token, que representa una unidad de significado en el código fuente.

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto, navega al directorio que contiene `main.py` en tu terminal y ejecuta el siguiente comando:

bash
python main.py

Esto abrirá la GUI de la aplicación, donde puedes ingresar el código fuente que deseas analizar. El Analizador Léxico leerá el código fuente, lo dividirá en tokens y mostrará los tokens en la GUI.

Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir lo que te gustaría cambiar o añadir. Asegúrate de actualizar las pruebas según corresponda.

Licencia
MIT
