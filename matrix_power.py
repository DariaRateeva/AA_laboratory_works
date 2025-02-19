import time
import tracemalloc
import matplotlib.pyplot as plt


def multiply(mat1, mat2):
    # Perform matrix multiplication
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    # Update matrix mat1 with the result
    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w


# Function to perform matrix exponentiation
def matrix_power(mat1, n):
    # Base case for recursion
    if n == 0 or n == 1:
        return

    # Initialize a helper matrix
    mat2 = [[1, 1], [1, 0]]

    # Recursively calculate mat1^(n // 2)
    matrix_power(mat1, n // 2)

    # Square the matrix mat1
    multiply(mat1, mat1)

    # If n is odd, multiply by the helper matrix mat2
    if n % 2 != 0:
        multiply(mat1, mat2)


# Function to calculate the nth Fibonacci number
def nth_fibonacci(n):
    if n <= 1:
        return n

    # Initialize the transformation matrix
    mat1 = [[1, 1], [1, 0]]

    # Raise the matrix mat1 to the power of (n - 1)
    matrix_power(mat1, n - 1)

    # The result is in the top-left cell of the matrix
    return mat1[0][0]
# Second series of Fibonacci indices (larger scope)
second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# List to store time taken for each computation
time_taken = []
space_used = []

# Compute Fibonacci numbers using Matrix Power method and measure time taken
for num in second_series:
    tracemalloc.start()
    start_time = time.time()
    nth_fibonacci(num)  # Using Matrix Power method
    end_time = time.time()

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)
    space_used.append(peak_memory / 1024)


    print(f"Fibonacci({num}) computed in {elapsed_time:.6f} seconds, Peak Memory Usage: {peak_memory / 1024:.2f} KB")

# Plot results
plt.plot(second_series, time_taken, marker='o', linestyle='-', color='r')
plt.xlabel("Fibonacci Term")
plt.ylabel("Time Taken (seconds)")
plt.title("Matrix Exponentiation Fibonacci Computation Time")
plt.grid(True)
plt.show()

# Plot space complexity
plt.figure(figsize=(10, 5))
plt.plot(second_series, space_used, marker='s', linestyle='-', color='b', label="Peak Memory Usage")
plt.xlabel("Fibonacci Term (n)")
plt.ylabel("Memory Usage (KB)")
plt.title("Matrix Exponentiation Fibonacci Space Complexity")
plt.grid(True)
plt.legend()
plt.show()
