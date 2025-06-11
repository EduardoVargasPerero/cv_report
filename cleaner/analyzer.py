"""
analyzer.py

Clase TextAnalyzer para análisis básico de texto: extracción de correos, teléfonos, nombres y estadísticas de palabras.

Autor: Eduardo Vargas <eduardoevargasp@hotmail.com>
Fecha: 11 de junio de 2025
"""

import re
from collections import Counter

class TextAnalyzer:
    """
    Clase para realizar análisis simple de texto, incluyendo:
    - Extracción de correos electrónicos
    - Extracción de números telefónicos
    - Detección básica de nombres propios
    - Estadísticas de palabras

    Atributos:
        text (str): El texto de entrada a analizar.
    """

    def __init__(self, text: str):
        """
        Inicializa el analizador con el texto dado.

        Args:
            text (str): Texto sobre el cual se realizarán los análisis.
        """
        self.text = text

    def extract_emails(self):
        """
        Extrae todas las direcciones de correo electrónico del texto.

        Returns:
            list[str]: Lista de direcciones de correo encontradas.
        """
        return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', self.text)

    def extract_phone_numbers(self):
        """
        Extrae números telefónicos que coincidan con patrones comunes (locales e internacionales).

        Returns:
            list[str]: Lista de números telefónicos encontrados.
        """
        return re.findall(r'\+?\d[\d\s()-]{7,}\d', self.text)

    def extract_names(self):
        """
        Detecta posibles nombres propios mediante una heurística:
        Palabras que inician con mayúscula seguidas opcionalmente por otra palabra con mayúscula.

        Returns:
            list[str]: Lista estimada de nombres propios.
        """
        return re.findall(r'\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,}(?:\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,})?', self.text)

    def word_stats(self):
        """
        Calcula estadísticas básicas sobre las palabras del texto.

        Returns:
            dict: Diccionario con:
                - total (int): Número total de palabras.
                - unique (int): Número de palabras únicas.
                - common (list[tuple[str, int]]): Las 10 palabras más comunes con sus frecuencias.
        """
        words = re.findall(r'\b\w+\b', self.text.lower())
        return {
            "total": len(words),
            "unique": len(set(words)),
            "common": Counter(words).most_common(10)
        }

    def summary(self):
        """
        Genera un resumen con las estadísticas del texto, correos, teléfonos y nombres detectados.

        Returns:
            str: Texto del resumen.
        """
        stats = self.word_stats()
        emails = self.extract_emails()
        phones = self.extract_phone_numbers()
        names = self.extract_names()

        summary = f"""Resumen del documento:
- Palabras totales: {stats['total']}
- Palabras únicas: {stats['unique']}

- 10 palabras más comunes:
"""
        for word, freq in stats["common"]:
            summary += f"  - {word}: {freq}\n"

        summary += f"""\n- Correos encontrados ({len(emails)}):\n"""
        summary += "\n".join(f"  - {email}" for email in emails) or "  - Ninguno"

        summary += f"""\n\n- Teléfonos encontrados ({len(phones)}):\n"""
        summary += "\n".join(f"  - {phone}" for phone in phones) or "  - Ninguno"

        summary += f"""\n\n- Nombres propios detectados (estimado: {len(names)}):\n"""
        summary += ", ".join(names[:10]) + ("..." if len(names) > 10 else "")

        return summary