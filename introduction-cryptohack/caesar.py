cipher = ""
for n in range(1, 27):
    plain = ""
    for i in cipher:
        if i.isalpha():
            shift = ord(i) - ord('A')
            shifted_char = chr(((shift - n) % 26) + ord('A'))
            plain += shifted_char
        else:
            plain += i

    print(n)
    print(plain)
