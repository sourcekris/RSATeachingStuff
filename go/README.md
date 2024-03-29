# RSA Excercises - Golang

## Overview

This repo is a set of exercises with background info on writing a small Go program to encrypt
and decrypt messages with RSA. Hopefully along the way you learn some things about Go.

## RSA History and Background

RSA is a public key cryptography algorithm named after its inventors: Ron Rivest, Adi Shamir, and
Leonard Adleman. It was first introduced in 1977 and has since become one of the most widely used 
encryption techniques in the world.

Unlike traditional symmetric encryption algorithms, which use a single key for both encryption and
decryption, public key algorithms use two keys: one to encrypt the message (public key) and another
to decrypt it (private key). The public key is shared with anyone who wants to send a message,
while the private key is kept secret and known only to the intended recipient. RSA is based on the
mathematical principles of prime factorization and the difficulty of factoring large composite
numbers.

## RSA Principles

RSA is based on the fact that it is computationally infeasible to factor the product of two large
prime numbers. The security of the RSA algorithm is based on the difficulty of factoring the
product of two large primes, which is the basis for generating the public and private keys.

To generate a public key, two large prime numbers (`p` and `q`) are selected, and their product
(`n`) is computed. Then, a number `e` (the public exponent) is chosen such that it is relatively
prime to `(p-1)(q-1)`. The public key is then the pair (`n`, `e`). The private key (`d`) is
generated by computing the modular inverse of `e` modulo `(p-1)(q-1)`, and this number is kept
secret and is only known by the recipient.

## RSA Math Operations

The RSA algorithm is based on modular arithmetic and exponentiation. The encryption process is
as follows: given a plaintext message `m`, the sender computes the ciphertext `c` by raising `m`
to the power of the public exponent `e` modulo `n`. 

That is, `c ≡ m^e (mod n)`.

To decrypt the ciphertext `c`, the recipient raises `c` to the power of the private exponent `d`
modulo `n`. 

That is, `m ≡ c^d (mod n)`. 

The recipient can then recover the original plaintext message `m`.

```
    Public Key (e, n)                 Private Key (d, n)
  +-------------------+              +-------------------+
  |                   |              |                   |
  |    Encryption     |              |    Decryption     |
  |                   |              |                   |
  +-------------------+              +-------------------+
             |                                  |
             |                                  |
             v                                  v
  +-------------------+              +-------------------+
  |                   |              |                   |
  |   Ciphertext (c)  |              |   Plaintext (m)   |
  |                   |              |                   |
  +-------------------+              +-------------------+
```

It is important to repeat and note that the security of RSA relies on the difficulty of factoring
the product of two large primes. If an attacker can factor this product, they can easily compute
the private key and decrypt any messages sent using the public key. Therefore, the size of the
primes used in the RSA algorithm is critical to its security.

## Exercises

In the following exercises we will work with Go to implement "textbook RSA". Textbook RSA
refers to implementations of the RSA algorithm without any additional security measures or
padding schemes.

## Table of Contents

* [Introduction](README.md)
* [Setup](setup.md)
  * [Setup Pre-work Virtualbox](../virtualbox.md)
  * [Setup Pre-work Windows Subsystem for Linux](../wsl.md)
* [Exercise 1: Generating an RSA Public/Private Key Pair](exercise1.md)
* [Exercise 2: Encrypting and Decrypting a Message](exercise2.md)
* [Exercise 3: Creating RSA Key Pair and Encryption/Decryption Functions](exercise3.md)
* [Exercise 4: Implementing RSA Encryption and Decryption using Object-Oriented Go](exercise4.md)
* [Exercise 5: Homework and followup ideas](exercise5.md)


## Author

* [Kris Hunt](https://github.com/sourcekris)
