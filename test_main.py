"""Test cases for encryption/decryption functions."""
import pytest
from main import encryption, decryption


def test_encryption_basic():
    """Test basic encryption functionality."""
    assert encryption("HELLO") == "3251232353"
    assert encryption("A") == "11"
    assert encryption("TEST") == "44515134"


def test_encryption_with_space():
    """Test encryption with spaces."""
    assert encryption("HELLO WORLD") == "32512323530025532423"


def test_decryption_basic():
    """Test basic decryption functionality."""
    assert decryption("3251232353") == "Hello"
    assert decryption("11") == "A"


def test_encryption_decryption_roundtrip():
    """Test that encryption followed by decryption returns original text."""
    original = "HELLO WORLD"
    encrypted = encryption(original)
    decrypted = decryption(encrypted)
    assert decrypted.upper() == original


def test_encryption_with_numbers():
    """Test encryption with numbers."""
    assert encryption("123") == "616263"


def test_encryption_with_special_chars():
    """Test encryption with special characters."""
    assert encryption("HELLO!") == "325123235391"
    assert encryption("A.B") == "119021"


def test_decryption_invalid_length():
    """Test that decryption raises error for invalid length."""
    with pytest.raises(ValueError, match="even number of digits"):
        decryption("123")  # Odd number of digits


def test_encryption_unsupported_char():
    """Test that encryption raises error for unsupported characters."""
    with pytest.raises(SyntaxError, match="not supported"):
        encryption("~")  # ~ is not in the encryption dictionary
