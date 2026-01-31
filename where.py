import math
import random

import math
import random

queen = random.randint(0, 360)
print(f"Random angle (degrees): {queen}")

heir = math.radians(queen)

princess = math.sin(heir)
king = math.cos(heir)
prince = math.tan(heir)

print(f"sin({queen}) = {princess}")
print(f"cos({queen}) = {king}")
print(f"tan({queen}) = {prince}")