# RSA Exercises - Python

## Exercise 2: Encrypting and Decrypting a Message using RSA

In this exercise, you will use the RSA key pair generated in Exercise 1 to encrypt and decrypt
a simple string message. You will encrypt the message using the public key and decrypt it using
the private key.

To complete this exercise, follow the steps below:

### Step 1: Import the necessary modules

Ensure that you have imported the required modules as mentioned in Exercise 1. For exercise 2
note that we import 2 further functions we'll use from PyCryptodome `long_to_bytes` and
`bytes_to_long`:

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime, long_to_bytes, bytes_to_long
```

### Step 2: Retrieve the RSA key pair

We'll generate the RSA key pair in the same way we did in Exercise 1.

```python
p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
```

### Step 3: Encrypting a message

Choose a plaintext message that you want to encrypt. For example, let's use the message
"Hello, RSA!".

```python
plaintext = "Hello, RSA!"
```

To encrypt the message, convert the plaintext to a long integer using `bytes_to_long()` and
raise it to the power of the public exponent `e` modulo `n` using the following code:

```python
plaintext_long = bytes_to_long(plaintext.encode())
ciphertext = pow(plaintext_long, e, n)
```

### Step 4: Decrypting the ciphertext

To decrypt the ciphertext, raise it to the power of the private exponent `d` modulo `n`
using the following code:

```python
decrypted_long = pow(ciphertext, d, n)
```

### Step 5: Retrieve the original message

To retrieve the original message, convert the decrypted long integer back to a string using
`long_to_bytes()` as follows:

```python
original_message = long_to_bytes(decrypted_long).decode()
```

### Step 6: Ensure the ciphertext was decrypted properly

To verify nothing broke during on encryption / decryption, check that our `plaintext` is
the same as our `original_message`. To do so we will use the Python built in called
`assert()` which will raise an exception if the argument we provide is not `True`:

```python
assert(plaintext == original_message)
```

### Step 7: Output the results

Print the ciphertext, decrypted plaintext, and the original message using the following code:

```python
print("Ciphertext: {}".format(ciphertext))
print("Decrypted plaintext: {}".format(decrypted_plaintext))
print("Original message: {}".format(original_message))
```

### Step 8: Run the program

Save the code in a Python file and run it. You should see the ciphertext, decrypted plaintext, 
and the original message printed to the console.

By completing this exercise, you have successfully encrypted a message using the RSA public
key and then decrypted it using the corresponding private key.


### Final: Code solution

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime, long_to_bytes, bytes_to_long

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

plaintext_long = bytes_to_long(plaintext.encode())
ciphertext = pow(plaintext_long, e, n)
decrypted_long = pow(ciphertext, d, n)
original_message = long_to_bytes(decrypted_long).decode()

assert(plaintext == original_message)

print("Ciphertext: {}".format(ciphertext))
print("Decrypted plaintext: {}".format(decrypted_plaintext))
print("Original message: {}".format(original_message))
```