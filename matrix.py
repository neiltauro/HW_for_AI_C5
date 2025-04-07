import random

def matrix_multiply(A, B):
    """
    Perform matrix multiplication of two 2D lists A and B.
    :param A: First matrix (list of lists)
    :param B: Second matrix (list of lists)
    :return: Resultant matrix after multiplication
    """
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage:
if __name__ == "__main__":
    # Generate a 100x100 matrix A with random integers
    A = [[random.randint(1, 10) for _ in range(100)] for _ in range(100)]
    
    # Generate a 100x100 matrix B with random integers
    B = [[random.randint(1, 10) for _ in range(100)] for _ in range(100)]

    #print("Matrix A:", A)
    #print("Matrix B:", B)
    #result = matrix_multiply(A, B)
    #print("Resultant Matrix:", result)
