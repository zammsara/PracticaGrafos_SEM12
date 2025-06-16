"""
Ejercicio de grafos:
Este programa implementa una clase Grafo en Python para representar grafos dirigidos y no dirigidos 
usando listas de adyacencia. Permite agregar vértices y aristas (con o sin peso), 
consultar los vecinos de un vértice y verificar si existe una arista entre dos vértices. 
Se hacen pruebas tanto con un grafo no dirigido como con uno dirigido,
mostrando la estructura resultante y las operaciones básicas solicitadas en el enunciado.
"""

from collections import defaultdict  # Importa defaultdict para inicializar listas vacías automáticamente al crear claves nuevas

class Grafo:
    def __init__(self, es_dirigido=False):
        # Diccionario donde cada clave es un vértice y su valor es una lista de tuplas (vecino, peso)
        self.grafo = defaultdict(list)
        self.es_dirigido = es_dirigido  # Booleano que indica si el grafo es dirigido (True) o no dirigido (False)

    def agregar_vertice(self, vertice):
        # Agrega un vértice al grafo solo si no existe ya
        if vertice not in self.grafo:
            self.grafo[vertice] = []  # Inicializa la lista de adyacencia para ese vértice

    def agregar_arista(self, u, v, peso=1):
        # Añade una arista desde u hasta v con un peso (por defecto 1)
        # Si los vértices no existen, los crea automáticamente
        self.agregar_vertice(u)  # Asegura que u existe en el grafo
        self.agregar_vertice(v)  # Asegura que v existe en el grafo
        # Agrega la arista u -> v si no existe ya esa conexión con ese peso
        if (v, peso) not in self.grafo[u]:
            self.grafo[u].append((v, peso))
        # Si el grafo no es dirigido, también agrega la arista v -> u
        if not self.es_dirigido:
            if (u, peso) not in self.grafo[v]:
                self.grafo[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        # Retorna solo los vértices vecinos de 'vertice', ignorando el peso
        # Si el vértice no existe, devuelve lista vacía
        return [vecino for vecino, _ in self.grafo.get(vertice, [])]

    def existe_arista(self, u, v):
        # Verifica si existe una arista de u a v (considera solo dirección u -> v)
        return any(vecino == v for vecino, _ in self.grafo.get(u, []))
    
    
# ---- Funciones externas para probar el grafo ----

def verificar_vecinos(grafo, vertice):
    # Obtiene vecinos del vértice y los imprime, o informa si no existe o no tiene vecinos
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
    # Imprime y devuelve si existe arista desde u hasta v
    existe = grafo.existe_arista(u, v)
    if existe:
        print(f"Sí existe una arista entre '{u}' y '{v}'.")
    else:
        print(f"No existe una arista entre '{u}' y '{v}'.")
    return existe

def mostrar_grafo(grafo):
    # Muestra la estructura completa: cada vértice y sus vecinos con peso
    print("\n--- Estructura completa del grafo ---")
    for vertice, vecinos in grafo.grafo.items():
        lista = [f"{vecino} (peso = {peso})" for vecino, peso in vecinos]
        print(f"{vertice} -> {', '.join(lista)}")
    print("-------------------------------------")
    
def mostrar_grafo_adyacencia(grafo):
    # Muestra la lista de adyacencia con colores en consola para mejor visualización
    print("\033[94m\n--- Lista de adyacencia del grafo ---\033[0m")  # Título azul
    for vertice, vecinos in grafo.grafo.items():
        vecinos_str = ", ".join(
            f"\033[92m{vecino}\033[0m (peso={peso})" for vecino, peso in vecinos
        )
        print(f"  \033[96m{vertice}\033[0m → {vecinos_str}")  # Vértices en cian, vecinos en verde
    print("\033[94m-------------------------------------\033[0m")  # Línea azul al final
