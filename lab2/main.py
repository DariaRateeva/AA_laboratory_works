import random
import time
import matplotlib.pyplot as plt
import copy
import sys

# Increase recursion limit for QuickSort
sys.setrecursionlimit(10000)

# Assuming these are the correct file names containing your sorting algorithms
try:
    from bubbleSort import bubbleSort
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
    random_arr = [random.randint(-1000, 1000) for _ in range(size)]
    sorted_arr = sorted(random_arr.copy())
    reversed_arr = sorted(random_arr.copy(), reverse=True)
    partially_sorted_arr = sorted(random_arr[:size // 2]) + random_arr[size // 2:]
    duplicate_arr = [random.randint(-100, 100) for _ in
                     range(size)]  # Smaller range for duplicates, including negatives

    return {
        "random": random_arr,
        "sorted": sorted_arr,
        "reversed": reversed_arr,
        "partially_sorted": partially_sorted_arr,
        "duplicates": duplicate_arr
    }


# Function to measure execution time of sorting algorithms
# Function to measure execution time of sorting algorithms
def measure_time(algorithm, arr, *args):
    arr_copy = copy.deepcopy(arr)
    start_time = time.time()

    try:
        if algorithm == quickSort:
            algorithm(arr_copy, 0, len(arr_copy) - 1)
        elif algorithm == mergeSort:
            algorithm(arr_copy, 0, len(arr_copy) - 1)
        else:  # bubble_sort and heapSort
            algorithm(arr_copy)
    except Exception as e:
        print(f"Error in {algorithm.__name__}: {e}")
        return None

    end_time = time.time()
    return (end_time - start_time) * 1000


# Main analysis function with different sizes for different algorithms
def perform_analysis():
    # Smaller sizes for Quick Sort due to recursion depth limitations
    quick_sort_sizes = [500, 1550, 5500, 8500]
    # Larger sizes for Bubble Sort, Heap Sort, and Merge Sort
    other_sort_sizes = [800, 1500, 10000, 12000]

    algorithms = {
        "Bubble Sort": bubbleSort,
        "Heap Sort": heapSort,
        "Merge Sort": mergeSort,
        "Quick Sort": quickSort
    }

    results = {alg: {data_type: [] for data_type in ["random", "sorted", "reversed",
                                                     "partially_sorted", "duplicates"]}
               for alg in algorithms}

    for alg_name, alg_func in algorithms.items():
        sizes_to_use = quick_sort_sizes if alg_name == "Quick Sort" else other_sort_sizes

        for size in sizes_to_use:
            arrays = generate_arrays(size)

            for data_type, arr in arrays.items():
                execution_time = measure_time(alg_func, arr)
                if execution_time is not None:
                    results[alg_name][data_type].append(execution_time)
                else:
                    results[alg_name][data_type].append(0)  # Default value for failed execution

    return results, (quick_sort_sizes, other_sort_sizes)


# Function to plot results
def plot_results(results, sizes):
    data_types = ["random", "sorted", "reversed", "partially_sorted", "duplicates"]
    algorithms = list(results.keys())
    colors = ['b', 'g', 'r', 'c', 'm']  # Colors for 5 data types

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


# Main execution
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
    print(f"   - Array sizes for Quick Sort: {sizes[0]}")
    print(f"   - Array sizes for Bubble, Heap, and Merge Sort: {sizes[1]}")

    print("\n3. Observations:")
    print("   - Bubble Sort: Expected O(n²) complexity, worst with reversed arrays")
    print("   - Heap Sort: O(n log n) complexity, consistent performance")
    print("   - Merge Sort: O(n log n) complexity, stable across all cases")
    print("   - Quick Sort: Average O(n log n), worst case O(n²) with sorted arrays, limited by recursion depth")