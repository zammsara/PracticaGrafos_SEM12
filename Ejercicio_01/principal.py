# Importamos el módulo
from modulo import Grafo

# Importamos la librería colorama para hacer el programa más agradable visualmente
from colorama import init, Fore, Style
init(autoreset=True)

# Librería que utilizaremos en el método "clear" para limpiar pantalla
import os

# Método para limpiar pantalla
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')

def mostrar_menu():
    print('=' * 55)
    print("\t\t\tMenú")
    print('=' * 55)
    print("1. Agregar vértice")
    print("2. Agregar arista")
    print("3. Ver vecinos de un vértice")
    print("4. Verificar si existe una arista entre dos vértices")
    print("5. Mostrar todos los vértices y sus conexiones")
    print("6. Cambiar tipo de grafo (dirigido / no dirigido)")
    print("7. Salir")
    print('=' * 55)

def imprimir_grafo(grafo):
    print(Style.BRIGHT+"\nRepresentación interna del grafo:")
    for vertice, vecinos in grafo.grafo.items():
        conexiones = ', '.join([f"{d} (peso {p})" for d, p in vecinos])
        print(f"{vertice} -> {conexiones if conexiones else 'Sin conexiones'}")

def main():
    clear()
    print(Style.DIM+"Inicializando grafo NO dirigido por defecto...\n")
    g = Grafo(es_dirigido=False)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                clear()
                vertice = input("Nombre del vértice: ")
                g.agregar_vertice(vertice)
                print(Fore.GREEN+f"Vértice '{vertice}' agregado.")

            case "2":
                clear()
                o = input("Vértice origen: ")
                d = input("Vértice destino: ")
                try:
                    peso = float(input("Peso de la arista (opcional, por defecto 1): ") or 1)
                except ValueError:
                    print(Fore.YELLOW+"Peso inválido, se usará 1 por defecto.")
                    peso = 1
                g.agregar_arista(o, d, peso)
                print(Fore.GREEN+f"\nArista agregada entre '{o}' y '{d}' con peso {peso}.")

            case "3":
                clear()
                vertice = input("¿De qué vértice deseas ver los vecinos?: ")
                vecinos = g.obtener_vecinos(vertice)
                if vecinos:
                    print(f"\nVecinos de '{vertice}': {vecinos}")
                else:
                    print(Fore.YELLOW+f"\nEl vértice '{vertice}' no existe o no tiene vecinos.")

            case "4":
                clear()
                o = input("Vértice origen: ")
                d = input("Vértice destino: ")
                existe = g.existe_arista(o, d)
                print(Fore.BLUE+f"¿Existe arista entre '{o}' y '{d}'?: {'Sí' if existe else 'No'}")

            case "5":
                clear()
                imprimir_grafo(g)

            case "6":
                clear()
                tipo = input("¿Deseas grafo dirigido? (s/n): ").lower()
                if tipo == 's':
                    g = Grafo(es_dirigido=True)
                    print(Fore.BLUE+"Nuevo grafo DIRIGIDO creado.")
                else:
                    g = Grafo(es_dirigido=False)
                    print(Fore.BLUE+"Nuevo grafo NO DIRIGIDO creado.")

            case "7":
                print(Fore.CYAN+"\n¡Hasta luego!")
                break

            case _:
                clear()
                print(Fore.RED+"Opción inválida. Intenta de nuevo.\n")

main()