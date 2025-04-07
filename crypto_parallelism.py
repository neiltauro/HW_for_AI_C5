import concurrent.futures

def caesar_cipher_encrypt_parallel(text, shift):
    """
    Encrypt the given text using Caesar Cipher with parallelism.
    :param text: The input string to encrypt
    :param shift: The number of positions to shift each character
    :return: Encrypted string
    """
    def encrypt_chunk(chunk):
        encrypted_chunk = ""
        for char in chunk:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                encrypted_chunk += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                encrypted_chunk += char
        return encrypted_chunk

    # Split the text into chunks for parallel processing
    chunk_size = len(text) // 4 or 1
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Use ThreadPoolExecutor to encrypt chunks in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        encrypted_chunks = list(executor.map(encrypt_chunk, chunks))

    return ''.join(encrypted_chunks)

def caesar_cipher_decrypt_parallel(text, shift):
    """
    Decrypt the given text encrypted with Caesar Cipher using parallelism.
    :param text: The encrypted string to decrypt
    :param shift: The number of positions to shift each character back
    :return: Decrypted string
    """
    return caesar_cipher_encrypt_parallel(text, -shift)

# Example usage:
if __name__ == "__main__":
    # Generate a large plaintext by repeating a smaller string
    plaintext = ("The quick brown fox jumps over the lazy dog 1234567890!@#$%^&*()_+-=[]{}|;:',.<>?/ " * 10000)
    shift = 10

    # Encrypt the text using parallelism
    encrypted = caesar_cipher_encrypt_parallel(plaintext, shift)
    print("Encrypted:", encrypted[:100] + "...")  # Print only the first 100 characters for brevity

    # Decrypt the text using parallelism
    decrypted = caesar_cipher_decrypt_parallel(encrypted, shift)
    print("Decrypted:", decrypted[:100] + "...")
