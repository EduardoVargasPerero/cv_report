"""
loader.py

Clase PDFLoader para cargar y extraer texto desde archivos PDF usando PyMuPDF (fitz).

Autor: Eduardo Vargas <eduardoevargasp@hotmail.com>
Fecha: 11 de junio de 2025
"""

import fitz  # PyMuPDF

class PDFLoader:
    """
    Clase utilitaria para cargar documentos PDF y extraer su contenido textual.

    Métodos:
        load_pdf(file_path): Extrae el texto completo de un archivo PDF dado.
    """

    @staticmethod
    def load_pdf(file_path):
        """
        Carga un archivo PDF desde el sistema de archivos y extrae su texto.

        Args:
            file_path (str): Ruta del archivo PDF a procesar.

        Returns:
            str: Texto extraído de todas las páginas del PDF.
        """
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text