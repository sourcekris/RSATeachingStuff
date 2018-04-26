#!/usr/bin/env python2

# OO_RSA_P1.py is the first part of the object oriented Python lesson. We want to demonstrate 
# what a class / object are in python, how they store state and have methods. How they are 
# constructed and how they are defined. The difference between members that are shared and members
# that are private etc.

import random
import libnum

# RSAKeys inherits from the object base class and stores state and holds methods for constructing
# and printing an RSA Key Pair.
class RSAKeys(object):
  # type is a member that belongs to ALL instances of objects of type RSAPublicKey.
  type = "public/private key pair"
  # e is common to all key pairs I care about.
  e = 65537

  # __init__ is the class constructor method and is invoked automatically on instantiation.
  def __init__(self, bitlength):
    # construct a new key pair here in this constructor.
    while True:
      self.p = libnum.generater_prime(bitlength)
      self.q = libnum.generate_prime(bitlength)

      # p and q must be co-prime.
      if libnum.gcd(self.p,self.q) == 1:
        break

    self.phi = (self.p - 1) * (self.q - 1)
    self.d = libnum.invmod(self.e, self.phi)
    self.n = self.p * self.q


  # String method returns a string with a pretty formated Key Pair.
  def String(self):
    out  = "Object: RSAKey Key Pair\n"
    out += "Public Key  {{n,e}}: {{{0},{1}}}\n".format(self.n, self.e)
    out += "Private Key {{n,d}}: {{{0},{1}}}\n".format(self.n, self.d)
    return out

  # Show method displays the pretty formated Key Pair on the console.
  def Show(self):
    print self.String()

  # PublicKey returns a tuple of the PublicKey components.
  def PublicKey(self):
    # TODO(flypig2016): implement me
    pass

  # PrivateKey returns a tuple of the PrivateKey components.
  def PrivateKey(self):
    # TODO(flypig2016): implement me
    pass

if __name__ == "__main__":
  b = RSAKeys(10)
  b.Show()

  # excercises ?

  # 1. Write the methods for returning just the public / private keys 
  # 2. Write some stuff in the main function to print some of the members of an RSAKey object
  # 3. Construct a few more keys. Compare the value of e across them. Compare the value of the type member across them
  # 4. Write a class just for PublicKeys and another one just for Private Keys. Have RSAKey instantiate an object of each.



