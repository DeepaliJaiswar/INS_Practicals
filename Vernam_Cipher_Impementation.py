def generate_cipher(key, plaintext):
    if len(key) != len(plaintext):
        raise ValueError("Key and plaintext must have the same length")

    # Convert the plaintext and key to binary
    plaintext_binary = ''.join(format(ord(char), '08b') for char in plaintext)

    # Perform XOR operation to calculate the ciphertext
    ciphertext_binary = ''.join(
        str(int(plaintext_bit) ^ int(key_bit)) 
        for plaintext_bit, key_bit in zip(plaintext_binary, key)
    )
    # Convert the ciphertext binary back to characters
    ciphertext = ''.join(
        chr(int(ciphertext_binary[i:i+8], 2))
        for i in range(0, len(ciphertext_binary), 8)
    )

    return ciphertext

if __name__ == "__main__":
    key = input("Enter the key (0s and 1s): ")
    plaintext = input("Enter the plaintext: ")

    try:
        ciphertext = generate_cipher(key, plaintext)
        print("Ciphertext:", ciphertext)
    except ValueError as e:
        print("Error:", e)

