import sys

def is_prime(prime):
  for number in xrange(2, prime):
    if prime % number == 0:
      return False

  return True

number = int(sys.argv[1])
primes = []

for i in xrange(2, number):
  if number % i == 0:
    if is_prime(i):
      primes.append(i)
      number /= i

print primes