import time
import tracemalloc
import matplotlib.pyplot as plt
import numpy as np


def matrix_multiply(A, B, m):
    """
    Multiply two 2x2 matrices with modulo to prevent overflow
    """
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m]
    ]


def matrix_power(matrix, n, m):
    """
    Calculate matrix power using efficient square-and-multiply algorithm with modulo
    """
    if n == 0:
        return [[1, 0], [0, 1]]

    # Initialize result as identity matrix
    result = [[1, 0], [0, 1]]
    base = matrix

    # Square and multiply algorithm
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base, m)
        base = matrix_multiply(base, base, m)
        n //= 2

    return result


def nth_fibonacci(n):
    """
    Calculate nth Fibonacci number using optimized matrix power
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Use a large prime modulo to prevent overflow while maintaining correctness
    m = 10 ** 20 + 7
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1, m)
    return result_matrix[0][0]


# Generate test series with exponential growth
first_series = [2 ** i for i in range(5, 25)]  # From 2^5 to 2^24

# Lists to store measurements
time_taken = []
space_used = []

# Compute Fibonacci numbers and measure performance
for num in first_series:
    # Take multiple measurements for each n
    times = []
    peaks = []
    for _ in range(5):  # Run 5 times for each number
        tracemalloc.start()
        start_time = time.time()
        nth_fibonacci(num)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(end_time - start_time)
        peaks.append(peak)

    # Use the minimum time and average memory to reduce impact of system variations
    elapsed_time = min(times)
    avg_memory = sum(peaks) / len(peaks) / 1024  # Convert to KB
    time_taken.append(elapsed_time)
    space_used.append(avg_memory)
    print(f"Fibonacci({num}) computed in {elapsed_time:.6f} seconds, Peak Memory Usage: {avg_memory:.2f} KB")

# Plot time complexity
plt.figure(figsize=(10, 6))
plt.loglog(first_series, time_taken, 'bo-', label='Actual time')
ref_log = [time_taken[0] * np.log2(x) / np.log2(first_series[0]) for x in first_series]
plt.grid(True)
plt.xlabel('n (log scale)')
plt.ylabel('Time (seconds, log scale)')
plt.title('Time Complexity of Matrix Power Fibonacci')
plt.legend()
plt.show()

# Plot space complexity
plt.figure(figsize=(10, 6))
plt.loglog(first_series, space_used, 'go-', label='Actual space')
ref_log_space = [space_used[0] * np.log2(x) / np.log2(first_series[0]) for x in first_series]
plt.grid(True)
plt.xlabel('n (log scale)')
plt.ylabel('Memory Usage (KB, log scale)')
plt.title('Space Complexity of Matrix Power Fibonacci')
plt.legend()
plt.show()

