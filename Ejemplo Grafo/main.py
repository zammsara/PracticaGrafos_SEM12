import collections
from grafo import Grafo


# --- Creación de Grafo No Dirigido ---
mi_grafo = Grafo(es_dirigido=False)

mi_grafo.agregar_arista('Managua', 'Masaya')
mi_grafo.agregar_arista('Managua', 'León')
mi_grafo.agregar_arista('Masaya', 'Granada')
mi_grafo.agregar_arista('Granada', 'Rivas')
mi_grafo.agregar_arista('Managua', 'Granada') # Arista adicional para mayor conectividad

mi_grafo.imprimir_grafo()

# Operaciones Básicas
print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")
print(f"¿Existe arista entre Managua y Masaya? {mi_grafo.existe_arista('Managua', 'Masaya')}")
print(f"¿Existe arista entre Managua y Rivas? {mi_grafo.existe_arista('Managua', 'Rivas')}")

# Recorridos
print(f"Orden recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
print(f"Orden recorrido DFS desde Managua: {mi_grafo.dfs('Managua')}")

# Conectividad y Caminos
print(f"¿Es el grafo conexo? {mi_grafo.es_conexo()}")
print(f"Camino Managua - Rivas: {mi_grafo.encontrar_camino('Managua', 'Rivas')}")
print(f"Camino Managua - Juigalpa: {mi_grafo.encontrar_camino('Managua', 'Juigalpa')}")

# --- Probar con un grafo dirigido ---
grafo_dirigido = Grafo(es_dirigido=True)
grafo_dirigido.agregar_arista('Inicio', 'A')
grafo_dirigido.agregar_arista('A', 'B')
grafo_dirigido.agregar_arista('B', 'C')
grafo_dirigido.agregar_arista('C', 'Fin')
grafo_dirigido.agregar_arista('Inicio', 'D')

grafo_dirigido.imprimir_grafo()

print(f"Orden recorrido BFS dirigido desde Inicio: {grafo_dirigido.bfs('Inicio')}")
print(f"Orden recorrido DFS dirigido desde Inicio: {grafo_dirigido.dfs('Inicio')}")

print(f"Camino dirigido de Inicio a Fin: {grafo_dirigido.encontrar_camino('Inicio', 'Fin')}")
print(f"Camino dirigido de Fin a Inicio: {grafo_dirigido.encontrar_camino('Fin', 'Inicio')}")
