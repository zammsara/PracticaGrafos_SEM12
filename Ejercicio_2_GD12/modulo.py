"""
Ejercicio 2: Recorridos en Grafos (60 minutos)

Desarrolla y amplía la clase Grafo del ejercicio anterior para incluir algoritmos de recorrido en grafos:
1. Implementa el método bfs(self, inicio) para realizar un recorrido en amplitud (BFS) desde un vértice dado.
   - Debe devolver la lista de los vértices en el orden visitado usando una cola y un conjunto de visitados.
2. Implementa el método dfs(self, inicio) para realizar un recorrido en profundidad (DFS) desde un vértice dado.
   - Debe devolver la lista de los vértices en el orden visitado, preferiblemente de forma recursiva.
3. Realiza pruebas sobre un grafo no dirigido como el del Ejercicio 1, mostrando los recorridos BFS y DFS desde 'A'.
   - Prueba también el comportamiento con un grafo desconexo (ej: agrega un vértice 'F' no conectado).

"""

from collections import defaultdict, deque

class Grafo:
    """
    Clase Grafo: Estructura de datos para representar grafos dirigidos o no dirigidos usando listas de adyacencia.
    Permite agregar vértices y aristas, consultar vecinos, verificar existencia de aristas y realizar recorridos BFS y DFS.
    """
    def __init__(self, es_dirigido=False):
        self.grafo = defaultdict(list)
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
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
        """
        Recorrido en amplitud (BFS) usando una cola. Devuelve la lista de vértices en el orden en que se visitan.
        """
        if inicio not in self.grafo:
            print(f"El vértice '{inicio}' no existe en el grafo.")
            return []
        visitados = set()
        cola = deque()
        recorrido = []
        cola.append(inicio)
        visitados.add(inicio)
        while cola:
            actual = cola.popleft()
            recorrido.append(actual)
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido

    def dfs(self, inicio):
        """
        Recorrido en profundidad (DFS) usando recursividad. Devuelve la lista de vértices en el orden en que se visitan.
        """
        if inicio not in self.grafo:
            print(f"El vértice '{inicio}' no existe en el grafo.")
            return []
        visitados = set()
        recorrido = []
        def _dfs_rec(v):
            visitados.add(v)
            recorrido.append(v)
            for vecino in self.obtener_vecinos(v):
                if vecino not in visitados:
                    _dfs_rec(vecino)
        _dfs_rec(inicio)
        return recorrido

# Funciones extra para usuario
def verificar_vecinos(grafo, vertice):
    vecinos = grafo.obtener_vecinos(vertice)
    if vecinos:
        print(f"Vecinos de '{vertice}': {vecinos}")
    else:
        if vertice in grafo.grafo:
            print(f"El vértice '{vertice}' existe pero no tiene vecinos.")
        else:
            print(f"El vértice '{vertice}' NO existe en el grafo.")

def verificar_arista(grafo, u, v):
    existe = grafo.existe_arista(u, v)
    if existe:
        print(f"Sí existe una arista entre '{u}' y '{v}'.")
    else:
        print(f"No existe una arista entre '{u}' y '{v}'.")

