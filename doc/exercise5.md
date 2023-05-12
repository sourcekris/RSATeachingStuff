# RSA Exercises - Python

## Exercise 5: Adding Type Hints to the RSA Encryption and Decryption Class

In this exercise, you will modify the existing RSA encryption and decryption class to add
type hints, allowing for better code readability and understanding. You will use Python's
built-in type hinting feature to specify the expected types of function arguments and return
values.

To complete this exercise, follow the steps below:

### Step 1: Update the `RSA` class with type hints

Modify the existing `RSA` class to include type hints for method arguments and return values.
Add the appropriate type hints based on the expected types of the variables. Here's an example of
how the updated class could look:

```python
from typing import Tuple
import random
from Crypto.Util.number import GCD, inverse, getPrime, bytes_to_long, long_to_bytes

class RSA:
    def __init__(self) -> None:
        self.public_key: Tuple[int, int] = None
        self.private_key: Tuple[int, int] = None

    def generate_keypair(self) -> None:
        p: int = getPrime(512)
        q: int = getPrime(512)
        n: int = p * q
        phi: int = (p - 1) * (q - 1)
        e: int = self.choose_public_exponent()
        d: int = inverse(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    def encrypt(self, message: str) -> int:
        n: int = self.public_key[0]
        e: int = self.public_key[1]
        plaintext_long: int = bytes_to_long(message.encode())
        ciphertext: int = pow(plaintext_long, e, n)
        return ciphertext

    def decrypt(self, ciphertext: int) -> str:
        n: int = self.private_key[0]
        d: int = self.private_key[1]
        decrypted_long: int = pow(ciphertext, d, n)
        original_message: str = long_to_bytes(decrypted_long).decode()
        return original_message

    def choose_public_exponent(self) -> int:
        return 3
```

## Step 2: Test the updated class

Create an instance of the `RSA` class, generate the key pair, and perform encryption and decryption
operations as before. The type hints will provide clearer information about the expected argument
and return types. For example:

```python
rsa = RSA()

# Generate RSA key pair
rsa.generate_keypair()

# Encrypt a message
message = "Hello, RSA!"
ciphertext = rsa.encrypt(message)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_message = rsa.decrypt(ciphertext)
print("Decrypted message:", decrypted_message)
```

### Step 3: Run the program

Save the code in a Python file and run it. The program should execute without errors, and you
should see the ciphertext and decrypted message printed to the console.

By completing this exercise, you have enhanced the RSA encryption and decryption class by adding
type hints to improve code clarity and facilitate understanding. Type hints are a valuable tool
for documenting and communicating the expected types of function arguments and return values.

### Final: Code solution

```python
from typing import Tuple
import random
from Crypto.Util.number import GCD, inverse, getPrime, bytes_to_long, long_to_bytes

class RSA:
    def __init__(self) -> None:
        self.public_key: Tuple[int, int] = None
        self.private_key: Tuple[int, int] = None

    def generate_keypair(self) -> None:
        p: int = getPrime(512)
        q: int = getPrime(512)
        n: int = p * q
        phi: int = (p - 1) * (q - 1)
        e: int = self.choose_public_exponent()
        d: int = inverse(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    def encrypt(self, message: str) -> int:
        n: int = self.public_key[0]
        e: int = self.public_key[1]
        plaintext_long: int = bytes_to_long(message.encode())
        ciphertext: int = pow(plaintext_long, e, n)
        return ciphertext

    def decrypt(self, ciphertext: int) -> str:
        n: int = self.private_key[0]
        d: int = self.private_key[1]
        decrypted_long: int = pow(ciphertext, d, n)
        original_message: str = long_to_bytes(decrypted_long).decode()
        return original_message

    def choose_public_exponent(self) -> int:
        return 3

rsa = RSA()

# Generate RSA key pair
rsa.generate_keypair()

# Encrypt a message
message = "Hello, RSA!"
ciphertext = rsa.encrypt(message)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_message = rsa.decrypt(ciphertext)
print("Decrypted message:", decrypted_message)
```

### Next

* [Back to Index](index.md)