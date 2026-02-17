# Real Numbers
import sys
from fractions import Fraction
from Decimal  import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"ideal temperature is {ideal_temp}")
print(f"Current temperature is {current_temp}")
print(f"Diff. temperature is {ideal_temp - current_temp}")

print(sys.float_info)