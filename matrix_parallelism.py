import concurrent.futures
import random

def matrix_multiply_parallel(A, B):
    """
    Perform matrix multiplication of two 2D lists A and B using parallelism.
    :param A: First matrix (list of lists)
    :param B: Second matrix (list of lists)
    :return: Resultant matrix after multiplication
    """
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    # Transpose matrix B for easier column access
    B_transposed = list(zip(*B))

    # Function to compute a single row of the result matrix
    def compute_row(row):
        return [sum(a * b for a, b in zip(row, col)) for col in B_transposed]

    # Use ThreadPoolExecutor to parallelize row computations
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = list(executor.map(compute_row, A))

    return result

# Example usage:
if __name__ == "__main__":
    # Generate a 100x100 matrix A with random integers
    A = [[random.randint(1, 10) for _ in range(100)] for _ in range(100)]
    
    # Generate a 100x100 matrix B with random integers
    B = [[random.randint(1, 10) for _ in range(100)] for _ in range(100)]

    print("Matrix A:", A)
    print("Matrix B:", B)

    result = matrix_multiply_parallel(A, B)
    print("Resultant Matrix:", result)
