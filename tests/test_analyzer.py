"""
test_analyzer.py

Prueba unitaria básica para la clase TextAnalyzer, enfocada en la generación de resúmenes.

Autor: Eduardo Vargas <eduardoevargasp@hotmail.com>
Fecha: 11 de junio de 2025
"""

from cleaner.analyzer import TextAnalyzer

def test_summary():
    """
    Verifica que el resumen generado por TextAnalyzer contenga información clave.

    Caso de prueba:
        - Texto de entrada simple con repeticiones
        - Se espera que el resumen incluya "palabras totales" (indicador de estadísticas)
    """
    sample_text = "Hola mundo. Hola Python. Python es genial."
    analyzer = TextAnalyzer(sample_text)
    summary = analyzer.summary()
    assert "palabras totales" in summary.lower()