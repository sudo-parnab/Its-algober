# Hashing Module

## Overview

The **Hashing Module** provides functionalities for securely hashing strings using various algorithms, primarily SHA-256 and MD5. Hashing is a fundamental operation in computer science that transforms input data (such as strings) into a fixed-size string of characters, which is typically a hexadecimal number. This is widely used in data integrity verification, password storage, and digital signatures.

### Why Use Hashing?

Hashing ensures that sensitive data (like passwords) can be stored securely, and it allows for the verification of data integrity without exposing the original data. By using hash functions, you can:

- Store passwords securely (as hashes) rather than in plaintext.
- Verify data integrity by comparing hashes.
- Generate unique identifiers for data.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
  - [Hashing a String](#hashing-a-string)
  - [Verifying a Hash](#verifying-a-hash)
- [Supported Algorithms](#supported-algorithms)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- Hash strings using popular hashing algorithms (SHA-256 and MD5).
- Verify if a given string matches its hash.
- Simple and intuitive interface with clear error messages.
- Support for multiple hashing algorithms.

## Getting Started

### Prerequisites

To use this module, you need to have Python 3.x installed on your system. This module utilizes Python's built-in `hashlib` library, so no additional packages are required.

### Installation

1. Download the `hashing.py` file from this repository.
2. Place it in your project directory, or install it into your Python environment.

## Usage

The module provides two main functions: `hash_string` and `verify_hash`.

### Hashing a String

To hash a string, use the `hash_string` function. The function takes two arguments: the string to hash and the hashing algorithm to use (optional, defaults to SHA-256).

```python
from hashing import hash_string

# Example 1: Hash a string using SHA-256
hashed_value_sha256 = hash_string("Hello, World!", algorithm="sha256")
print(f"SHA-256 Hashed Value: {hashed_value_sha256}")

# Example 2: Hash a string using MD5
hashed_value_md5 = hash_string("Hello, World!", algorithm="md5")
print(f"MD5 Hashed Value: {hashed_value_md5}")
```

### Verifying A Hash

To verify if a string matches its hash, use the `verify_hash` function. This function takes three arguments: the original string, the hash to verify against, and the algorithm used to create the hash.

```python
from hashing import verify_hash

# Hash the original string
original_string = "Hello, World!"
hashed_value = hash_string(original_string, algorithm="sha256")

# Example 1: Verify the hash with the original string
is_valid = verify_hash(original_string, hashed_value, algorithm="sha256")
print(f"Is the hash valid? {is_valid}")  # Output: True

# Example 2: Verify the hash with a different string
is_valid_false = verify_hash("Goodbye, World!", hashed_value, algorithm="sha256")
print(f"Is the hash valid? {is_valid_false}")  # Output: False
```

### Supported Algorithms

The module currently supports the following hashing algorithms:

- SHA-256: A widely used cryptographic hash function that generates a 256-bit hash value.
- MD5: An older hash function that produces a 128-bit hash value. Note that MD5 is considered less secure than SHA-256 and is generally not recommended for sensitive data.

### Error Handling

The module includes error handling to manage unsupported algorithms and invalid inputs. Here are some examples of how errors are handled:

#### Unsupported Algorithm

If an unsupported algorithm is specified, a `ValueError` will be raised:

```python
try:
    hash_string("Hello, World!", algorithm="unsupported_algorithm")
except ValueError as e:
    print(e)  # Output: Unsupported algorithm: unsupported_algorithm. Use 'sha256' or 'md5'.
```

#### Invalid Input

If the input is not a string, a `TypeError` will be raised:

```python
try:
    hash_string(12345)  # Invalid input
except TypeError as e:
    print(e)  # Output: Input must be a string.
```

### Contributing

Contributions to the Hashing Module are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear messages.
Push your branch to your forked repository.
Submit a pull request explaining your changes.

### License

This project is licensed under the `MIT License`. See the LICENSE file for details.
