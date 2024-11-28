import math

a = 288260533169915
p = 1007621497415251

exp = int((p-1) / 2)

print(pow(a, exp, p)) 

print(p % 4)
