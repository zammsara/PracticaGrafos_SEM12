import collections 
from grafo import Grafo
import os

from grafo import verificar_vecinos, verificar_arista, mostrar_grafo, mostrar_grafo_adyacencia


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    
   


# Función para manejar un menú interactivo para manipular un grafo no dirigido
def menu_grafos():
    
    grafo = Grafo(es_dirigido=False)  # Crea un grafo no dirigido
    print("\n¡Grafo creado!\n")
    
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario decida salir
        
        # Mostrar las opciones disponibles al usuario
        print("\n--- MENÚ GRAFOS ---")
        print("1. Agregar vértice")
        print("2. Agregar arista")
        print("3. Consultar vecinos de un vértice")
        print("4. Verificar existencia de arista")
        print("5. Mostrar estructura completa del grafo")
        print("6. Salir")
        print("-------------------")
        
        try:
            # Leer opción del usuario y convertirla a entero
            opcion = int(input("Elige una opción: ").strip())
        except ValueError:
            # Si la entrada no es un número válido, mostrar mensaje y reiniciar el ciclo
            print("Entrada inválida. Por favor, ingresa un número.")
            limpiar_pantalla()  # Función para limpiar pantalla (se asume definida)
            continue  # Volver a mostrar el menú
        
        # Usamos match para seleccionar la acción según la opción ingresada
        match opcion:
            case 1:
                # Opción 1: Agregar un vértice
                vertice = input("Nombre del vértice: ").strip()
                grafo.agregar_vertice(vertice)  # Agrega el vértice al grafo
                print(f"Vértice '{vertice}' agregado.")
                limpiar_pantalla()
                
            case 2:
                # Opción 2: Agregar una arista con peso opcional
                u = input("Vértice de inicio: ").strip()
                v = input("Vértice de destino: ").strip()
                try:
                    # Lee el peso, si está vacío usa 1 por defecto
                    peso = int(input("Peso (opcional, por defecto 1): ").strip() or "1")
                except ValueError:
                    # Si el peso no es válido, usar 1 y mostrar mensaje
                    print("Peso inválido, se usará 1.")
                    peso = 1
                grafo.agregar_arista(u, v, peso)  # Agrega la arista al grafo
                
                # Mensaje diferente si es dirigido o no dirigido
                if grafo.es_dirigido:
                    print(f"Arista dirigida '{u}' -> '{v}' (peso={peso}) agregada.")
                else:
                    print(f"Arista no dirigida '{u}' <-> '{v}' (peso={peso}) agregada.")
                limpiar_pantalla()
                
            case 3:
                # Opción 3: Consultar vecinos de un vértice
                vertice = input("Vértice a consultar: ").strip()
                verificar_vecinos(grafo, vertice)  # Función externa que imprime vecinos
                limpiar_pantalla()
                
            case 4:
                # Opción 4: Verificar existencia de una arista
                u = input("Vértice de inicio: ").strip()
                v = input("Vértice de destino: ").strip()
                verificar_arista(grafo, u, v)  # Función externa que imprime si existe la arista
                limpiar_pantalla()
                
            case 5:
                # Opción 5: Mostrar la estructura completa del grafo con colores
                mostrar_grafo_adyacencia(grafo)
                limpiar_pantalla()
                
            case 6:
                # Opción 6: Salir del menú y terminar programa
                print("¡Hasta luego!")
                break
                
            case _:
                # Cualquier otra opción no válida
                print("Opción inválida. Intenta de nuevo.")
                limpiar_pantalla()
        
        print("\n")  # Espacio visual entre iteraciones del menú

# Si este script se ejecuta directamente, llama a la función del menú
if __name__ == '__main__':
    menu_grafos()
