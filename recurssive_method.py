import time
import matplotlib.pyplot as plt

# Recursive function to compute Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# First series of Fibonacci indices (limited scope)
first_series = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]

# List to store time taken for each computation
time_taken = []

# Compute Fibonacci numbers and measure time taken
for num in first_series:
    start_time = time.time()
    fibonacci_recursive(num)
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)
    print(f"Fibonacci({num}) computed in {elapsed_time:.6f} seconds")

# Plot results
plt.plot(first_series, time_taken, marker='o', linestyle='-', color='b')
plt.xlabel("Fibonacci Term")
plt.ylabel("Time Taken (seconds)")
plt.title("Recursive Fibonacci Computation Time")
plt.grid(True)
plt.show()

