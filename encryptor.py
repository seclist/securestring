
from cryptography.fernet import Fernet

def main():
    choice = input("""
                    
                    Main Menu:
                    
                    1.  Encrypt
                    2.  Decrypt
                                    
                                    Enter your choice:  """)
    
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    else:
        print("\n Invalid Input")
        main()

def encrypt():
    # User inputs the string to encrypt
    message = input("Enter the message you want to encrypt: ")
    # Generate encryption key
    key = Fernet.generate_key()
    # Set Fernet as the encryption key
    fernet = Fernet(key)
    # Encrypts the message with the key
    encMessage = fernet.encrypt(message.encode())
    # Convert the encrypted bytes to a string
    encMessageString = encMessage.decode()
    # Prints original + encrypted string
    print("Original string:", message)
    print("Encrypted string:", encMessageString)
    print("Key: " + key.decode())  # Convert the key to a string for display

def decrypt():
    dec_message = input("Enter the message you want to decrypt: ")
    key = input("Enter your decryption key: ").strip().encode()  # Encode and strip spaces
    try:
        fernet = Fernet(key)
        decMessage = fernet.decrypt(dec_message.encode()).decode()
        print("Decrypted string:", decMessage)
    except Exception as e:
        print("Decryption failed. Make sure you entered the correct key.")
        print("Error:", str(e))  # Print the specific error message for further debugging


main()

