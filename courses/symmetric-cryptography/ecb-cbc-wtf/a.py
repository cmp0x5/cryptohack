import requests

r = requests.get('https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag')
d = r.json()
ciphertext = d['ciphertext']
blocks_cipher = [ciphertext[i:i+32] for i in range(0,len(ciphertext), 32)]

url = 'https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + ciphertext + '/'
r = requests.get(url)
d = r.json()
decrypted = d['plaintext']
blocks_decrypted = [decrypted[i:i+32] for i in range(0, len(decrypted), 32)]

c1 = bytes.fromhex(blocks_cipher[0])
c2 = bytes.fromhex(blocks_cipher[1])

p2 = bytes.fromhex(blocks_decrypted[1])
p3 = bytes.fromhex(blocks_decrypted[2])

flag = bytes(a ^ b for a,b in zip(c1, p2))
flag2 = bytes(a ^ b for a,b in zip(c2, p3))
print(flag + flag2)


