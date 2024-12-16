def gcd_ext(a, b):
    if (a == 0):
        return b, 0, 1
    gcd, x1, y1 = gcd_ext(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

e = 65537

phi = (p-1) * (q-1)

# d*e = 1 mod phi

gcd, a, b = gcd_ext(phi, e)
print(gcd)
print(a)
print(b)
