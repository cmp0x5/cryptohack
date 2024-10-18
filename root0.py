p = 29
ints = [14, 6, 11]

for i in range(p):
    if pow(i, 2, p) in ints:
        print("i: " + str(i) + "**2=" + str(pow(i, 2)) + " mod p=" + str(pow(i, 2, p)))
