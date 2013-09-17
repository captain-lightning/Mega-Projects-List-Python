import sys

fibonacci = [0, 1]

for i in xrange(0, int(sys.argv[1])):
  fibonacci.append(sum(fibonacci[-2:]))

print fibonacci

# If you prefer the line by line approach:
#
#for number in fibonacci:
#  print number