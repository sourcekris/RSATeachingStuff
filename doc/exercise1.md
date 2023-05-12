# RSA Exercises - Python

## Exercise 1: Generating an RSA Public/Private Key Pair

### Overview

In this exercise, you will use Python to generate an RSA public/private key pair. 

### Step 1: Import the necessary modules

You will need to import the `random` and `Crypto.Util.number` modules to generate
the prime numbers, compute the modular inverse, and generate the RSA key pair,
respectively. Use the following code to import these modules:

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime
```

### Step 2: Choose two large prime numbers

Use the following code to generate two large prime numbers:

```python
p = getPrime(512)
q = getPrime(512)
```

This generates two 512-bit prime numbers `p` and `q` using the `getPrime` function 
from Crypto.Util.number.

### Step 3: Compute the product of the prime numbers

Use the following code to compute the product n of the prime numbers p and q:

```python
n = p * q
```

### Step 4: Choose a public exponent

We want to choose a public exponent `e` that is relatively prime to `(p-1)(q-1)`. For
simplicity and to help illustrate some real world problems later, lets take a well known 
prime that works for now. We can iterate on this part later. So use the following code to
set `e = 3`.

```python
e = 3
```

### Step 5: Compute the private exponent

Compute the private exponent `d` using the modular inverse of `e modulo (p-1)(q-1)` using
the following code:

```python
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
```

This code uses the `inverse()` function from `Crypto.Util.number` to compute the modular inverse
of e modulo phi.

### Step 6: Output the key pair

Use the following code to output the public key (n, e) and the private key (n, d):

```python
print(f"Public key: (n = {n}, e = {e})")
print(f"Private key: (n = {n}, d = {d})")
```

This will print the public key (n, e) and the private key (n, d) so you can see your work.

### Final: Code solution

The below is the summarized code from above, take some time to check your solution and then
add your own comments to the code. 

This part might seem overly simplified but its just a basis to get familiar with the math
and libraries we will use later.

```python
import random
from Crypto.Util.number import GCD, inverse, getPrime

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(f"Public key: (n = {n}, e = {e})")
print(f"Private key: (n = {n}, d = {d})")
```
