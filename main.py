"""
main.py

Script principal para ejecutar el flujo de análisis de archivos PDF:
Carga, análisis de texto y generación de reportes (texto y HTML).

Autor: Eduardo Vargas <eduardoevargasp@hotmail.com>
Fecha: 11 de junio de 2025
"""

from cleaner.loader import PDFLoader
from cleaner.analyzer import TextAnalyzer
from cleaner.reporter import Reporter

def main():
    """
    Función principal del script:
        - Solicita al usuario una ruta de archivo PDF.
        - Extrae el texto del PDF.
        - Analiza el contenido textual.
        - Genera y guarda un resumen en formato de texto plano y HTML.
    """
    file_path = input("Ingrese la ruta del archivo PDF: ")
    try:
        text = PDFLoader.load_pdf(file_path)
        analyzer = TextAnalyzer(text)
        summary = analyzer.summary()

        Reporter.print_summary(summary)
        Reporter.save_summary_to_file(summary, "reports/summary.txt")
        Reporter.generate_html_report(summary, "reports/report.html")

        print("Reporte generado en 'reports/report.html'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()