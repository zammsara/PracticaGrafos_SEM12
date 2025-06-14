from collections import defaultdict

class Grafo:
    """
    Clase Grafo que implementa una estructura de grafo simple (dirigido o no dirigido).
    Usa un diccionario para la representación interna:
    - Las claves son los vértices.
    - Los valores son listas de tuplas (vecino, peso).
    Permite agregar vértices y aristas automáticamente, consultar vecinos y verificar existencia de aristas.
    """
    def __init__(self, es_dirigido=False):
        """
        Inicializa un grafo vacío.
        :param es_dirigido: Si es True, el grafo es dirigido. Si es False, es no dirigido.
        """
        self.grafo = defaultdict(list)
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        """
        Agrega un vértice al grafo. Si el vértice ya existe, no realiza ninguna acción.
        """
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        """
        Agrega una arista entre los vértices u y v.
        Si los vértices no existen, los agrega automáticamente.
        Si el grafo es no dirigido, añade la arista en ambos sentidos.
        :param u: Vértice de inicio.
        :param v: Vértice de destino.
        :param peso: Peso de la arista (opcional, por defecto 1).
        """
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        # Para evitar duplicados, sólo agrega si no existe ya la arista
        if (v, peso) not in self.grafo[u]:
            self.grafo[u].append((v, peso))
        if not self.es_dirigido:
            if (u, peso) not in self.grafo[v]:
                self.grafo[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        """
        Devuelve una lista de todos los vértices adyacentes (vecinos) a un vértice dado.
        Si el vértice no existe, devuelve una lista vacía.
        """
        if vertice in self.grafo:
            # Solo se devuelven los nombres de los vecinos (no los pesos)
            return [vecino for vecino, _ in self.grafo[vertice]]
        else:
            return []

    def existe_arista(self, u, v):
        """
        Verifica si existe una arista entre u y v.
        Devuelve True si existe, False en caso contrario.
        """
        return any(vecino == v for vecino, _ in self.grafo.get(u, []))