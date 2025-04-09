import time
import random
import heapq
import matplotlib.pyplot as plt
import numpy as np
from math import inf


# --------------------------
# Graph Generation Functions
# --------------------------
def generate_sparse_graph(n):
    graph = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for i in range(n):
        neighbors = random.sample(range(n), min(4, max(1, n - 1)))
        for j in neighbors:
            if j != i:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph


def generate_dense_graph(n):
    graph = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for i in range(n):
        num_neighbors = max(1, int(n * 0.2))
        neighbors = random.sample(range(n), num_neighbors)
        for j in neighbors:
            if j != i:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph


# --------------------------
# Dijkstra's Algorithm (for all nodes)
# --------------------------
def dijkstra(graph):

    n = len(graph)
    dist_matrix = [[inf for _ in range(n)] for _ in range(n)]

    for src in range(n):
        dist = [inf] * n
        dist[src] = 0
        visited = [False] * n
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True

            for v in range(n):
                if graph[u][v] != inf and dist[v] > d + graph[u][v]:
                    dist[v] = d + graph[u][v]
                    heapq.heappush(heap, (dist[v], v))

        dist_matrix[src] = dist

    return dist_matrix


# --------------------------
# Empirical Analysis
# --------------------------
def run_experiment(graph_generator, max_nodes, step, num_trials=3):
    node_counts = list(range(10, max_nodes + 1, step))
    times = []

    for n in node_counts:
        total_time = 0
        for _ in range(num_trials):
            graph = graph_generator(n)
            start_time = time.time()
            dijkstra(graph)
            total_time += time.time() - start_time
        times.append(total_time / num_trials)
    return node_counts, times


# --------------------------
# Plotting Results
# --------------------------
def plot_results(node_counts, sparse_time, dense_time):
    plt.figure(figsize=(8, 6))

    plt.plot(node_counts, sparse_time, 'o-', label='Sparse Graph')
    plt.plot(node_counts, dense_time, 's-', label='Dense Graph')

    x = np.array(node_counts)
    sparse_fit = np.polyval(np.polyfit(x, sparse_time, 2), x)
    dense_fit = np.polyval(np.polyfit(x, dense_time, 2), x)

    plt.plot(x, sparse_fit, 'b--', label='Sparse Quadratic Fit')
    plt.plot(x, dense_fit, 'r--', label='Dense Quadratic Fit')

    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.title("Time Complexity Analysis of Dijkstra's Algorithm (All Pairs)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    max_nodes = 200
    step = 10
    num_trials = 5

    print("Testing sparse graphs...")
    sparse_nodes, sparse_time = run_experiment(generate_sparse_graph, max_nodes, step, num_trials)

    print("Testing dense graphs...")
    dense_nodes, dense_time = run_experiment(generate_dense_graph, max_nodes, step, num_trials)

    plot_results(sparse_nodes, sparse_time, dense_time)
