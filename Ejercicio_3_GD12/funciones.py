# Métodos utilitarios para operar sobre grafos.
# Todos reciben como primer argumento la instancia de la clase Grafo.
from grafo import Grafo
from collections import defaultdict, deque

class Funciones:
    def opcion_agregar_vertice(grafo):
        vertice = input("Nombre del vértice: ").strip()
        grafo.agregar_vertice(vertice)
        print(f"Vértice '{vertice}' agregado.")

    def opcion_agregar_arista(grafo):
        u = input("Vértice de inicio: ").strip()
        v = input("Vértice de destino: ").strip()
        try:
            peso = int(input("Peso (opcional, por defecto 1): ").strip() or "1")
        except ValueError:
            print("Peso inválido, se usará 1.")
            peso = 1
        grafo.agregar_arista(u, v, peso)
        if grafo.es_dirigido:
            print(f"Arista '{u}' -> '{v}' agregada (peso={peso}).")
        else:
            print(f"Arista '{u}' <-> '{v}' agregada (peso={peso}).")

    def opcion_consultar_vecinos(grafo):
        vertice = input("Vértice a consultar: ").strip()
        vecinos = grafo.obtener_vecinos(vertice)
        if vecinos:
            print(f"Vecinos de '{vertice}': {vecinos}")
        else:
            if vertice in grafo.grafo:
                print(f"El vértice '{vertice}' existe pero no tiene vecinos.")
            else:
                print(f"El vértice '{vertice}' NO existe en el grafo.")
                
    def opcion_verificar_arista(grafo):
        u = input("Vértice de inicio: ").strip()
        v = input("Vértice de destino: ").strip()
        if grafo.existe_arista(u, v):
            print(f"Sí existe una arista entre '{u}' y '{v}'.")
        else:
            print(f"No existe una arista entre '{u}' y '{v}'.")

    def opcion_mostrar_adyacencia(grafo):
        grafo.mostrar_adyacencia()

    def opcion_bfs(grafo):
        inicio = input("Vértice inicial para BFS: ").strip()
        resultado = grafo.bfs(inicio)
        if resultado:
            print(f"Recorrido BFS desde '{inicio}': {resultado}")

    def opcion_dfs(grafo):
        inicio = input("Vértice inicial para DFS: ").strip()
        resultado = grafo.dfs(inicio)
        if resultado:
            print(f"Recorrido DFS desde '{inicio}': {resultado}")

    def opcion_desconexo(grafo):
        print("Agregando vértice 'F' (desconexo)...")
        grafo.agregar_vertice('F')
        grafo.mostrar_adyacencia()
        inicio = input("Vértice inicial para BFS/DFS: ").strip()
        print(f"BFS: {grafo.bfs(inicio)}")
        print(f"DFS: {grafo.dfs(inicio)}")

    # Métodos nuevos para ejercicio 3
    def opcion_es_conexo(grafo):
        if grafo.es_conexo():
            print("El grafo es conexo.")
        else:
            print("El grafo NO es conexo.")

    def opcion_encontrar_camino(grafo):
        inicio = input("Vértice de inicio: ").strip()
        fin = input("Vértice destino: ").strip()
        camino = grafo.encontrar_camino(inicio, fin)
        if camino:
            print(f"Camino de '{inicio}' a '{fin}': {camino}")
        else:
            print(f"No existe camino entre '{inicio}' y '{fin}'.")
