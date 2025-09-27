# main.py - Archivo principal para ejecutar el analizador

from  analizadordetexto import AnalizadorTexto   # ojo: aquí debe coincidir el nombre exacto del archivo

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
    print(f"   • Total de palabras: {stats['total_palabras']}")
    print(f"   • Total de caracteres: {stats['total_caracteres']}")
    print(f"   • Palabra más larga: {stats['palabra_mas_larga']}")

    # Métrica de "complejidad": promedio de longitud de palabras
    promedio_longitud = (
        stats["total_caracteres"] / stats["total_palabras"]
        if stats["total_palabras"] > 0 else 0
    )
    promedio_longitud = (
    stats["total_caracteres"] / stats["total_palabras"]
    if stats["total_palabras"] > 0 else 0
)
    print(f"   • Complejidad: {'Simple' if promedio_longitud < 15 else 'Compleja'}")

    # Diversidad léxica = cantidad de palabras únicas / total palabras
    diversidad = (
        (len(set(analizador.palabras)) / stats["total_palabras"]) * 100
        if stats["total_palabras"] > 0 else 0
    )
    print(f"   • Diversidad léxica: {diversidad:.1f}%")

    print("\n✅ Análisis completado exitosamente!")

if __name__ == "__main__":
    main()