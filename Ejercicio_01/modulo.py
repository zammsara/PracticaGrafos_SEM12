class Grafo:
    def __init__(self, es_dirigido=False):
        """
        Constructor del grafo:
        Parámetro:
        - es_dirigido (bool): Si es True, el grafo será dirigido (las aristas van en una sola dirección)
                              Si es False, el grafo será no dirigido (las aristas van en ambas direcciones)
        """
        self.es_dirigido = es_dirigido
        # Diccionario donde:
        # - clave = vértice (ej: 'A')
        # - valor = lista de tuplas (vecino, peso) que representa los vértices conectados
        self.grafo = {}

    def agregar_vertice(self, vertice):
        """
        Agrega un vértice al grafo si no existe
        Parámetro:
        - vertice(str): Nombre o etiqueta del vértice (por ejemplo: 'A', 'B', 'Nodo1')
        """
        if vertice not in self.grafo:
            self.grafo[vertice] = []  #se crea una lista vacía de vecinos

    def agregar_arista(self, o,d, peso=1):
        """
        Agrega una arista entre dos vértices
        Parámetros:
        - o(str): Vértice de origen
        - d(str): Vértice de destino
        - peso (int o float): Valor numérico opcional que representa el peso/costo de la conexión entre o y d
                              Por defecto es 1. 

        Si el grafo es no dirigido, se crea la conexión en ambas direcciones
        Si o u d no existen aún, se agregan automáticamente.
        """
        # Aseguramos que ambos vértices existan
        if o not in self.grafo:
            self.agregar_vertice(o)
        if d not in self.grafo:
            self.agregar_vertice(d)

        # Agregamos una arista de o hacia d con el peso
        self.grafo[o].append((d, peso))

        # Si el grafo es no dirigido, también agregamos la arista de d hacia o
        if not self.es_dirigido:
            self.grafo[d].append((o, peso))

    def obtener_vecinos(self, vertice):
        """
        Devuelve una lista con los vecinos (adyacentes) del vértice dado
        Parámetro:
        - vertice(str): El vértice del cual queremos conocer sus conexiones

        Retorna:
        - Lista de vértices vecinos (sin mostrar el peso)
          Si el vértice no existe, retorna una lista vacía
        """
        if vertice in self.grafo:
            # Extraemos solo el nombre del vecino (ignorando el peso)
            return [vecino for vecino, _ in self.grafo[vertice]]
        else:
            return []

    def existe_arista(self, o, d):
        """
        Verifica si existe una arista entre o y d
        Parámetros:
        - o(str): Vértice de origen
        - d(str): Vértice de destino

        Retorna:
        - True si existe la conexión de o a d
        - False si no existe
        """
        if o in self.grafo:
            for vecino, _ in self.grafo[o]:
                if vecino == d:
                    return True
        return False
    
    
            