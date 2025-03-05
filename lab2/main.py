import random
import time
import matplotlib.pyplot as plt
import copy
import sys

sys.setrecursionlimit(10000)

try:
    from selectionSort import selectionSort
    from heapSort import heapSort
    from mergeSort import mergeSort
    from quickSort import quickSort
except ImportError as e:
    print(f"Error importing sorting algorithms: {e}")
    print("Make sure all sorting algorithm files are in the same directory")
    exit(1)


# Function to generate different types of arrays with negative numbers
def generate_arrays(size=1000):
    # Use a range that includes negative numbers (-1000 to 1000 for random, -100 to 100 for duplicates)
    random_arr = [random.randint(-10000, 10000) for _ in range(size)]
    sorted_arr = sorted(random_arr.copy())
    reversed_arr = sorted(random_arr.copy(), reverse=True)
    partially_sorted_arr = sorted(random_arr[:size // 2]) + random_arr[size // 2:]
    duplicate_arr = [random.randint(-100, 100) for _ in
                     range(size)]

    return {
        "random": random_arr,
        "sorted": sorted_arr,
        "reversed": reversed_arr,
        "partially_sorted": partially_sorted_arr,
        "duplicates": duplicate_arr
    }


# Function to measure execution time of sorting algorithms
def measure_time(algorithm, arr, *args):
    arr_copy = copy.deepcopy(arr)
    start_time = time.time()

    try:
        if algorithm == quickSort:
            algorithm(arr_copy, 0, len(arr_copy) - 1)
        elif algorithm == mergeSort:
            algorithm(arr_copy, 0, len(arr_copy) - 1)
        else:
            algorithm(arr_copy)
    except Exception as e:
        print(f"Error in {algorithm.__name__}: {e}")
        return None

    end_time = time.time()
    return (end_time - start_time) * 1000


def perform_analysis():
    quick_sort_sizes = [500, 1550, 5500, 8500]
    sort_sizes = [500, 1550, 5500, 8500]

    algorithms = {
        "Selection Sort": selectionSort,
        "Heap Sort": heapSort,
        "Merge Sort": mergeSort,
        "Quick Sort": quickSort
    }

    results = {alg: {data_type: [] for data_type in ["random", "sorted", "reversed",
                                                     "partially_sorted", "duplicates"]}
               for alg in algorithms}

    for alg_name, alg_func in algorithms.items():
        sizes_to_use = sort_sizes

        for size in sizes_to_use:
            arrays = generate_arrays(size)

            for data_type, arr in arrays.items():
                execution_time = measure_time(alg_func, arr)
                if execution_time is not None:
                    results[alg_name][data_type].append(execution_time)
                else:
                    results[alg_name][data_type].append(0)

    return results, (sort_sizes, sort_sizes)


def plot_results(results, sizes):
    data_types = ["random", "sorted", "reversed", "partially_sorted", "duplicates"]
    algorithms = list(results.keys())
    colors = ['b', 'g', 'r', 'c', 'm']

    for i, alg in enumerate(algorithms):
        plt.figure(figsize=(10, 6))
        sizes_to_use = sizes[0] if alg == "Quick Sort" else sizes[1]
        for data_type in data_types:
            plt.plot(sizes_to_use, results[alg][data_type], label=data_type, marker='o',
                     color=colors[data_types.index(data_type)])

        plt.title(f"{alg} Performance Analysis")
        plt.xlabel("Array Size")
        plt.ylabel("Time (ms)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    results, sizes = perform_analysis()
    plot_results(results, sizes)

    print("\nEmpirical Analysis Conclusions:")
    print("1. Input Data Properties:")
    print("   - Random: Completely unsorted random numbers (including negatives, -1000 to 1000)")
    print("   - Sorted: Fully sorted in ascending order (including negatives)")
    print("   - Reversed: Fully sorted in descending order (including negatives)")
    print("   - Partially Sorted: First 50% sorted, rest random (including negatives)")
    print("   - Duplicates: Contains repeated values (including negatives, -100 to 100)")

    print("\n2. Metrics Used:")
    print("   - Execution time in milliseconds")
    print(f"   - Array sizes: {sizes[1]}")

    print("\n3. Observations:")
    print("   - Selection Sort: Expected O(n²) complexity, consistent performance")
    print("   - Heap Sort: O(n log n) complexity, consistent performance")
    print("   - Merge Sort: O(n log n) complexity, stable across all cases")
    print("   - Quick Sort: Average O(n log n), worst case O(n²) with sorted arrays, limited by recursion depth")