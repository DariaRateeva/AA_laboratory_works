import time
import tracemalloc
import matplotlib.pyplot as plt

# Matrix exponentiation method for Fibonacci (O(log n))
MOD = 10**9 + 7

# function to multiply two 2x2 Matrices
def multiply(A, B):
    # Matrix to store the result
    C = [[0, 0], [0, 0]]

    # Matrix Multiply
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    # Copy the result back to the first matrix
    A[0][0] = C[0][0]
    A[0][1] = C[0][1]
    A[1][0] = C[1][0]
    A[1][1] = C[1][1]

# Function to find (Matrix M ^ expo)
def power(M, expo):
    # Initialize result with identity matrix
    ans = [[1, 0], [0, 1]]

    # Fast Exponentiation
    while expo:
        if expo & 1:
            multiply(ans, M)
        multiply(M, M)
        expo >>= 1

    return ans


def nthFibonacci(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    M = [[1, 1], [1, 0]]
    # F(0) = 0, F(1) = 1
    F = [[1, 0], [0, 0]]

    # Multiply matrix M (n - 1) times
    res = power(M, n - 1)

    # Multiply Resultant with Matrix F
    multiply(res, F)

    return res[0][0] % MOD

# Second series of Fibonacci indices (larger scope)
second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# List to store time taken for each computation
time_taken = []
space_used = []

# Compute Fibonacci numbers using Matrix Power method and measure time taken
for num in second_series:
    tracemalloc.start()
    start_time = time.time()
    nthFibonacci(num)  # Using Matrix Power method
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
