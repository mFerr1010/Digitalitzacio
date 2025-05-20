import hashlib

def hash_text(text):
    """
    Generates a SHA-256 hash for the given text.

    Args:
        text (str): The input text to hash.

    Returns:
        str: The resulting hash in hexadecimal format.
    """
    return hashlib.md5(text.encode('utf-8')).hexdigest()

print(hash_text("12345"))  # Example usage