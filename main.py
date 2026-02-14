import os

# Optimized encryption dictionary - kept for custom mapping
encryption_dict = {
    "A": 11, "B": 21, "C": 31, "D": 41,
    "E": 51, "F": 12, "G": 22, "H": 32,
    "I": 42, "J": 52, "K": 13, "L": 23,
    "M": 33, "N": 43, "O": 53, "P": 14,
    "Q": 66, "R": 24, "S": 34, "T": 44,
    "U": 54, "V": 15, "W": 25, "X": 35,
    "Y": 45, "Z": 55, " ": "00", ".": 90,
    "!": 91, "@": 92, "#": 93, "$": 94,
    "%": 95, ",": 96, "?": 97, "+": 98,
    "-": 99, "*": 10, "/": 20, "'": 30,
    # Numbers 0-9 added below
    "0": 60, "1": 61, "2": 62, "3": 63,
    "4": 64, "5": 65, "6": 67, "7": 68,
    "8": 69, "9": 70
}

# Pre-compute reversed dict once for better performance
reversed_dict = {value: key for key, value in encryption_dict.items()}


def encryption(text: str) -> str:
    """Encrypt text using dictionary mapping. Uses list comprehension for better performance."""
    result = []
    for char in text.upper():
        if char in encryption_dict:
            result.append(str(encryption_dict[char]))
        else:
            raise SyntaxError(f"Character '{char}' is not supported")
    return ''.join(result)  # More efficient than += in loop


def decryption(text: str) -> str:
    """Decrypt text by parsing 2-digit codes. Optimized with list comprehension."""
    if len(text) % 2 != 0:
        raise ValueError("Encrypted text must have an even number of digits")
    
    result = []
    for i in range(0, len(text), 2):
        code = text[i:i+2]
        # Try string lookup first, then int
        if code in reversed_dict:
            result.append(reversed_dict[code])
        elif int(code) in reversed_dict:
            result.append(reversed_dict[int(code)])
        else:
            raise ValueError(f"Invalid encrypted code: {code}")
    
    return ''.join(result).capitalize()


def file_encryption(input_file: str) -> str:
    """Encrypt contents of a file and save to a new file."""
    if not os.path.exists(input_file):
        raise FileNotFoundError("Invalid file path")
    
    with open(input_file, "r") as file:
        text = file.read()
    
    encrypted = encryption(text)
    filename, ext = os.path.splitext(input_file)
    output_file = filename + '_encrypted' + ext
    
    with open(output_file, "w") as f:
        f.write(encrypted)
    
    print(f"✅ Encrypted file created: {output_file}")
    return encrypted


def file_decryption(input_file: str) -> str:
    """Decrypt contents of a file and save to a new file."""
    if not os.path.exists(input_file):
        raise FileNotFoundError("Invalid file path")
    
    with open(input_file, "r") as file:
        text = file.read()
    
    decrypted = decryption(text)
    filename, ext = os.path.splitext(input_file)
    
    if filename.endswith('_encrypted'):
        output_file = filename.replace('_encrypted', '_decrypted') + ext
    else:
        output_file = filename + '_decrypted' + ext
    
    with open(output_file, "w") as f:
        f.write(decrypted)
    
    print(f"✅ Decrypted file created: {output_file}")
    return decrypted


def main():
    """Main interactive menu for encryption/decryption."""
    print("🔐 Welcome to Jai's Encryption System")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt Message")
        print("2. Encrypt from a file")
        print("3. Decrypt Message")
        print("4. Decrypt to a file")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            try:
                msg = input("Enter message: ")
                print("Encrypted:", encryption(msg))
            except SyntaxError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "2":
            try:
                input_filepath = input("Enter the file path: ")
                file_encryption(input_filepath)
            except FileNotFoundError as e:
                print(f"❌ Error: {e}. Please try again.")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == "3":
            try:
                code = input("Enter encrypted numbers: ")
                print("Decrypted:", decryption(code))
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "4":
            try:
                input_filepath = input("Enter the file path: ")
                file_decryption(input_filepath)
            except FileNotFoundError as e:
                print(f"❌ Error: {e}. Please try again.")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == "5":
            print("Goodbye 👋")
            break
        
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
