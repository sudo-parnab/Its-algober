import hashlib

def hash_string(input_string: str, algorithm: str = 'sha256') -> str:
    """
    Hashes a given input string using the specified hashing algorithm.
    
    Args:
        input_string (str): The string to be hashed.
        algorithm (str): The hashing algorithm to use. Defaults to 'sha256'.
                         Options: 'sha256', 'md5'.
    
    Returns:
        str: The hexadecimal representation of the hashed string.
    
    Raises:
        ValueError: If an unsupported algorithm is provided.
    """
    
    # Supported algorithms
    algorithms = {
        'sha256': hashlib.sha256,
        'md5': hashlib.md5,
    }
    
    # Check if the specified algorithm is supported
    if algorithm not in algorithms:
        raise ValueError(f"Unsupported algorithm: {algorithm}. Use 'sha256' or 'md5'.")
    
    # Create a hash object
    hash_object = algorithms[algorithm]()
    
    # Encode the string and update the hash object
    hash_object.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return hash_object.hexdigest()

def verify_hash(input_string: str, hashed_string: str, algorithm: str = 'sha256') -> bool:
    """
    Verifies if the hashed string matches the hash of the input string using the specified algorithm.
    
    Args:
        input_string (str): The original string to verify.
        hashed_string (str): The previously hashed string to compare against.
        algorithm (str): The hashing algorithm used for hashing. Defaults to 'sha256'.
    
    Returns:
        bool: True if the hashes match, False otherwise.
    
    Raises:
        ValueError: If an unsupported algorithm is provided.
    """
    
    # Hash the input string
    new_hash = hash_string(input_string, algorithm)
    
    # Compare the new hash with the given hash
    return new_hash == hashed_string

if __name__ == "__main__":
    # Example usage
    sample_string = "Hello, World!"
    algorithm = 'sha256'
    
    hashed = hash_string(sample_string, algorithm)
    print(f"Original String: {sample_string}")
    print(f"Hashed String using {algorithm}: {hashed}")
    
    # Verify the hash
    is_valid = verify_hash(sample_string, hashed, algorithm)
    print(f"Is the hash valid? {is_valid}")
