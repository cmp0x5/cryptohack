from random import randint

a = 288260533169915 # not prime
p = 1007621497415251 # is prime

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag]) # byte to 8-bit binary value
    for b in plaintext:
        e = randint(1, p) # e is random value between 1 and p
        n = pow(a, e, p) # calculate modulus of a**e mod p 
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

cipher = encrypt_flag(FLAG)
print(cipher)
# each item in list was generated from a bit, n if 1, additive inverse of n if 0
