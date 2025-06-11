import os
"""
reporter.py

Clase Reporter para mostrar, guardar y generar reportes HTML a partir de resúmenes de análisis de texto.

Autor: Eduardo Vargas <eduardoevargasp@hotmail.com>
Fecha: 11 de junio de 2025
"""

import os
from datetime import datetime

class Reporter:
    """
    Clase utilitaria para manejar la presentación y almacenamiento de resúmenes de análisis de texto.

    Métodos:
        print_summary(summary): Muestra el resumen en consola.
        save_summary_to_file(summary, filename): Guarda el resumen como archivo de texto.
        generate_html_report(summary, filename): Crea un archivo HTML con formato visual del resumen.
    """

    @staticmethod
    def print_summary(summary: str):
        """
        Imprime el resumen en la salida estándar (consola).

        Args:
            summary (str): Texto del resumen a mostrar.
        """
        print(summary)

    @staticmethod
    def save_summary_to_file(summary: str, filename: str):
        """
        Guarda el resumen en un archivo de texto plano con codificación UTF-8.

        Args:
            summary (str): Texto del resumen a guardar.
            filename (str): Ruta y nombre del archivo destino.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(summary)

    @staticmethod
    def generate_html_report(summary: str, filename: str):
        """
        Genera un archivo HTML con formato, incluyendo fecha y hora de generación.

        Args:
            summary (str): Texto del resumen a incluir en el reporte.
            filename (str): Ruta y nombre del archivo HTML de salida.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_content = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Reporte de Análisis de PDF</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f9f9f9;
                    padding: 40px;
                    color: #333;
                }}
                h1 {{
                    color: #2c3e50;
                }}
                .timestamp {{
                    font-size: 0.9em;
                    color: #888;
                }}
                pre {{
                    background-color: #fff;
                    border: 1px solid #ccc;
                    padding: 20px;
                    border-radius: 5px;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }}
            </style>
        </head>
        <body>
            <h1>Reporte de Análisis de PDF</h1>
            <p class="timestamp">Generado el {timestamp}</p>
            <pre>{summary}</pre>
        </body>
        </html>
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)