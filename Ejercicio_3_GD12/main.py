from grafo import Grafo
from funciones import Funciones
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Menú modular validando la entrada y usando match-case con enteros.
    grafo = Grafo()
    while True:
        print("\n--- MENÚ GRAFOS ---")
        print("1. Agregar vértice")
        print("2. Agregar arista")
        print("3. Consultar vecinos de un vértice")
        print("4. Verificar existencia de arista")
        print("5. Mostrar lista de adyacencia")
        print("6. Recorrido BFS")
        print("7. Recorrido DFS")
        print("8. Prueba de recorrido en grafo desconexo")
        print("9. Verificar si el grafo es conexo")
        print("10. Encontrar camino entre dos vértices")
        print("0. Salir")
        print("-------------------")
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        match opcion:
            case 1:
                Funciones.opcion_agregar_vertice(grafo)
                limpiar_pantalla()
            case 2:
                Funciones.opcion_agregar_arista(grafo)
                limpiar_pantalla()
            case 3:
                Funciones.opcion_consultar_vecinos(grafo)
                limpiar_pantalla()
            case 4:
                Funciones.opcion_verificar_arista(grafo)
                limpiar_pantalla()
            case 5:
                Funciones.opcion_mostrar_adyacencia(grafo)
                limpiar_pantalla()
            case 6:
                Funciones.opcion_bfs(grafo)
                limpiar_pantalla()
            case 7:
                Funciones.opcion_dfs(grafo)
                limpiar_pantalla()
            case 8:
                Funciones.opcion_desconexo(grafo)
                limpiar_pantalla()
            case 9:
                Funciones.opcion_es_conexo(grafo)
                limpiar_pantalla()
            case 10:
                Funciones.opcion_encontrar_camino(grafo)
                limpiar_pantalla()
           
            case 0:
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida.")

if __name__ == '__main__':
    menu()
