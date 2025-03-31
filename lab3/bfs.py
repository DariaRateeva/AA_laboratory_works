import time
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque


# BFS implementation
def bfs(adj):
    # get number of vertices
    V = len(adj)

    # create an array to store the traversal
    res = []
    s = 0
    # Create a queue for BFS
    q = deque()

    # Initially mark all the vertices as not visited
    visited = [False] * V

    # Mark source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and store it
        curr = q.popleft()
        res.append(curr)

        # Get all adjacent vertices of the dequeued
        # vertex curr. If an adjacent has not been
        # visited, mark it visited and enqueue it
        for i in range(len(adj[curr])):
            if adj[curr][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return res


def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1


# Graph generation functions
def generate_chain_graph(n):
    """Generate a chain graph with n vertices (0-1-2-...-n-1)"""
    adj = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        add_edge(adj, i, i + 1)
    return adj


def generate_tree(n):
    """Generate a balanced binary tree with n vertices"""
    adj = [[0] * n for _ in range(n)]
    for i in range(1, n):
        parent = (i - 1) // 2
        if parent < n and i < n:
            add_edge(adj, parent, i)
    return adj


def generate_cyclic_graph(n):
    """Generate a cyclic graph (single cycle 0-1-2-...-n-1-0)"""
    adj = generate_chain_graph(n)
    add_edge(adj, 0, n - 1)  # Complete the cycle
    return adj


def generate_random_sparse_graph(n, edge_factor=2):
    """Generate random sparse graph with approximately edge_factor*n edges"""
    adj = [[0] * n for _ in range(n)]
    max_edges = n * (n - 1) // 2
    target_edges = min(edge_factor * n, max_edges)

    edges_added = 0
    while edges_added < target_edges:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and adj[u][v] == 0:
            add_edge(adj, u, v)
            edges_added += 1
    return adj


def generate_random_dense_graph(n, density=0.5):
    """Generate random dense graph with given density (0-1)"""
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                add_edge(adj, i, j)
    return adj


# Performance measurement
def measure_performance(graph_generator, max_size=800, step=50, repeats=50):
    sizes = range(step, max_size + 1, step)
    times = []

    for n in sizes:
        total_time = 0
        for _ in range(repeats):
            adj = graph_generator(n)

            start_time = time.time()
            bfs(adj)
            end_time = time.time()

            total_time += (end_time - start_time)

        avg_time = total_time / repeats
        times.append(avg_time)

    return sizes, times


# Plotting function
def plot_results(results, title="BFS Performance on Different Graph Types"):
    plt.figure(figsize=(12, 8))

    for label, (sizes, times) in results.items():
        plt.plot(sizes, times, 'o-', label=label)

    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Execution time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


# Main analysis
def analyze_bfs_performance():
    max_size = 800  # Reduced for demonstration (can increase for more thorough analysis)
    step = 50
    repeats = 50

    graph_types = {
        "Chain Graph": generate_chain_graph,
        "Binary Tree": generate_tree,
        "Cyclic Graph": generate_cyclic_graph,
        "Random Sparse (e=2n)": lambda n: generate_random_sparse_graph(n, 2),
        "Random Dense (d=0.5)": lambda n: generate_random_dense_graph(n, 0.5)
    }

    results = {}

    for name, generator in graph_types.items():
        print(f"Testing {name}...")
        sizes, times = measure_performance(generator, max_size, step, repeats)
        results[name] = (sizes, times)

    plot_results(results)


# Run the analysis
analyze_bfs_performance()