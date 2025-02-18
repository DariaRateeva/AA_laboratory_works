import time
import tracemalloc
import matplotlib.pyplot as plt
def nth_fibonacci(n):
    if n <= 1:
        return n

    # To store the curr Fibonacci number
    curr = 0

    # To store the previous Fibonacci numbers
    prev1 = 1
    prev2 = 0

    # Loop to calculate Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        # Calculate the curr Fibonacci number
        curr = prev1 + prev2

        # Update prev2 to the last Fibonacci number
        prev2 = prev1

        # Update prev1 to the curr Fibonacci number
        prev1 = curr

    return curr

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
plt.title("Space optimized approach"
          " Computation Time")
plt.grid(True)
plt.show()


# Plot space complexity
plt.figure(figsize=(10, 5))
plt.plot(first_series, space_used, marker='s', linestyle='-', color='r', label="Peak Memory Usage")
plt.xlabel("Fibonacci Term (n)")
plt.ylabel("Memory Usage (KB)")
plt.title("Space-Optimized Fibonacci Space Complexity")
plt.grid(True)
plt.legend()
plt.show()