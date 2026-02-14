# Encrypting by Python 🔐

A pure Python encryption/decryption utility that converts messages to encrypted series of numbers and vice versa.

## Overview

This project implements a custom encryption algorithm that transforms text characters into numeric codes and can decrypt them back to the original message. It's useful for understanding encryption concepts and protecting simple text data.

## Features

✨ **Core Features:**
- 🔒 Text encryption to numeric codes
- 🔓 Numeric code decryption back to text
- 📁 File-based encryption/decryption
- 🎯 Support for letters, numbers, and special characters
- ⚡ Pure Python implementation (no external dependencies)

## Supported Characters

The encryption dictionary supports:
- **Letters:** A-Z (case-insensitive)
- **Numbers:** 0-9
- **Special Characters:** Space, Period (.), Exclamation (!), @, #, $, %, Comma (,), Question (?), Plus (+), Minus (-), Asterisk (*), Forward Slash (/), Apostrophe (')

## Installation

### Requirements
- Python 3.x
- No external dependencies required

### Setup

1. Clone the repository:
```bash
git clone https://github.com/j-shrma/encrypting-by-python.git
cd encrypting-by-python
```

2. No additional setup needed! The project uses only Python's standard library.

## Usage

### Quick Start

```python
from main import encryption, decryption

# Encrypt a message
encrypted = encryption("Hello World")
print(encrypted)  # Output: 32515344531344533300

# Decrypt a message
decrypted = decryption("32515344531344533300")
print(decrypted)  # Output: Hello world
```

### API Functions

#### `encryption(text)`
Converts text to encrypted numeric codes.

**Parameters:**
- `text` (str): The text to encrypt

**Returns:**
- str: Encrypted numeric string

**Raises:**
- `SyntaxError`: If an unsupported character is found

**Example:**
```python
result = encryption("Python")
```

#### `decryption(text)`
Converts encrypted numeric codes back to text.

**Parameters:**
- `text` (str): The encrypted numeric string

**Returns:**
- str: Decrypted text (capitalized)

**Raises:**
- `ValueError`: If encrypted text has odd number of digits or invalid code

**Example:**
```python
result = decryption("52122454435244")
```

#### `file_encryption(input_file)`
Encrypts the contents of a file and saves to a new file.

**Parameters:**
- `input_file` (str): Path to the file to encrypt

**Returns:**
- str: Encrypted content

**Example:**
```python
file_encryption("message.txt")
# Creates: message_encrypted.txt
```

#### `file_decryption(input_file)`
Decrypts the contents of an encrypted file and saves to a new file.

**Parameters:**
- `input_file` (str): Path to the encrypted file

**Returns:**
- str: Decrypted content

**Example:**
```python
file_decryption("message_encrypted.txt")
# Creates: message_decrypted.txt
```

## Encryption Algorithm

The encryption uses a character-to-numeric mapping dictionary:

| Character | Code | Character | Code | Character | Code |
|-----------|------|-----------|------|-----------|------|
| A | 11 | B | 21 | C | 31 |
| D | 41 | E | 51 | F | 12 |
| ... | ... | ... | ... | ... | ... |
| 0 | 60 | 1 | 61 | 2 | 62 |
| Space | 00 | Period | 90 | ! | 91 |

Each character is converted to its corresponding numeric code and concatenated to form the encrypted string.

## Example Test Files

The repository includes example test files:
- `test_encrypted.txt` - Sample encrypted data
- `test_decrypted.txt` - Corresponding decrypted data

## How It Works

1. **Encryption Process:**
   - Input text is converted to uppercase
   - Each character is looked up in the encryption dictionary
   - Numeric codes are concatenated together
   - Result is a numeric string

2. **Decryption Process:**
   - Numeric string is split into 2-digit codes
   - Each code is looked up in the reverse dictionary
   - Original characters are reconstructed
   - Result is capitalized

## Limitations

⚠️ **Important Notes:**
- The encryption is **NOT cryptographically secure** and should **NOT** be used for sensitive data
- It's intended for educational purposes and simple obfuscation
- The algorithm is deterministic and can be easily reversed
- For real security, use established cryptographic libraries like `cryptography` or `PyCryptodome`

## Use Cases

✅ **Suitable for:**
- Learning encryption concepts
- Simple text obfuscation
- Educational projects
- Game development (puzzle encoding)

❌ **NOT suitable for:**
- Securing sensitive/confidential information
- Password storage
- Financial data protection
- Personal identification protection

## Project Structure

```
encrypting-by-python/
├── main.py                      # Core encryption/decryption functions
├── USER_GUIDE.txt               # User guide documentation
├── test_encrypted.txt           # Example encrypted file
├── test_decrypted.txt           # Example decrypted file
├── JaiEncryption.exe            # Windows executable (optional)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── .github/                     # GitHub configuration
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Improve documentation

## License

This project is open source and available under the MIT License.

## Author

Created by [j-shrma](https://github.com/j-shrma)

## Disclaimer

This project is provided as-is for educational purposes. Use at your own risk. The author is not responsible for any misuse or data loss resulting from this software.

---

**Last Updated:** 2026-02-14 04:12:18
