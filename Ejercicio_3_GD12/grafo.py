"""
Ejercicio 3: Conectividad y Ruta Simple

Desarrollado por el equipo para practicar grafos en Python:
- Implementa Grafo y MenuGrafos de manera modular.
- Menú interactivo validado con try-except, usando match-case con opciones numéricas.
- Todo comentado pensando en otros estudiantes que usen el código.
"""

from collections import defaultdict, deque
import os

def limpiar_pantalla():
    """Función utilitaria para limpiar la pantalla, sirve en Windows y Linux/Mac."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Grafo:
    """
    Clase principal de grafos del equipo.
    Permite grafos dirigidos o no, aristas con peso y recorridos BFS/DFS.
    Incluye es_conexo y encontrar_camino como pide el ejercicio.
    """
    def __init__(self, es_dirigido=False):
        self.grafo = defaultdict(list)
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        # Siempre añade los vértices primero (por si no existen)
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        if (v, peso) not in self.grafo[u]:
            self.grafo[u].append((v, peso))
        if not self.es_dirigido:
            if (u, peso) not in self.grafo[v]:
                self.grafo[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        return [vecino for vecino, _ in self.grafo.get(vertice, [])]

    def existe_arista(self, u, v):
        return any(vecino == v for vecino, _ in self.grafo.get(u, []))

    def mostrar_adyacencia(self):
        print("\n--- Lista de adyacencia del grafo ---")
        for vertice, vecinos in self.grafo.items():
            vecinos_str = ", ".join(f"{vecino}(peso={peso})" for vecino, peso in vecinos)
            print(f"  {vertice} -> {vecinos_str}")
        print("-------------------------------------")

    def bfs(self, inicio):
        if inicio not in self.grafo:
            print(f"El vértice '{inicio}' no existe en el grafo.")
            return []
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        recorrido = []
        while cola:
            actual = cola.popleft()
            recorrido.append(actual)
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido

    def dfs(self, inicio):
        if inicio not in self.grafo:
            print(f"El vértice '{inicio}' no existe en el grafo.")
            return []
        visitados = set()
        recorrido = []
        def _dfs(v):
            visitados.add(v)
            recorrido.append(v)
            for vecino in self.obtener_vecinos(v):
                if vecino not in visitados:
                    _dfs(vecino)
        _dfs(inicio)
        return recorrido

    def es_conexo(self):
        """
        Devuelve True si el grafo (no dirigido) es conexo.
        Estrategia: Si el BFS desde cualquier vértice recorre todos, entonces es conexo.
        """
        if not self.grafo:
            return True
        inicio = next(iter(self.grafo))
        visitados = set(self.bfs(inicio))
        return len(visitados) == len(self.grafo)

    def encontrar_camino(self, inicio, fin):
        """
        Devuelve un camino simple de inicio a fin usando BFS, reconstruyendo con padres.
        Si no hay camino o los vértices no existen, devuelve [].
        """
        if inicio not in self.grafo or fin not in self.grafo:
            return []
        padres = {}
        visitados = set([inicio])
        cola = deque([inicio])
        padres[inicio] = None
        while cola:
            actual = cola.popleft()
            if actual == fin:
                # Reconstruir el camino usando padres
                camino = []
                while actual is not None:
                    camino.append(actual)
                    actual = padres[actual]
                return list(reversed(camino))
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    padres[vecino] = actual
                    visitados.add(vecino)
                    cola.append(vecino)
        return []

