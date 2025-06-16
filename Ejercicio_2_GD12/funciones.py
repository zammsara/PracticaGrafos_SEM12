import collections  # Importa el módulo collections, no usado explícitamente en este fragmento
import modulo  # Importa un módulo externo llamado 'modulo'
from modulo import Grafo, verificar_vecinos, verificar_arista  # Importa clases y funciones específicas desde 'modulo'

class Funciones: 
    # Método para agregar un vértice al grafo solicitando el nombre al usuario
    def opcion_agregar_vertice(grafo):
        vertice = input("Nombre del vértice: ").strip()  # Solicita y limpia entrada del usuario
        grafo.agregar_vertice(vertice)  # Llama al método para agregar vértice al grafo
        print(f"Vértice '{vertice}' agregado.")  # Confirma al usuario

    # Método para agregar una arista con peso opcional
    def opcion_agregar_arista(grafo):
        u = input("Vértice de inicio: ").strip()  # Lee vértice origen
        v = input("Vértice de destino: ").strip()  # Lee vértice destino
        try:
            # Intenta leer el peso, usa 1 por defecto si el usuario no ingresa nada
            peso = int(input("Peso (opcional, por defecto 1): ").strip() or "1")
        except ValueError:
            # Si el peso no es válido, usa 1 y avisa
            print("Peso inválido, se usará 1.")
            peso = 1
        grafo.agregar_arista(u, v, peso)  # Agrega la arista con peso al grafo
        if grafo.es_dirigido:
            # Mensaje si el grafo es dirigido
            print(f"Arista '{u}' -> '{v}' agregada (peso={peso}).")
        else:
            # Mensaje si el grafo no es dirigido
            print(f"Arista '{u}' <-> '{v}' agregada (peso={peso}).")

    # Método para consultar e imprimir los vecinos de un vértice
    def opcion_consultar_vecinos(grafo):
        vertice = input("Vértice a consultar: ").strip()  # Solicita vértice a consultar
        vecinos = grafo.obtener_vecinos(vertice)  # Obtiene lista de vecinos
        if vecinos:
            # Si hay vecinos, imprime la lista
            print(f"Vecinos de '{vertice}': {vecinos}")
        else:
            # Si no hay vecinos, verifica si el vértice existe o no
            if vertice in grafo.grafo:
                print(f"El vértice '{vertice}' existe pero no tiene vecinos.")
            else:
                print(f"El vértice '{vertice}' NO existe en el grafo.")
                
    # Método para verificar e imprimir si existe una arista entre dos vértices
    def opcion_verificar_arista(grafo):
        u = input("Vértice de inicio: ").strip()  # Vértice origen
        v = input("Vértice de destino: ").strip()  # Vértice destino
        if grafo.existe_arista(u, v):
            # Si existe arista, informa al usuario
            print(f"Sí existe una arista entre '{u}' y '{v}'.")
        else:
            # Si no existe arista, informa al usuario
            print(f"No existe una arista entre '{u}' y '{v}'.")

    # Método para mostrar la lista de adyacencia del grafo usando su método interno
    def opcion_mostrar_adyacencia(grafo):
        grafo.mostrar_adyacencia()

    # Método para ejecutar y mostrar un recorrido BFS desde un vértice inicial
    def opcion_bfs(grafo):
        inicio = input("Vértice inicial para BFS: ").strip()  # Vértice desde donde iniciar BFS
        resultado = grafo.bfs(inicio)  # Ejecuta BFS
        if resultado:
            print(f"Recorrido BFS desde '{inicio}': {resultado}")  # Muestra recorrido BFS

    # Método para ejecutar y mostrar un recorrido DFS desde un vértice inicial
    def opcion_dfs(grafo):
        inicio = input("Vértice inicial para DFS: ").strip()  # Vértice desde donde iniciar DFS
        resultado = grafo.dfs(inicio)  # Ejecuta DFS
        if resultado:
            print(f"Recorrido DFS desde '{inicio}': {resultado}")  # Muestra recorrido DFS

    # Método para agregar un vértice desconexo y luego mostrar recorridos BFS y DFS
    def opcion_desconexo(grafo):
        print("Agregando vértice 'F' (desconexo)...")
        grafo.agregar_vertice('F')  # Agrega vértice desconectado al grafo
        grafo.mostrar_adyacencia()  # Muestra lista de adyacencia actualizada
        inicio = input("Vértice inicial para BFS/DFS: ").strip()  # Vértice para iniciar recorridos
        print(f"BFS: {grafo.bfs(inicio)}")  # Muestra recorrido BFS desde el inicio
        print(f"DFS: {grafo.dfs(inicio)}")  # Muestra recorrido DFS desde el inicio
