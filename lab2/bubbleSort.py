def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Remove the swapped flag and always perform all passes
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    # No early termination, ensuring O(n²) behavior even for sorted arrays