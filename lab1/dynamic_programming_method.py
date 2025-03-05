import time
import tracemalloc
import matplotlib.pyplot as plt

# Bottom-Up Dynamic Programming approach
def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Second series of Fibonacci indices (larger scope)
second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# List to store time taken for each computation
time_taken = []
space_used = []

# Compute Fibonacci numbers using DP and measure time taken
for num in second_series:
    tracemalloc.start()
    start_time = time.time()
    fibonacci_dp(num)  # Using Bottom-Up DP method
    end_time = time.time()

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)
    space_used.append(peak_memory / 1024)
    print(f"Fibonacci({num}) computed in {elapsed_time:.6f} seconds, Peak Memory Usage: {peak_memory / 1024:.2f} KB")

# Plot results
plt.plot(second_series, time_taken, marker='o', linestyle='-', color='g')
plt.xlabel("Fibonacci Term")
plt.ylabel("Time Taken (seconds)")
plt.title("Bottom-Up Dynamic Programming Fibonacci Computation Time")
plt.grid(True)
plt.show()


# Plot space complexity
plt.figure(figsize=(10, 5))
plt.plot(second_series, space_used, marker='s', linestyle='-', color='r', label="Peak Memory Usage")
plt.xlabel("Fibonacci Term (n)")
plt.ylabel("Memory Usage (KB)")
plt.title("Bottom-Up Dynamic Programming Fibonacci Space Complexity")
plt.grid(True)
plt.legend()
plt.show()