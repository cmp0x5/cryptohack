import requests

r = requests.get('https://aes.cryptohack.org/bean_counter/encrypt/')
d = r.json()
ciphertext = d['encrypted']

block1 = ciphertext[:32]
png = "89504e470d0a1a0a0000000d49484452"

png_bytes = bytes.fromhex(png)
block1_bytes = bytes.fromhex(block1)

keystream = bytes([a^b for a,b in zip(png_bytes, block1_bytes)])

ciphertext_blocks = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]

with open("flag.png", 'wb') as f:
    for block in ciphertext_blocks:
        block = bytes.fromhex(block)
        plain = bytes([a^b for a,b in zip(block, keystream)])
        f.write(plain)

