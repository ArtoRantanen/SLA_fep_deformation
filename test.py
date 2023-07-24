import math
fep_density = 1300
resin_density = 1175
total_internal_reflection = math.degrees(math.asin(resin_density/fep_density))
print(total_internal_reflection)
