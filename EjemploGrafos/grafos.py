import collections

class Grafo:
    def __init__(self, es_dirigido = False):
        self.es_dirigido = es_dirigido
        self. grafo = {}
        
    def agregar_vertice(self, vertice):
        """Si el vertice no existe, lo agrega al grafo (conj vacio de vecinos)"""
        
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vertice {vertice} agregado al grafo.")
        else:
            print(f"El vertice {vertice} ya existe en el grafo.")
        
    def agregar_arista(self, u, v, peso = 1):
       #Nos aseguramos de que los vertices existan antes de agregar la arista
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        #Agregamos la arista
        self.grafo[u].add(v)
        print(f"Arista {u} -> {v} agregada.")
        
        #Si el grafo no es dirigido, agregamos la arista en sentido contrario
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} agregada.")
            
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice]) #Convertir a lista para devolver
        return [] 
    
    """Devuelve True si existe una arista entre u y v, False en caso contrario. (u no exista, o v no exista, o no haya arista entre ellos)"""
    def existe_arista(self, u, v):
        return u in self.grafo and v in self.grafo[u]
    
    def bfs(self, inicio):
        visitados = set()
        cola = collections.deque([inicio])
        recorrido = []

        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = []
        
        while cola:
            vertice_actual = cola.popleft()
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
            
            #Agregar vecinos no visitados a la cola
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido
    def dfs(self, inicio):
        visitados = set()
        recorrido = []
        
        def dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")

            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    dfs_recursivo(vecino)
            
        dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("------- Representación del Grafo -------")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice} -> {', '.join(vecinos)}")
        print("----------------------------------------")
        
    def es_conexo(self):
        if not self.grafo:
            return True
        
        primer_vertice = next(iter(self.grafo))
        
        recorrido = self.bfs(primer_vertice)
        return len(recorrido) == len(self.grafo)
    
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f" Error: '{inicio}' o '{fin}' no están en el grafo.")
            return []

        cola = collections.deque()
        visitados = set()
        padres = {}
        
        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None
        
        while cola:
            vertice_actual, camino = cola.popleft()

            if vertice_actual == fin:
                camino = []
                temp = fin
                
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino[::-1]  # Invertir el camino para que vaya de inicio a fin
            
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    cola.append(vecino)
                    
        return []  # Si no se encuentra un camino, devolver una lista vacía