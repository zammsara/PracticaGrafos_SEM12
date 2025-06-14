import collections 
from grafo import Grafo

# Grafo no dirigido
grafo_nd = Grafo(es_dirigido=False)
for vertice in ['A', 'B', 'C', 'D', 'E']:
    grafo_nd.agregar_vertice(vertice)

aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas:
    grafo_nd.agregar_arista(u, v)

# Imprime vecinos
print("Vecinos de 'A':", grafo_nd.obtener_vecinos('A'))
print("Vecinos de 'D':", grafo_nd.obtener_vecinos('D'))
print("Vecinos de 'F':", grafo_nd.obtener_vecinos('F'))  # Vértice no existente

# Verifica existencia de aristas
print("¿Existe arista ('A', 'C')?", grafo_nd.existe_arista('A', 'C'))
print("¿Existe arista ('A', 'D')?", grafo_nd.existe_arista('A', 'D'))

# Grafo dirigido
grafo_d = Grafo(es_dirigido=True)
grafo_d.agregar_arista('X', 'Y')
grafo_d.agregar_arista('Y', 'Z')
grafo_d.agregar_arista('X', 'Z')

print("Vecinos de 'X' (dirigido):", grafo_d.obtener_vecinos('X'))
print("Vecinos de 'Y' (dirigido):", grafo_d.obtener_vecinos('Y'))