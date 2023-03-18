import random
import time
import heapq

def crear_grafo_aleatorio(num_nodos, densidad):
    grafo = {}
    for i in range(num_nodos):
        grafo[i] = {}
        for j in range(num_nodos):
            if i != j and random.random() < densidad:
                grafo[i][j] = random.randint(1, 10)
    return grafo

def dijkstra(grafo, origen, destino):
    heap = [(0, origen, [])]
    visitados = set()
    while heap:
        (costo, actual, camino) = heapq.heappop(heap)
        if actual not in visitados:
            visitados.add(actual)
            camino = camino + [actual]
            if actual == destino:
                return camino
            for siguiente in grafo[actual]:
                nuevo_costo = costo + grafo[actual][siguiente]
                heapq.heappush(heap, (nuevo_costo, siguiente, camino))
    return []

if __name__ == '__main__':
    num_nodos = 20
    densidad = 0.3
    grafo = crear_grafo_aleatorio(num_nodos, densidad)
    nodo_inicial = random.randint(0, num_nodos - 1)
    nodo_final = random.randint(0, num_nodos - 1)
    while nodo_final == nodo_inicial:
        nodo_final = random.randint(0, num_nodos - 1)
    start_time = time.time()
    shortest_path = dijkstra(grafo, nodo_inicial, nodo_final)
    end_time = time.time()
    shortest_path = list(map(str, shortest_path))
    print(f"Camino más corto de {nodo_inicial} a {nodo_final}: {' -> '.join(shortest_path)}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
