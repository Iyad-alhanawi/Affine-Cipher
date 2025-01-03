import numpy as np
import string

def get_cipher_keys():
    """
    Prompts the user for the two cipher keys and validates them.
    Returns:
        (int, int): A tuple containing the two cipher keys.
    """
    while True:
        try:
            a = int(input("Enter your first cipher key (integer): "))
            b = int(input("Enter your second cipher key (integer): "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter integers for the cipher keys.")

def affine_encrypt(plain_text, a, b):
    """
    Encrypts the plain text using the Affine cipher.
    
    Args:
        plain_text (str): The text to be encrypted.
        a (int): The first cipher key.
        b (int): The second cipher key.

    Returns:
        str: The encrypted cipher text.
    """
    # Ensure that a is coprime to 26
    if np.gcd(a, 26) != 1:
        raise ValueError("The first cipher key 'a' must be coprime to 26.")

    cipher_text = []
    for char in plain_text:
        if char.isalpha():  # Process only alphabetic characters
            index = ord(char) - ord('a')  # Get index (0-25)
            cipher_index = (a * index + b) % 26  # Apply Affine cipher formula
            cipher_text.append(chr(cipher_index + ord('a')))  # Convert back to character
        else:
            cipher_text.append(char)  # Keep spaces and non-alphabetic characters

    return ''.join(cipher_text)  # Return the joined cipher text

def affine_decrypt(cipher_text, a, b):
    """
    Decrypts the cipher text using the Affine cipher.
    
    Args:
        cipher_text (str): The text to be decrypted.
        a (int): The first cipher key.
        b (int): The second cipher key.

    Returns:
        str: The decrypted plain text.
    """
    # Ensure that a is coprime to 26
    if np.gcd(a, 26) != 1:
        raise ValueError("The first cipher key 'a' must be coprime to 26.")

    # Calculate the modular multiplicative inverse of a
    a_inv = pow(a, -1, 26)  # Using Python's built-in function to find inverse
    plain_text = []
    for char in cipher_text:
        if char.isalpha():  # Process only alphabetic characters
            index = ord(char) - ord('a')  # Get index (0-25)
            plain_index = (a_inv * (index - b)) % 26  # Apply inverse Affine cipher formula
            plain_text.append(chr(plain_index + ord('a')))  # Convert back to character
        else:
            plain_text.append(char)  # Keep spaces and non-alphabetic characters

    return ''.join(plain_text)  # Return the joined plain text

def main():
    choice = input("Affine encryption or decryption? (type 'encryption' or 'decryption'): \n").strip().lower()

    if choice == "encryption":
        plain_text = input("Enter your plain text: ").strip().lower()  # Accept lower case for consistency
        a, b = get_cipher_keys()  # Get and validate the cipher keys
        try:
            encrypted_text = affine_encrypt(plain_text, a, b)  # Encrypt the plain text
            print("Encrypted text:", encrypted_text)  # Output the encrypted text
        except ValueError as e:
            print(e)  # Handle error if keys are invalid

    elif choice == "decryption":
        cipher_text = input("Enter your cipher text: ").strip().lower()  # Accept lower case for consistency
        a, b = get_cipher_keys()  # Get and validate the cipher keys
        try:
            decrypted_text = affine_decrypt(cipher_text, a, b)  # Decrypt the cipher text
            print("Decrypted text:", decrypted_text)  # Output the decrypted text
        except ValueError as e:
            print(e)  # Handle error if keys are invalid

    else:
        print("Invalid choice. Please type 'encryption' or 'decryption'.")

if __name__ == "__main__":
    main()  # Run the main function