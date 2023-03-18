import random
import networkx as nx
import heapq
import time

# Función para crear un grafo aleatorio con n nodos y m aristas
def crear_grafo_aleatorio(n, m):
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(m):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        w = random.randint(1, 10)
        G.add_edge(u, v, weight=w)
    return G

# Función para implementar el algoritmo A*
def a_star(G, start, end):
    # Inicializar la cola de prioridad con el nodo de inicio
    heap = [(0, start)]
    # Inicializar el diccionario de nodos visitados
    visited = {}
    # Inicializar el diccionario de padres
    parents = {}
    # Mientras la cola de prioridad no esté vacía
    while heap:
        # Sacar el nodo con la menor distancia estimada de la cola de prioridad
        (f, u) = heapq.heappop(heap)
        # Si el nodo ya ha sido visitado, continuar
        if u in visited:
            continue
        # Marcar el nodo como visitado y guardar su distancia estimada
        visited[u] = f
        # Si llegamos al nodo final, terminar
        if u == end:
            break
        # Para cada vecino del nodo actual
        for (v, w) in G[u].items():
            # Calcular la distancia real desde el nodo inicial al vecino
            g = visited[u] + w['weight']
            # Calcular la distancia estimada desde el vecino al nodo final
            h = nx.shortest_path_length(G, v, end, weight='weight')
            # Calcular la distancia total estimada desde el nodo inicial al nodo final a través del vecino
            f = g + h
            # Si el vecino ya ha sido visitado con una distancia estimada menor o igual, continuar
            if v in visited and visited[v] <= f:
                continue
            # Agregar el vecino a la cola de prioridad con su distancia estimada
            heapq.heappush(heap, (f, v))
            # Guardar el nodo padre del vecino
            parents[v] = u
    # Si no se pudo llegar al nodo final, regresar None
    if end not in visited:
        return None
    # Reconstruir la ruta más corta desde el nodo inicial al nodo final
    path = [end]
    while path[-1] != start:
        path.append(parents[path[-1]])
    path.reverse()
    return path

# Ejemplo de uso
n = 30
m = 60
start = 0
end = n-1

G = crear_grafo_aleatorio(n, m)
print("Grafo:", G.edges(data=True))

start_time = time.time()
ruta_mas_corta = a_star(G, start, end)
end_time = time.time()
print("Ruta más corta:", ruta_mas_corta)
print("Tiempo de compilación:", end_time - start_time)
