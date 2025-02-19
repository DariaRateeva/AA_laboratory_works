import time
import matplotlib.pyplot as plt
import sys


def get_size(obj):
    """Return size of object in bytes"""
    return sys.getsizeof(obj)


def nth_fibonacci(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def measure_space_complexity(n):
    """Measure only the essential variables used in the algorithm"""
    prev, curr = 0, 1
    # Only measure the two variables we actually use
    return get_size(prev) + get_size(curr)


# Test series
first_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Lists to store time taken and space used for each computation
time_taken = []
space_used = []

# Compute Fibonacci numbers and measure time and space
for num in first_series:
    # Measure time
    start_time = time.time()
    nth_fibonacci(num)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Measure space (only essential variables)
    space = measure_space_complexity(num)

    time_taken.append(elapsed_time)
    space_used.append(space)

    print(f"Fibonacci({num}) computed in {elapsed_time:.6f} seconds, Essential Memory Usage: {space} bytes")

# Plot time complexity
plt.figure(figsize=(10, 5))
plt.plot(first_series, time_taken, marker='o', linestyle='-', color='b')
plt.xlabel("Fibonacci Term")
plt.ylabel("Time Taken (seconds)")
plt.title("Space Optimized Approach Computation Time")
plt.grid(True)
plt.show()

# Plot space complexity
plt.figure(figsize=(10, 5))
plt.plot(first_series, space_used, marker='s', linestyle='-', color='r', label="Essential Memory Usage")
plt.xlabel("Fibonacci Term (n)")
plt.ylabel("Memory Usage (bytes)")
plt.title("Space Optimized Approach Fibonacci Space Complexity (O(1))")
plt.grid(True)
plt.legend()
plt.axhline(y=space_used[0], color='g', linestyle='--', label="Constant Space Line")
plt.legend()
plt.show()