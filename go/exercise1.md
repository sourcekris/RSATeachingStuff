# RSA Exercises - Golang

## Exercise 1: Generating an RSA Public/Private Key Pair

### Overview

In this exercise, you will use Golang to generate an RSA public/private key pair.

### Step 1: Import the necessary packages

You will need to import the `crypto/rand` and `math/big` packages to generate
the prime numbers, compute the modular inverse, and generate the RSA key pair, respectively. Use the following code to import these packages:

```go
package main

import (
	"crypto/rand"
	"math/big"
)
```

### Step 2: Choose two large prime numbers

Use the following code to generate two large prime numbers:

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
```

This generates two 512-bit prime numbers `p` and `q` using the `rand.Prime` function from the `crypto/rand` package.

### Step 3: Compute the product of the prime numbers

Use the following code to compute the product n of the prime numbers p and q:

```go
n := new(big.Int).Mul(p, q)
```

### Step 4: Choose a public exponent

We want to choose a public exponent `e` that is relatively prime to `(p-1)(q-1)`. For simplicity and to help illustrate some real-world problems later, let's take a well-known prime that works for now. We can iterate on this part later. So use the following code to set `e = 3`.

```go
e := 3
```

### Step 5: Compute the private exponent

Compute the private exponent `d` using the modular inverse of `e modulo (p-1)(q-1)` using the following code:

```go
phi := new(big.Int).Mul(new(big.Int).Sub(p, big.NewInt(1)), new(big.Int).Sub(q, big.NewInt(1)))
d := new(big.Int).ModInverse(big.NewInt(int64(e)), phi)
```

### Step 6: Output the key pair

Use the following code to output the public key (n, e) and the private key (n, d):

```go
fmt.Printf("Public key: (n = %v, e = %v)\n", n, e)
fmt.Printf("Private key: (n = %v, d = %v)\n", n, d)
```

This will print the public key (n, e) and the private key (n, d) so you can see your work.

### Final: Code solution

The below is the summarized code from above. Take some time to check your solution and then add your own comments to the code. This part might seem overly simplified, but it's just a basis to get familiar with the math and libraries we will use later.

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

	fmt.Printf("Public key: (n = %v, e = %v)\n", n, e)
	fmt.Printf("Private key: (n = %v, d = %v)\n", n, d)
}
```

### Next

* [Exercise 2](exercise2.md)
* [Back to Index](index.md)
