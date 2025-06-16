
from modulo import Grafo
import os
from funciones import Funciones as f

"""
Módulo principal para interactuar con el grafo.
Permite al usuario crear un grafo dirigido o no dirigido y realizar diversas operaciones sobre él.
"""

def limpiar_pantalla(): 
    """Limpia la pantalla de la terminal."""
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_grafos():
    print("¿Deseas trabajar con un grafo dirigido? (s/n): ", end="")
    dirigido = input().strip().lower() == 's' # True si es dirigido, False si no lo es
    grafo = Grafo(es_dirigido=False) if not dirigido else Grafo(es_dirigido=True)
    print("\n¡Grafo creado!\n")

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
        print("0. Salir")
        print("-------------------")
        try:
            
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            continue
        match opcion:
            case 1:
               f.opcion_agregar_vertice(grafo)
               limpiar_pantalla()
            case 2:
                f.opcion_agregar_arista(grafo)
                limpiar_pantalla()
            case 3:
                f.opcion_consultar_vecinos(grafo)
                limpiar_pantalla()
            case 4:
                f.opcion_verificar_arista(grafo)
                limpiar_pantalla()
            case 5:
                f.opcion_mostrar_adyacencia(grafo)
                limpiar_pantalla()
            case 6:
                f.opcion_bfs(grafo)
                limpiar_pantalla()
            case 7:
                f.opcion_dfs(grafo)
                limpiar_pantalla()
            case 8:
                f.opcion_desconexo(grafo)
                limpiar_pantalla()
            case 0:
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                
if __name__ == "__main__":
    menu_grafos()