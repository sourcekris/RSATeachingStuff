#!/usr/bin/env python2

# OO_RSA_P2.py is the second part of the object oriented Python lesson.

import random
import libnum

class RSAPrivateKey(object):
  keytype = "private"
  e = 65537

  def __init__(self, bitlength):
    while True:
      self.p = libnum.generate_prime(bitlength)
      self.q = libnum.generate_prime(bitlength)

      # p and q must be co-prime.
      if libnum.gcd(self.p,self.q) == 1:
        break

    self.phi = (self.p - 1) * (self.q - 1)
    self.d = libnum.invmod(self.e, self.phi)
    self.n = self.p * self.q

  def String(self):
    return "RSAPrivateKey Object: {{{0},{1}}}".format(self.n, self.d)

  def Show(self):
    print self.String()
  
class RSAPublicKey(object):
  keytype = "public"

  def __init__(self, privateKey):
    self.n = privateKey.n
    self.e = privateKey.e

  def String(self):
    return "RSAPublicKey Object: {{{0},{1}}}".format(self.n, self.e)

  def Show(self):
    print self.String()

# RSAKeys inherits from the object base class and stores state and holds methods for constructing
# and printing an RSA Key Pair.
class RSAKeys(object):
  # keytype is a member that belongs to ALL instances of objects of type RSAPublicKey.
  keytype = "public/private key pair"
  # e is common to all key pairs I care about.
  e = 65537

  # __init__ is the class constructor method and is invoked automatically on instantiation.
  def __init__(self, bitlength):
    # construct a new key pair here in this constructor.
    self.PrivateKey = RSAPrivateKey(10)
    self.PublicKey = RSAPublicKey(self.PrivateKey)

  # String method returns a string with a pretty formated Key Pair.
  def String(self):
    out  = "Object: RSAKey Key Pair\n"
    out += "Public Key  {{n,e}}: {{{0},{1}}}\n".format(self.PublicKey.n, self.PublicKey.e)
    out += "Private Key {{n,d}}: {{{0},{1}}}\n".format(self.PrivateKey.n, self.PrivateKey.d)
    return out

  # Show method displays the pretty formated Key Pair on the console.
  def Show(self):
    print self.String()

  # PublicKey returns the PublicKey object.
  def PublicKey(self):
    return self.PublicKey

  # PrivateKey returns the PrivateKey object.
  def PrivateKey(self):
    return self.PrivateKey

if __name__ == "__main__":
  b = RSAKeys(10)
  b.PublicKey.Show()
  b.PrivateKey.Show()

