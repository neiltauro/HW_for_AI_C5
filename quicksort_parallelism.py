import concurrent.futures

def quicksort_parallel(arr):
    """
    Perform Quicksort on the input array using parallelism.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Use ThreadPoolExecutor to sort left and right partitions in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        left_sorted_future = executor.submit(quicksort_parallel, left)
        right_sorted_future = executor.submit(quicksort_parallel, right)

        left_sorted = left_sorted_future.result()
        right_sorted = right_sorted_future.result()

    return left_sorted + middle + right_sorted

# Example usage:
if __name__ == "__main__":
    import random

    sample_array = [random.randint(0, 10000) for _ in range(5000)]
    print("Original array:", sample_array)

    sorted_array = quicksort_parallel(sample_array)
    print("Sorted array:", sorted_array)
