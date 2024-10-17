def euclid(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(euclid(270, 192))
print(euclid(66528, 52920))

