from collections import deque

class Grafo:
    def __init__(self, es_dirigido=False):
        self.lista_adyacencia = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = set()

    def agregar_arista(self, vertice1, vertice2):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.lista_adyacencia[vertice1].add(vertice2)
        if not self.es_dirigido:
            self.lista_adyacencia[vertice2].add(vertice1)

    def obtener_vecinos(self, vertice):
        return self.lista_adyacencia.get(vertice, [])

    def existe_arista(self, vertice1, vertice2):
        return vertice2 in self.lista_adyacencia.get(vertice1, [])

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        resultado = []

        while cola:
            vertice = cola.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                cola.extend(self.lista_adyacencia[vertice] - visitados)
        return resultado

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        resultado = [inicio]
        for vecino in self.lista_adyacencia[inicio]:
            if vecino not in visitados:
                resultado.extend(self.dfs(vecino, visitados))
        return resultado

    def imprimir_grafo(self):
        for vertice in self.lista_adyacencia:
            print(f"{vertice} -> {', '.join(self.lista_adyacencia[vertice])}")

    def es_conexo(self):
        if not self.lista_adyacencia:
            return True
        inicio = next(iter(self.lista_adyacencia))
        visitados = set(self.dfs(inicio))
        return len(visitados) == len(self.lista_adyacencia)

    def encontrar_camino(self, inicio, destino, camino=None):
        if camino is None:
            camino = []
        camino = camino + [inicio]
        if inicio == destino:
            return camino
        if inicio not in self.lista_adyacencia:
            return None
        for vecino in self.lista_adyacencia[inicio]:
            if vecino not in camino:
                nuevo_camino = self.encontrar_camino(vecino, destino, camino)
                if nuevo_camino:
                    return nuevo_camino
        return None

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista("Managua", "Masaya")
grafo.agregar_arista("Managua", "León")
grafo.agregar_arista("Masaya", "Granada")
grafo.agregar_arista("Granada", "Rivas")

grafo.imprimir_grafo()

print("BFS desde Managua:", grafo.bfs("Managua"))
print("DFS desde Managua:", grafo.dfs("Managua"))
print("¿Es conexo?:", grafo.es_conexo())
print("Camino de Managua a Rivas:", grafo.encontrar_camino("Managua", "Rivas"))