# RSA Exercises - Python

## Exercise 3: Creating RSA Key Pair and Encryption/Decryption Functions

In this exercise, you will refactor the code learned so far into functions that can be
called in a larger program. You will create three functions: `generate_keypair`,
`encrypt_rsa`, and `decrypt_rsa`. The `generate_keypair` function will generate an RSA
key pair, `encrypt_rsa` will encrypt a message using the public key, and `decrypt_rsa`
will decrypt the ciphertext using the private key.

To complete this exercise, follow the steps below:

### Step 1: Import the necessary modules

Ensure that you have imported the required modules as mentioned in Exercise 2:

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime, bytes_to_long, long_to_bytes
```

### Step 2: Create the `generate_keypair` function

Define the `generate_keypair` function, which will generate an RSA key pair. This function
will take no arguments and return the public key `(n, e)` and private key `(n, d)` as a tuple.

```python
def generate_keypair():
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    d = inverse(e, phi)
    return (n, e), (n, d)
```

### Step 3: Create the `encrypt_rsa` function

Define the `encrypt_rsa` function, which will encrypt a message using the RSA public key. This
function will take the message and the public key as arguments and return the ciphertext.

```python
def encrypt_rsa(message, public_key):
    n, e = public_key
    plaintext_long = bytes_to_long(message.encode())
    ciphertext = pow(plaintext_long, e, n)
    return ciphertext
```

### Step 4: Create the `decrypt_rsa` function

Define the `decrypt_rsa` function, which will decrypt the ciphertext using the RSA private key.
This function will take the ciphertext and the private key as arguments and return the decrypted
plaintext.

```python
def decrypt_rsa(ciphertext, private_key):
    n, d = private_key
    decrypted_long = pow(ciphertext, d, n)
    original_message = long_to_bytes(decrypted_long).decode()
    return original_message
```

### Step 5: Test the functions

To test the functions, you can create a main program that calls these functions and performs
encryption and decryption operations using the generated key pair. For example:

```python
# Generate RSA key pair
public_key, private_key = generate_keypair()

# Encrypt a message using the public key
message = "Hello, RSA!"
ciphertext = encrypt_rsa(message, public_key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext using the private key
decrypted_message = decrypt_rsa(ciphertext, private_key)
print(f"Decrypted message: {decrypted_message}")
```

### Step 6: Run the program

Save the code in a Python file and run it. You should see the ciphertext and the
decrypted message printed to the console.

By completing this exercise, you have refactored the code into functions that can be 
reused and called in a larger program. This modular approach allows for better code
organization and maintainability.

### Final: Code solution

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime, bytes_to_long, long_to_bytes

def generate_keypair():
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    d = inverse(e, phi)
    return (n, e), (n, d)

def encrypt_rsa(message, public_key):
    n, e = public_key
    plaintext_long = bytes_to_long(message.encode())
    ciphertext = pow(plaintext_long, e, n)
    return ciphertext

def decrypt_rsa(ciphertext, private_key):
    n, d = private_key
    decrypted_long = pow(ciphertext, d, n)
    original_message = long_to_bytes(decrypted_long).decode()
    return original_message

# Generate RSA key pair
public_key, private_key = generate_keypair()

# Encrypt a message using the public key
message = "Hello, RSA!"
ciphertext = encrypt_rsa(message, public_key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext using the private key
decrypted_message = decrypt_rsa(ciphertext, private_key)
print(f"Decrypted message: {decrypted_message}")
```

### Next

* [Exercise 4](exercise4.md)
* [Back to Index](index.md)