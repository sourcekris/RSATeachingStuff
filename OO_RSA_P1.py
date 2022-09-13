#!/usr/bin/env python3

# OO_RSA_P1.py is the first object oriented pattern. It demonstrates an initial implementation
# of a class / object are in python, how it stores state and has methods. How it is are 
# constructed and how it is defined. The difference between members that are shared and members
# that are private etc.

import random
from Crypto.Util.number import GCD, inverse

# isPrime tests if x is prime or not by trial division.
# TODO: Find a more efficient method!
def isPrime(x):
  for i in range(2, x-1):
    if x % i == 0:
      return False
  return True

# generatPrime returns a prime number of bit length bits.
def generatePrime(bits):
  while True:
    value = random.getrandbits(bits)
    if isPrime(value):
      return value

# RSAKeys inherits from the object base class and stores state and holds methods for constructing
# and printing an RSA Key Pair.
class RSAKeys(object):
  # type is a member that belongs to ALL instances of objects of type RSAPublicKey.
  keytype = "public/private key pair"
  # e is common to all key pairs I care about.
  e = 65537

  # __init__ is the class constructor method and is invoked automatically on instantiation.
  def __init__(self, bitlength):
    # construct a new key pair here in this constructor.
    while True:
      self.p = generatePrime(bitlength)
      self.q = generatePrime(bitlength)

      # p and q must be co-prime.
      if GCD(self.p,self.q) == 1:
        break

    self.phi = (self.p - 1) * (self.q - 1)
    self.d = inverse(self.e, self.phi)
    self.n = self.p * self.q


  # String method returns a string with a pretty formated Key Pair.
  def String(self):
    out  = "Object: RSAKey Key Pair\n"
    out += "Public Key  {{n,e}}: {{{0},{1}}}\n".format(self.n, self.e)
    out += "Private Key {{n,d}}: {{{0},{1}}}\n".format(self.n, self.d)
    return out

  # Show method displays the pretty formated Key Pair on the console.
  def Show(self):
    print(self.String())

  # PublicKey returns a tuple of the PublicKey components.
  def PublicKey(self):
    # TODO: implement me
    pass

  # PrivateKey returns a tuple of the PrivateKey components.
  def PrivateKey(self):
    # TODO: implement me
    pass

if __name__ == "__main__":
  b = RSAKeys(10)
  b.Show()

  # excercises ?

  # 1. Write the methods for returning just the public / private keys 
  # 2. Write some stuff in the main function to print some of the members of an RSAKey object
  # 3. Construct a few more keys. Compare the value of e across them. Compare the value of the keytype member across them
  # 4. Write a class just for PublicKeys and another one just for Private Keys. Have RSAKey instantiate an object of each.



