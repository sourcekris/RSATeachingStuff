# RSA Exercises - Python

## Exercise 4: Implementing RSA Encryption and Decryption using Object-Oriented Python

In this exercise, you will implement the concepts learned so far in object-oriented Python code.
You will create a class that represents the RSA encryption and decryption operations. The
class will have methods to generate an RSA key pair, encrypt a message, and decrypt a ciphertext.

This type of code is called "object oriented" and the object-oriented Python code we will write
encapsulates the related data and functions into a single class we will call `RSA`. The class 
serves as a blueprint or template for creating instances that can store data (such as the RSA
key pair) and perform operations (such as encryption and decryption) using that data.

By organizing the code into a class, we can leverage the concept of encapsulation,which allows
us to group related data and behavior together. This approach provides several benefits:

1. **Code Organization**: The class allows us to keep related data and methods together, making the 
   code more structured and easier to navigate.

2. **Reusability**: Once we create an instance of the RSA class, we can reuse it multiple times,
   generating new key pairs and performing encryption/decryption operations without duplicating
   code.

3. **State Management**: The class can store the key pair (public and private keys) as instance
   variables, ensuring that the relevant data is retained and accessible across different method
   calls within the same instance.

4. **Type Hinting**: With the class-based approach, we can use type hints to specify the expected
   types of method arguments and return values, enhancing code readability and enabling better
tooling support.

Object-oriented programming (OOP) promotes the use of classes and objects, which allows for better
organization, modularity, and reusability of code. It enables a more intuitive and structured
approach to solving complex problems by modeling real-world entities and their interactions.

To complete this exercise, follow the steps below:

### Step 1: Import the necessary modules

Ensure that you have imported the required modules as mentioned in Exercise 2:

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime, bytes_to_long, long_to_bytes
```

### Step 2: Create the `RSA` class

Define the `RSA` class that will handle the RSA encryption and decryption operations. The
class will have methods to generate the key pair, encrypt a message, and decrypt a ciphertext.

```python
class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_keypair(self):
        p = getPrime(512)
        q = getPrime(512)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.choose_public_exponent()
        d = inverse(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    def encrypt(self, message):
        n, e = self.public_key
        plaintext_long = bytes_to_long(message.encode())
        ciphertext = pow(plaintext_long, e, n)
        return ciphertext

    def decrypt(self, ciphertext):
        n, d = self.private_key
        decrypted_long = pow(ciphertext, d, n)
        original_message = long_to_bytes(decrypted_long).decode()
        return original_message

    def choose_public_exponent(self):
        # We only use 3 for now.
        return 3
```

### Step 3: Test the class

To test the `RSA` class, you can create an instance of the class, generate the key pair,
and perform encryption and decryption operations. For example:

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

### Step 4: Run the program

Save the code in a Python file and run it. You should see the ciphertext and the
decrypted message printed to the console.

By completing this exercise, you have implemented the RSA encryption and decryption operations
using object-oriented Python code. The `RSA` class encapsulates the functionality and provides
an organized and reusable structure for performing RSA operations.

### Final: Code solution

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime, bytes_to_long, long_to_bytes

class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_keypair(self):
        p = getPrime(512)
        q = getPrime(512)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.choose_public_exponent()
        d = inverse(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    def encrypt(self, message):
        n, e = self.public_key
        plaintext_long = bytes_to_long(message.encode())
        ciphertext = pow(plaintext_long, e, n)
        return ciphertext

    def decrypt(self, ciphertext):
        n, d = self.private_key
        decrypted_long = pow(ciphertext, d, n)
        original_message = long_to_bytes(decrypted_long).decode()
        return original_message

    def choose_public_exponent(self):
        # We only use 3 for now.
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

* [Exercise 5](exercise5.md)
* [Back to Index](index.md)