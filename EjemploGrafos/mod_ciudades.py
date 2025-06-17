import collections
from grafos import Grafo
grafo = Grafo()

def menu_principal():
    print("Menú Principal:")
    print("1. Grafo Dirigido")
    print("2. Grafo No Dirigido")
    print("3. Operaciones con Grafos")
    print("4. Salir")
    
def menu_imprimir_grafo():
    print("1. Agregar Arista")
    print("2. Vecinos de un vértice")
    print("3. Recorrido en Anchura (BFS)")
    print("4. Recorrido en Profundidad (DFS)")
    print("5. Conectividad del Grafo")
    print("6. Encontrar Camino entre dos vértices")
    print("7. Imprimir Grafo")
    print("8. Volver al Menú Principal")
    
def menu_grafos():
    respuesta = 0
    while respuesta != 8:
        menu_imprimir_grafo()
        try:
            respuesta = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        match respuesta: 
            case 1:
                u = input("Ingrese el vértice de origen: ").upper()
                v = input("Ingrese el vértice de destino: ").upper()
                grafo.agregar_arista(u, v)
            case 2:
                vertice = input("Ingrese el vértice para obtener sus vecinos: ").upper()
                vecinos = grafo.obtener_vecinos(vertice)
                if vecinos:
                    print(f"Vecinos de {vertice}: {', '.join(vecinos)}")
                else:
                    print(f"No hay vecinos para el vértice {vertice}.")
            case 3:
                inicio = input("Ingrese el vértice de inicio para BFS: ").upper()
                recorrido_bfs = grafo.bfs(inicio)
                print(f"Recorrido BFS desde {inicio}: {', '.join(recorrido_bfs)}")
            
            case 4:
                inicio = input("Ingrese el vértice de inicio para DFS: ").upper()
                recorrido_dfs = grafo.dfs(inicio)
                print(f"Recorrido DFS desde {inicio}: {', '.join(recorrido_dfs)}")
                
            case 5:
                if grafo.es_conexo():
                    print("El grafo es conexo.")
                else:
                    print("El grafo no es conexo.")
            case 6:
                u = input("Ingrese el vértice de origen: ").upper()
                v = input("Ingrese el vértice de destino: ").upper()
                camino = grafo.encontrar_camino(u, v)
                if camino:
                    print(f"Camino encontrado de {u} a {v}: {' -> '.join(camino)}")
                else:
                    print(f"No se encontró un camino de {u} a {v}.")
            case 7:
                grafo.imprimir_grafo()
            case 8: 
                print("Si regresa al menú principal, se perderán los datos en el grafo actual.")
                confirmacion = input("¿Esta seguro de que desea volver al menú principal? (S/N)").upper()
                if confirmacion == "S":
                    respuesta = 8
                elif confirmacion == "N":
                    respuesta = 0
                else:
                    print("Opción no válida. No se tomará ninguna acción.")
                    respuesta = 0
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
    
menu_grafos()
    
