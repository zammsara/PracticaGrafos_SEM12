import collections 
from grafo import Grafo
import os

from grafo import verificar_vecinos, verificar_arista, mostrar_grafo, mostrar_grafo_adyacencia


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    
   


# Grafo no dirigido
def menu_grafos():
    
    grafo = Grafo(es_dirigido=False)
    print("\n¡Grafo creado!\n")
    while True:
        
        # Mostrar el menú de opciones
        print("\n--- MENÚ GRAFOS ---")
        print("1. Agregar vértice")
        print("2. Agregar arista")
        print("3. Consultar vecinos de un vértice")
        print("4. Verificar existencia de arista")
        print("5. Mostrar estructura completa del grafo")
        print("6. Salir")
        print("-------------------")
        try :
            opcion = int(input("Elige una opción: ").strip())
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            limpiar_pantalla() 
            continue
 

        match opcion:    
            case 1:
                vertice = input("Nombre del vértice: ").strip()
                grafo.agregar_vertice(vertice)
                print(f"Vértice '{vertice}' agregado.")
                limpiar_pantalla()
            case 2:
                u = input("Vértice de inicio: ").strip()
                v = input("Vértice de destino: ").strip()
                try:
                    peso = int(input("Peso (opcional, por defecto 1): ").strip() or "1")
                except ValueError:
                    print("Peso inválido, se usará 1.")
                    peso = 1
                grafo.agregar_arista(u, v, peso)
                if grafo.es_dirigido:
                    print(f"Arista dirigida '{u}' -> '{v}' (peso={peso}) agregada.")
                else:
                    print(f"Arista no dirigida '{u}' <-> '{v}' (peso={peso}) agregada.")
                limpiar_pantalla()
            case 3: 
                vertice = input("Vértice a consultar: ").strip()
                verificar_vecinos(grafo, vertice)
                limpiar_pantalla()
            case 4:
                u = input("Vértice de inicio: ").strip()# Retorna una copia de la cadena con los espacios en blanco al inicio y al final eliminados
                v = input("Vértice de destino: ").strip() # Return a copy of the string with leading and trailing whitespace removed
                verificar_arista(grafo, u, v)
                limpiar_pantalla()
            case 5:
                mostrar_grafo_adyacencia(grafo)
                limpiar_pantalla()
            
            case 6:
                print("¡Hasta luego!")
                break
            case _: 
                print("Opción inválida. Intenta de nuevo.")
                limpiar_pantalla()
                
        print("\n")  # Espacio entre iteraciones del menú
# Importar las funciones de verificación y mostrar del grafo
if __name__ == '__main__':
    menu_grafos()
       
            

        