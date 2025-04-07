import random

def quicksort(arr):
    """
    Perform Quicksort on the input array.
    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage:
if __name__ == "__main__":
    sample_array = [random.randint(0, 10000) for _ in range(5000)]
    print("Original array:", sample_array)
    sorted_array = quicksort(sample_array)
    print("Sorted array:", sorted_array)