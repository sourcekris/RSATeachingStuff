# RSA Exercises - Golang

## Exercise 3: Creating RSA Key Pair and Encryption/Decryption Functions

In this exercise, you will refactor the code learned so far into functions that can be called in a larger program. You will create three functions: `generateKeypair`, `encryptRSA`, and `decryptRSA`. The `generateKeypair` function will generate an RSA key pair, `encryptRSA` will encrypt a message using the public key, and `decryptRSA` will decrypt the ciphertext using the private key.

To complete this exercise, follow the steps below:

### Step 1: Import the necessary packages

Ensure that you have imported the required packages as mentioned in Exercise 2:

```go
package main

import (
	"crypto/rand"
	"math/big"
)
```

### Step 2: Create the `generateKeypair` function

Define the `generateKeypair` function, which will generate an RSA key pair. This function will take no arguments and return the public key `(n, e)` and private key `(n, d)` as two `*big.Int` values.

```go
func generateKeypair() (*big.Int, *big.Int, *big.Int, *big.Int) {
	p := generatePrime(512)
	q := generatePrime(512)
	n := new(big.Int).Mul(p, q)
	phi := new(big.Int).Mul(new(big.Int).Sub(p, big.NewInt(1)), new(big.Int).Sub(q, big.NewInt(1)))
	e := big.NewInt(3)
	d := new(big.Int).ModInverse(e, phi)
	return n, e, n, d
}
```

### Step 3: Create the `encryptRSA` function

Define the `encryptRSA` function, which will encrypt a message using the RSA public key. This function will take the message and the public key as arguments and return the ciphertext as a `*big.Int`.

```go
func encryptRSA(message string, publicKey *big.Int) *big.Int {
	n, e := publicKey, big.NewInt(3)
	plaintextBytes := []byte(message)
	plaintextBigInt := new(big.Int).SetBytes(plaintextBytes)
	ciphertext := new(big.Int).Exp(plaintextBigInt, e, n)
	return ciphertext
}
```

### Step 4: Create the `decryptRSA` function

Define the `decryptRSA` function, which will decrypt the ciphertext using the RSA private key. This function will take the ciphertext and the private key as arguments and return the decrypted plaintext as a string.

```go
func decryptRSA(ciphertext, privateKey *big.Int) string {
	n, d := privateKey, new(big.Int).ModInverse(big.NewInt(3), phi)
	decryptedBigInt := new(big.Int).Exp(ciphertext, d, n)
	originalMessageBytes := decryptedBigInt.Bytes()
	originalMessage := string(originalMessageBytes)
	return originalMessage
}
```

### Step 5: Test the functions

To test the functions, you can create a main program that calls these functions and performs encryption and decryption operations using the generated key pair. For example:

```go
package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)

func main() {
	// Generate RSA key pair
	publicKey, privateKey := generateKeypair()

	// Encrypt a message using the public key
	message := "Hello, RSA!"
	ciphertext := encryptRSA(message, publicKey)
	fmt.Printf("Ciphertext: %v\n", ciphertext)

	// Decrypt the ciphertext using the private key
	decryptedMessage := decryptRSA(ciphertext, privateKey)
	fmt.Printf("Decrypted message: %v\n", decryptedMessage)
}
```

### Step 6: Run the program

Save the code in a Go file and run it. You should see the ciphertext and the decrypted message printed to the console.

By completing this exercise, you have refactored the code into functions that can be reused and called in a larger program. This modular approach allows for better code organization and maintainability.

### Next

* [Exercise 4](exercise4.md)
* [Back to Index](index.md)
```
