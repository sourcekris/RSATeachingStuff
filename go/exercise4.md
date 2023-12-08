# RSA Exercises - Golang

## Exercise 4: Implementing RSA Encryption and Decryption using Object-Oriented Golang

In this exercise, you will implement the concepts learned so far in object-oriented Golang code.
You will create a struct that represents the RSA encryption and decryption operations. The
struct will have methods to generate an RSA key pair, encrypt a message, and decrypt a ciphertext.

This type of code is called "object oriented," and the object-oriented Golang code we will write
encapsulates the related data and functions into a single struct we will call `RSA`. The struct
serves as a blueprint or template for creating instances that can store data (such as the RSA
key pair) and perform operations (such as encryption and decryption) using that data.

By organizing the code into a struct, we can leverage the concept of encapsulation, which allows
us to group related data and behavior together. This approach provides several benefits:

1. **Code Organization**: The struct allows us to keep related data and methods together, making the
   code more structured and easier to navigate.

2. **Reusability**: Once we create an instance of the RSA struct, we can reuse it multiple times,
   generating new key pairs and performing encryption/decryption operations without duplicating
   code.

3. **State Management**: The struct can store the key pair (public and private keys) as struct
   fields, ensuring that the relevant data is retained and accessible across different method
   calls within the same instance.

4. **Type Safety**: With the struct-based approach, we can use method receivers to specify the
   expected types of method arguments, enhancing code readability and enabling better tooling
   support.

Object-oriented programming (OOP) promotes the use of structs and methods, which allows for better
organization, modularity, and reusability of code. It enables a more intuitive and structured
approach to solving complex problems by modeling real-world entities and their interactions.

To complete this exercise, follow the steps below:

### Step 1: Import the necessary packages

Ensure that you have imported the required packages as mentioned in Exercise 2:

```go
package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)
```

### Step 2: Create the `RSA` struct

Define the `RSA` struct that will handle the RSA encryption and decryption operations. The
struct will have methods to generate the key pair, encrypt a message, and decrypt a ciphertext.

```go
type RSA struct {
	publicKey  *big.Int
	privateKey *big.Int
}

func (r *RSA) generateKeypair() {
	p := generatePrime(512)
	q := generatePrime(512)
	n := new(big.Int).Mul(p, q)
	phi := new(big.Int).Mul(new(big.Int).Sub(p, big.NewInt(1)), new(big.Int).Sub(q, big.NewInt(1)))
	e := r.choosePublicExponent()
	d := new(big.Int).ModInverse(e, phi)
	r.publicKey = n
	r.privateKey = d
}

func (r *RSA) encrypt(message string) *big.Int {
	n, e := r.publicKey, big.NewInt(3)
	plaintextBytes := []byte(message)
	plaintextBigInt := new(big.Int).SetBytes(plaintextBytes)
	ciphertext := new(big.Int).Exp(plaintextBigInt, e, n)
	return ciphertext
}

func (r *RSA) decrypt(ciphertext *big.Int) string {
	n, d := r.privateKey, new(big.Int).ModInverse(big.NewInt(3), phi)
	decryptedBigInt := new(big.Int).Exp(ciphertext, d, n)
	originalMessageBytes := decryptedBigInt.Bytes()
	originalMessage := string(originalMessageBytes)
	return originalMessage
}

func (r *RSA) choosePublicExponent() *big.Int {
	// We only use 3 for now.
	return big.NewInt(3)
}
```

### Step 3: Test the struct

To test the `RSA` struct, you can create an instance of the struct, generate the key pair,
and perform encryption and decryption operations. For example:

```go
package main

func main() {
	// Create an instance of RSA struct
	rsa := RSA{}

	// Generate RSA key pair
	rsa.generateKeypair()

	// Encrypt a message
	message := "Hello, RSA!"
	ciphertext := rsa.encrypt(message)
	fmt.Printf("Ciphertext: %v\n", ciphertext)

	// Decrypt the ciphertext
	decryptedMessage := rsa.decrypt(ciphertext)
	fmt.Printf("Decrypted message: %v\n", decryptedMessage)
}
```

### Step 4: Run the program

Save the code in a Go file and run it. You should see the ciphertext and the
decrypted message printed to the console.

By completing this exercise, you have implemented the RSA encryption and decryption operations
using object-oriented Golang code. The `RSA` struct encapsulates the functionality and provides
an organized and reusable structure for performing RSA operations.

### Next

* [Exercise 5](exercise5.md)
* [Back to Index](index.md)
```
