import time

def caesar_cipher_encrypt(text, shift):
    """
    Encrypt the given text using Caesar Cipher.
    :param text: The input string to encrypt
    :param shift: The number of positions to shift each character
    :return: Encrypted string
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """
    Decrypt the given text encrypted with Caesar Cipher.
    :param text: The encrypted string to decrypt
    :param shift: The number of positions to shift each character back
    :return: Decrypted string
    """
    return caesar_cipher_encrypt(text, -shift)

# Example usage:
if __name__ == "__main__":
    # Generate a large plaintext by repeating a smaller string
    plaintext = ("The quick brown fox jumps over the lazy dog 1234567890!@#$%^&*()_+-=[]{}|;:',.<>?/ " * 10000)
    shift = 10

    # Measure execution time
    start_time = time.time()

    encrypted = caesar_cipher_encrypt(plaintext, shift)
    print("Encrypted:", encrypted)

    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)
