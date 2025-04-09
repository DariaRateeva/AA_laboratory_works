import time
import random
import matplotlib.pyplot as plt
import numpy as np
from math import inf


# --------------------------
# Graph Generation Functions
# --------------------------
def generate_sparse_graph(n):
    """Sparse graph: Each node connects to ~4 neighbors."""
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
    """Dense graph: Each node connects to ~20% of other nodes."""
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
# Floyd-Warshall Algorithm (Dynamic Programming)
# --------------------------
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != inf and dist[k][j] != inf and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


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
            floyd_warshall(graph)
            total_time += time.time() - start_time
        times.append(total_time / num_trials)
    return node_counts, times


# --------------------------
# Plotting Results
# --------------------------
def plot_results(node_counts, sparse_time, dense_time):
    plt.figure(figsize=(8, 6))

    plt.plot(node_counts, sparse_time, 'o-', label='Sparse Graph (O(n³))')
    plt.plot(node_counts, dense_time, 's-', label='Dense Graph (O(n³))')

    x = np.array(node_counts)
    sparse_fit = np.polyval(np.polyfit(x, sparse_time, 3), x)
    dense_fit = np.polyval(np.polyfit(x, dense_time, 3), x)

    plt.plot(x, sparse_fit, 'b--', label='Sparse Cubic Fit')
    plt.plot(x, dense_fit, 'r--', label='Dense Cubic Fit')

    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Analysis of Floyd-Warshall Algorithm')
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
