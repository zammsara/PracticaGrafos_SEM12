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
        # Inicializa el grafo como un diccionario donde cada vértice tiene una lista de adyacencia
        self.grafo = defaultdict(list)
        # Indica si el grafo es dirigido o no (por defecto no dirigido)
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        # Agrega un vértice al grafo si no existe
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        # Asegura que ambos vértices existan antes de agregar la arista
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        # Agrega la arista de u a v con el peso dado si no existe ya
        if (v, peso) not in self.grafo[u]:
            self.grafo[u].append((v, peso))
        # Si el grafo no es dirigido, agrega también la arista inversa
        if not self.es_dirigido:
            if (u, peso) not in self.grafo[v]:
                self.grafo[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        # Retorna una lista con los vecinos (vértices adyacentes) del vértice dado, ignorando el peso
        return [vecino for vecino, _ in self.grafo.get(vertice, [])]

    def existe_arista(self, u, v):
        # Verifica si existe una arista de u hacia v
        return any(vecino == v for vecino, _ in self.grafo.get(u, []))

    def mostrar_adyacencia(self):
        # Imprime la lista de adyacencia completa mostrando cada vértice y sus vecinos con peso
        print("\n--- Lista de adyacencia del grafo ---")
        for vertice, vecinos in self.grafo.items():
            vecinos_str = ", ".join(f"{vecino}(peso={peso})" for vecino, peso in vecinos)
            print(f"  {vertice} -> {vecinos_str}")
        print("-------------------------------------")

    def bfs(self, inicio):
        """
        Recorrido en amplitud (BFS) usando una cola.
        Devuelve la lista de vértices en el orden en que se visitan.
        """
        # Verifica que el vértice de inicio exista en el grafo
        if inicio not in self.grafo:
            print(f"El vértice '{inicio}' no existe en el grafo.")
            return []
        visitados = set()  # Conjunto para rastrear vértices visitados
        cola = deque()     # Cola para manejar el orden de visita BFS
        recorrido = []     # Lista para almacenar el orden de recorrido
        cola.append(inicio)
        visitados.add(inicio)
        # Mientras haya vértices por visitar
        while cola:
            actual = cola.popleft()  # Extrae el vértice actual
            recorrido.append(actual)  # Lo añade al recorrido
            # Recorre sus vecinos
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)  # Marca como visitado
                    cola.append(vecino)    # Lo añade a la cola para visitar luego
        return recorrido

    def dfs(self, inicio):
        """
        Recorrido en profundidad (DFS) usando recursividad.
        Devuelve la lista de vértices en el orden en que se visitan.
        """
        # Verifica que el vértice de inicio exista en el grafo
        if inicio not in self.grafo:
            print(f"El vértice '{inicio}' no existe en el grafo.")
            return []
        visitados = set()  # Conjunto para marcar vértices visitados
        recorrido = []     # Lista para almacenar orden de recorrido

        def _dfs_rec(v):
            visitados.add(v)      # Marca el vértice actual como visitado
            recorrido.append(v)   # Lo añade al recorrido
            # Llama recursivamente a todos sus vecinos no visitados
            for vecino in self.obtener_vecinos(v):
                if vecino not in visitados:
                    _dfs_rec(vecino)

        _dfs_rec(inicio)  # Comienza el recorrido desde el vértice inicial
        return recorrido

# Funciones extra para usuario
def verificar_vecinos(grafo, vertice):
    vecinos = grafo.obtener_vecinos(vertice)  # Obtiene los vecinos del vértice
    if vecinos:
        print(f"Vecinos de '{vertice}': {vecinos}")
    else:
        # Indica si el vértice existe pero no tiene vecinos, o si no existe
        if vertice in grafo.grafo:
            print(f"El vértice '{vertice}' existe pero no tiene vecinos.")
        else:
            print(f"El vértice '{vertice}' NO existe en el grafo.")

def verificar_arista(grafo, u, v):
    existe = grafo.existe_arista(u, v)  # Verifica si hay una arista de u a v
    if existe:
        print(f"Sí existe una arista entre '{u}' y '{v}'.")
    else:
        print(f"No existe una arista entre '{u}' y '{v}'.")
