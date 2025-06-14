import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vértice '{vertice}' agregado.")
        else:
            print(f"Vértice '{vertice}' ya existe.")
            
    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.grafo[u].add(v)
        if not self.es_dirigido:
            self.grafo[v].add(u)
        print(f"Arista '{u} - {v}' (bidireccional) agregada.")
    
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])
        return []

    def existe_arista(self, u, v):
        return u in self.grafo and v in self.grafo[u]

    def bfs(self, inicio):
        visitados = set()
        cola = collections.deque()
        cola.append(inicio)
        visitados.add(inicio)
        recorrido = []

        while cola:
            vertice_actual = cola.popleft()
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return recorrido

    def bfs(self, inicio):
        visitados = set()
        cola = collections.deque()
        cola.append(inicio)
        visitados.add(inicio)
        recorrido = []

        while cola:
            vertice_actual = cola.popleft()
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return recorrido

    def dfs(self, inicio):
        visitados = set()
        recorrido = []

        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")

            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)

        _dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("\n--- Representación del Grafo ---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {', '.join(vecinos)}")
        print("--------------------------------")

    def es_conexo(self):
        if not self.grafo:
            return True
        primer_vertice = next(iter(self.grafo))
        recorrido_bfs = self.bfs(primer_vertice)
        return len(recorrido_bfs) == len(self.grafo)
    
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no existen en el grafo.")
            return []

        cola = collections.deque()
        visitados = set()
        padres = {}
        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None

        while cola:
            actual = cola.popleft()
            if actual == fin:
                camino = []
                while actual:
                    camino.append(actual)
                    actual = padres[actual]
                return camino[::-1]

            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)

        return []  # Si no hay camino
