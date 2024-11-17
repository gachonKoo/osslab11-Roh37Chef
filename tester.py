import sys
sys.path.append(".")

import geo.utils as utils

# Check available functions
print(dir(utils))

# Test pythagoras
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# Test circle
r = 10
area = utils.circle(r)
print('area =', area)
