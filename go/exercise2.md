# RSA Exercises - Golang

## Exercise 2: Encrypting and Decrypting a Message using RSA

In this exercise, you will use the RSA key pair generated in Exercise 1 to encrypt and decrypt a simple string message. You will encrypt the message using the public key and decrypt it using the private key.

To complete this exercise, follow the steps below:

### Step 1: Import the necessary packages

Ensure that you have imported the required packages as mentioned in Exercise 1. For Exercise 2, note that we import 2 additional functions we'll use from the math/big package: `SetBytes` and `Bytes`.

```go
package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)
```

### Step 2: Retrieve the RSA key pair

We'll generate the RSA key pair in the same way we did in Exercise 1.

```go
func generatePrime(bits int) *big.Int {
	prime, err := rand.Prime(rand.Reader, bits)
	if err != nil {
		panic(err)
	}
	return prime
}

p := generatePrime(512)
q := generatePrime(512)
n := new(big.Int).Mul(p, q)
e := 3
phi := new(big.Int).Mul(new(big.Int).Sub(p, big.NewInt(1)), new(big.Int).Sub(q, big.NewInt(1)))
d := new(big.Int).ModInverse(big.NewInt(int64(e)), phi)
```

### Step 3: Encrypting a message

Choose a plaintext message that you want to encrypt. For example, let's use the message "Hello, RSA!".

```go
plaintext := "Hello, RSA!"
```

To encrypt the message, convert the plaintext to a big integer using `SetBytes` and raise it to the power of the public exponent `e` modulo `n` using the following code:

```go
plaintextBytes := []byte(plaintext)
plaintextBigInt := new(big.Int).SetBytes(plaintextBytes)
ciphertext := new(big.Int).Exp(plaintextBigInt, big.NewInt(int64(e)), n)
```

### Step 4: Decrypting the ciphertext

To decrypt the ciphertext, raise it to the power of the private exponent `d` modulo `n` using the following code:

```go
decryptedBigInt := new(big.Int).Exp(ciphertext, d, n)
```

### Step 5: Retrieve the original message

To retrieve the original message, convert the decrypted big integer back to a string using `Bytes` as follows:

```go
originalMessageBytes := decryptedBigInt.Bytes()
originalMessage := string(originalMessageBytes)
```

### Step 6: Ensure the ciphertext was decrypted properly

To verify nothing broke during encryption/decryption, check that our `plaintext` is the same as our `originalMessage`. To do so, we will use the Go built-in `fmt.Println()` which will print an error if the arguments do not match:

```go
fmt.Println(plaintext == originalMessage)
```

### Step 7: Output the results

Print the ciphertext, decrypted plaintext, and the original message using the following code:

```go
fmt.Printf("Ciphertext: %v\n", ciphertext)
fmt.Printf("Decrypted plaintext: %v\n", decryptedBigInt)
fmt.Printf("Original message: %v\n", originalMessage)
```

### Step 8: Run the program

Save the code in a Go file and run it. You should see the ciphertext, decrypted plaintext, and the original message printed to the console.

By completing this exercise, you have successfully encrypted a message using the RSA public key and then decrypted it using the corresponding private key.

### Final: Code solution

```go
package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)

func generatePrime(bits int) *big.Int {
	prime, err := rand.Prime(rand.Reader, bits)
	if err != nil {
		panic(err)
	}
	return prime
}

func main() {
	p := generatePrime(512)
	q := generatePrime(512)
	n := new(big.Int).Mul(p, q)
	e := 3
	phi := new(big.Int).Mul(new(big.Int).Sub(p, big.NewInt(1)), new(big.Int).Sub(q, big.NewInt(1)))
	d := new(big.Int).ModInverse(big.NewInt(int64(e)), phi)

	plaintext := "Hello, RSA!"
	plaintextBytes := []byte(plaintext)
	plaintextBigInt := new(big.Int).SetBytes(plaintextBytes)
	ciphertext := new(big.Int).Exp(plaintextBigInt, big.NewInt(int64(e)), n)

	decryptedBigInt := new(big.Int).Exp(ciphertext, d, n)
	originalMessageBytes := decryptedBigInt.Bytes()
	originalMessage := string(originalMessageBytes)

	fmt.Printf("Ciphertext: %v\n", ciphertext)
	fmt.Printf("Decrypted plaintext: %v\n", decryptedBigInt)
	fmt.Printf("Original message: %v\n", originalMessage)

	fmt.Println(plaintext == originalMessage)
}
```

### Next

* [Exercise 3](exercise3.md)
* [Back to Index](index.md)
