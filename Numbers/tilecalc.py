import re

price_per_tile = raw_input("Price per tile?\n")
dimensions = raw_input("Height, Width? -- (10x10)?\n")

match = re.match(r'(\d+)x(\d+)', dimensions, re.I)

print "An %s floor will cost you $%.2f at $%.2f per tile." % (dimensions, (float(match.group(1)) \
  * float(match.group(2))), float(price_per_tile))