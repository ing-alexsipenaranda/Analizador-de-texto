# analizador_texto.py

class AnalizadorTexto:
    def __init__(self, nombre_archivo):
        """Constructor: Inicializa las estructuras de datos"""
        self.texto = ""                    # String: guarda todo el texto del archivo
        self.lineas = []                   # Lista: cada línea del archivo
        self.palabras = []                 # Lista: todas las palabras encontradas
        self.oraciones = []                # Lista: todas las oraciones
        self.frecuencias = {}              # Dict: {palabra: veces_que_aparece}
        self.longitud_palabras = {}        # Dict: {longitud: cantidad}
        self.estadisticas = ()             # Tupla: estadísticas finales inmutables

        # Cargar y procesar archivo automáticamente
        self.cargar_archivo(nombre_archivo)
        self.procesar_texto()

    def cargar_archivo(self, nombre_archivo):
        """Lee el archivo de texto y lo almacena"""
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                self.texto = archivo.read()
                self.lineas = self.texto.split('\n')
            print(f"✅ Archivo '{nombre_archivo}' cargado exitosamente")
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'")

    def procesar_texto(self):
        """Procesa el texto y extrae palabras, oraciones, etc."""
        import re
        # Limpiar y extraer palabras (eliminar puntuación)
        texto_limpio = re.sub(r'[^\w\s]', ' ', self.texto.lower())
        self.palabras = texto_limpio.split()

        # Extraer oraciones (dividir por . ! ?)
        self.oraciones = re.split(r'[.!?]+', self.texto)
        self.oraciones = [s.strip() for s in self.oraciones if s.strip()]


    def analizar_frecuencia_palabras(self):
        """Calcula la frecuencia de cada palabra en el texto"""
        for palabra in self.palabras:
            if palabra in self.frecuencias:
                self.frecuencias[palabra] += 1
            else:
                self.frecuencias[palabra] = 1

        # Calcular longitud de palabras
        for palabra in self.palabras:
            longitud = len(palabra)
            if longitud in self.longitud_palabras:
                self.longitud_palabras[longitud] += 1
            else:
                self.longitud_palabras[longitud] = 1
        print("✅ Análisis de frecuencia de palabras completado")


    def obtener_top_palabras(self, n=5):
        """Devuelve las n palabras más frecuentes"""
        return sorted(self.frecuencias.items(), key=lambda item: item[1], reverse=True)[:n] 
    