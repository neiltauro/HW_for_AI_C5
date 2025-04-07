# Python Algorithm Implementation and Bytecode Analysis Project

This project contains multiple Python scripts that demonstrate algorithmic implementations and bytecode analysis. Each script is designed to perform a specific task, and the project also includes tools to analyze and optimize these scripts.

---

## **Project Structure**

### **1. `quicksort.py`**
- **Purpose**: Implements the Quicksort algorithm to efficiently sort large datasets.
- **Inputs**:
    - A list of integers to be sorted.
- **Outputs**:
    - A sorted list of integers.
- **Functionality**:
    - The script divides the array into partitions based on a pivot element.
    - Recursively sorts the left and right partitions.
    - Combines the sorted partitions to produce the final sorted array.
- **Example Workflow**:
    - Generates a random list of 5000 integers.
    - Sorts the list using the Quicksort algorithm.
    - Prints the original and sorted arrays.

---

### **2. `matrix.py`**
- **Purpose**: Implements matrix multiplication to compute the product of two matrices.
- **Inputs**:
    - Two 2D lists (matrices) `A` and `B`.
- **Outputs**:
    - A 2D list representing the resultant matrix after multiplication.
- **Functionality**:
    - The script transposes matrix `B` for efficient column access.
    - Computes each element of the resultant matrix by performing dot products of rows and columns.
- **Example Workflow**:
    - Multiplies two 3x3 matrices `A` and `B`.
    - Prints the input matrices and the resultant matrix.

---

### **3. `crypto.py`**
- **Purpose**: Implements Caesar Cipher encryption and decryption for text inputs.
- **Inputs**:
    - A string (`text`) to be encrypted or decrypted.
    - An integer (`shift`) representing the number of positions to shift each character.
- **Outputs**:
    - An encrypted or decrypted string.
- **Functionality**:
    - The script processes each character in the text, applying the shift to generate the encrypted or decrypted output.
- **Example Workflow**:
    - Encrypts a plaintext string.
    - Decrypts the encrypted string to verify correctness.
    - Prints the first 100 characters of the encrypted and decrypted strings for brevity.

---

### **4. `genbytecode.py`**
- **Purpose**: Compiles a Python script into bytecode and disassembles it into a human-readable format.
- **Inputs**:
    - The name of the Python script to analyze (e.g., `crypto.py`, `matrix.py`, `quicksort.py`).
- **Outputs**:
    - A text file named `<scriptname>_bytecode.txt` containing the disassembled bytecode.
- **Functionality**:
    - Uses `py_compile` to compile the input script into a `.pyc` file.
    - Reads the compiled bytecode and disassembles it using Python's `dis` module.
    - Writes the disassembled bytecode to a text file for analysis.
- **Example Workflow**:
    - Run the script with the name of the Python file to analyze:
        ```python
        python genbytecode.py crypto.py
        ```
    - Generates a file named `crypto_bytecode.txt` containing the disassembled bytecode.

---

## **Workflow**

1. **Algorithm Implementation**:
   - Write Python scripts (`quicksort.py`, `matrix.py`, `crypto.py`) to implement different workloads.
   - Test the scripts for correctness and efficiency.

2. **Bytecode Analysis**:
   - Use `genbytecode.py` to analyze the compiled bytecode of the scripts.
   - Example:
     ```
     python genbytecode.py quicksort.py
     ```
   - Output: A file named `quicksort_bytecode.txt` containing the disassembled bytecode.

3. **Performance Evaluation**:
   - Measure execution time and resource usage for each script.
   - Compare results to identify potential areas for optimization.

4. **Output Files**:
   - `<scriptname>_bytecode.txt`: Contains the human-readable bytecode of the specified script. Useful for understanding the low-level operations performed by the Python interpreter.

---

## **Purpose of Output Files**

- **`<scriptname>_bytecode.txt`**:
  - Provides insights into the compiled bytecode of the script.
  - Helps identify optimization opportunities and understand the internal workings of the Python interpreter.
  - Useful for debugging and performance analysis.

---

## **How to Run**

1. Clone or download the project files.
2. Run the scripts individually to test their functionality:
   - `python quicksort.py`
   - `python matrix.py`
   - `python crypto.py`
3. Use `genbytecode.py` to analyze the bytecode of any script:
   ```python
   python genbytecode.py <scriptname>
   ```

---

## **Conclusion**

This project demonstrates the initial steps of writing Python scripts for different workloads and analyzing their bytecode. The scripts are designed to handle various computational tasks efficiently, and the bytecode analysis provides insights into Python's internal operations, execution time, and resource usage.