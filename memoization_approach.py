import sys
import time
import tracemalloc
import matplotlib.pyplot as plt
# Function to calculate the nth Fibonacci number using memoization

sys.setrecursionlimit(20000)
def nth_fibonacci_util(n, memo):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]
    memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)

    return memo[n]


# Wrapper function that handles both initialization
# and Fibonacci calculation
def nth_fibonacci(n):

    # Create a memoization table and initialize with -1
    memo = [-1] * (n + 1)

    # Call the utility function
    return nth_fibonacci_util(n, memo)

first_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# List to store time taken for each computation
time_taken = []
space_used = []
# Compute Fibonacci numbers and measure time taken
for num in first_series:
    tracemalloc.start()
    start_time = time.time()
    nth_fibonacci(num)
    end_time = time.time()

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)
    space_used.append(peak_memory / 1024)
    print(f"Fibonacci({num}) computed in {elapsed_time:.6f} seconds, Peak Memory Usage: {peak_memory / 1024:.2f} KB")

# Plot results
plt.plot(first_series, time_taken, marker='o', linestyle='-', color='b')
plt.xlabel("Fibonacci Term")
plt.ylabel("Time Taken (seconds)")
plt.title("Memoization Approach"
          " Computation Time")
plt.grid(True)
plt.show()

# Plot space complexity
plt.figure(figsize=(10, 5))
plt.plot(first_series, space_used, marker='s', linestyle='-', color='r', label="Peak Memory Usage")
plt.xlabel("Fibonacci Term (n)")
plt.ylabel("Memory Usage (KB)")
plt.title("Memoization Approach Fibonacci Space Complexity")
plt.grid(True)
plt.legend()
plt.show()
