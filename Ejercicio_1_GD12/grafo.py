"""
Ejercicio de grafos:
Este programa implementa una clase Grafo en Python para representar grafos dirigidos y no dirigidos 
usando listas de adyacencia. Permite agregar vértices y aristas (con o sin peso), 
consultar los vecinos de un vértice y verificar si existe una arista entre dos vértices. 
Se hacen pruebas tanto con un grafo no dirigido como con uno dirigido,
mostrando la estructura resultante y las operaciones básicas solicitadas en el enunciado.
"""

from collections import defaultdict  # defaultdict permite inicializar listas vacías automáticamente para nuevos vértices

class Grafo:
    def __init__(self, es_dirigido=False):
        # Diccionario donde las claves son vértices y los valores son listas de tuplas (vecino, peso)
        self.grafo = defaultdict(list)
        self.es_dirigido = es_dirigido  # Controla si el grafo es dirigido o no

    def agregar_vertice(self, vertice):
        # Agrega un vértice si no existe. Si ya existe, no hace nada.
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        # Agrega una arista entre u y v. Si los vértices no existen, se crean automáticamente.
        # Si es no dirigido, agrega la arista en ambos sentidos.
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        if (v, peso) not in self.grafo[u]:
            self.grafo[u].append((v, peso))
        if not self.es_dirigido:
            if (u, peso) not in self.grafo[v]:
                self.grafo[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        # Devuelve solo los nombres de los vecinos (no los pesos). Si el vértice no existe, devuelve lista vacía.
        return [vecino for vecino, _ in self.grafo.get(vertice, [])]

    def existe_arista(self, u, v):
        # Retorna True si existe una arista de u a v (verifica solo dirección u -> v)
        return any(vecino == v for vecino, _ in self.grafo.get(u, []))
    
    
# ---- Funciones de usuario para verificar el funcionamiento del grafo ----

def verificar_vecinos(grafo, vertice):

    # Devuelve e imprime los vecinos de un vértice. Informa si el vértice no existe.

    vecinos = grafo.obtener_vecinos(vertice)
    if vecinos:
        print(f"Vecinos de '{vertice}': {vecinos}")
        return vecinos
    else:
        if vertice in grafo.grafo:
            print(f"El vértice '{vertice}' existe pero no tiene vecinos.")
            return []
        else:
            print(f"El vértice '{vertice}' NO existe en el grafo.")
            return None

def verificar_arista(grafo, u, v):

    # Indica si existe una arista entre u y v.

    existe = grafo.existe_arista(u, v)
    if existe:
        print(f"Sí existe una arista entre '{u}' y '{v}'.")
    else:
        print(f"No existe una arista entre '{u}' y '{v}'.")
    return existe

"""Función para mostrar la estructura completa del grafo. LISTA DE ADYACENCIA"""
def mostrar_grafo(grafo):
  
    # Muestra toda la estructura del grafo: vértices y sus vecinos con peso.
    print("\n--- Estructura completa del grafo ---")
    for vertice, vecinos in grafo.grafo.items():
        lista = [f"{vecino} (peso = {peso})" for vecino, peso in vecinos]
        print(f"{vertice} -> {', '.join(lista)}")
    print("-------------------------------------")
    
def mostrar_grafo_adyacencia(grafo):
    print("\033[94m\n--- Lista de adyacencia del grafo ---\033[0m")  # Azul
    for vertice, vecinos in grafo.grafo.items():
        vecinos_str = ", ".join(
            f"\033[92m{vecino}\033[0m (peso={peso})" for vecino, peso in vecinos
        )
        print(f"  \033[96m{vertice}\033[0m → {vecinos_str}")
    print("\033[94m-------------------------------------\033[0m")
