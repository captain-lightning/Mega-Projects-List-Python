# Impossible to go beyond platform's floating point C library without implementing my own algorithm,
# A much less accurate but much more precise derivation is substituted after 48 decimal places
import decimal
import math, sys

precision = int(sys.argv[1])

if len(sys.argv) > 2 or precision > 48:

    x = decimal.Decimal(22.0)
    y = decimal.Decimal(7.0)
    decimal.getcontext().prec = precision

    print x / y

else:
  print ("{0:.%df}" % precision).format(math.pi)