# main.py - Archivo principal para ejecutar el analizador

from analizador_texto import AnalizadorTexto

def main():
    print("🔍 ANALIZADOR DE TEXTO v1.0")
    print("-" * 40)

    # Crear instancia del analizador
    analizador = AnalizadorTexto("mi_texto.txt")

    # Analizar frecuencia de palabras
    analizador.analizar_frecuencia_palabras()

    # Mostrar top 5 palabras en consola
    print("\n📊 Top 5 palabras más frecuentes:")
    for palabra, frecuencia in analizador.obtener_top_palabras(5):
        print(f"   • {palabra}: {frecuencia} veces")

    # Calcular y mostrar estadísticas
    stats = analizador.calcular_estadisticas()
    print(f"\n📈 Resumen del texto:")
    print(f"   • Complejidad: {'Simple' if stats[3] < 15 else 'Compleja'}")
    print(f"   • Diversidad léxica: {(stats[2]/stats[0])*100:.1f}%")

    # Generar reporte completo
    analizador.generar_reporte("analisis_completo.txt")
    print("\n✅ Análisis completado exitosamente!")

if __name__ == "__main__":
    main()