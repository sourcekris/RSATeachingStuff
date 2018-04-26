#!/usr/bin/env python2

import random
import libnum

# isPrime tests if x is prime or not by trial division.
# TODO(flypig2016): Find a more efficient method!
def isPrime(x):
  for i in xrange(2, x-1):
    if x % i == 0:
      return False
  return True

# generatPrime returns a prime number of bit length bits.
def generatePrime(bits):
  while True:
    value = random.getrandbits(bits)
    if isPrime(value):
      return value

class RSAKeys(object):
  # type is a member that belongs to ALL instances of objects of type RSAPublicKey.
  type = "public"
  # e is common to all key pairs I care about.
  e = 65537

  def __init__(self, bitlength):
    # construct a new key pair here in this constructor.
    while True:
      self.p = generatePrime(bitlength)
      self.q = generatePrime(bitlength)

      # p and q must be co-prime.
      if libnum.gcd(self.p,self.q) == 1:
        break

    self.phi = (self.p - 1) * (self.q - 1)
    self.d = libnum.invmod(self.e, self.phi)
    self.n = self.p * self.q


  def String(self):
    out  = "Object: RSAKey Key Pair\n"
    out += "Public Key  {{n,e}}: {{{0},{1}}}\n".format(self.n, self.e)
    out += "Private Key {{n,d}}: {{{0},{1}}}\n".format(self.n, self.d)
    return out

  def Show(self):
    print self.String()

if __name__ == "__main__":
  b = RSAKeys(10)
  b.Show()

