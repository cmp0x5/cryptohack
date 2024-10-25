p = 26513
q = 32321

for i in range(q):
    n = (i*p) % q
    if n == 1:
        print(i)
