import sys

def is_prime(prime):
  for number in xrange(2, prime):
    if prime % number == 0:
      return False

  return True

def next_prime(current):
  current += 1
  while not is_prime(current):
    current += 1
  return current

i = 2

while raw_input("Print the next Prime Number? ")[:1].lower() != "n":
  print i
  i = next_prime(i)
  