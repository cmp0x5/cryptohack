import requests

r = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/')
d = r.json()
cookie = d['cookie']
cookie_blocks = [cookie[i:i+32] for i in range(0, len(cookie), 32)]

original_iv = bytes.fromhex(cookie_blocks[0])
cookie = "".join([a for a in cookie_blocks[1:]])
print(cookie)

original = b"admin=False;expi"
target = b"admin=True;expir"

new_iv = bytes([a ^ b ^ c for a,b,c in zip(original_iv, original, target)])

url = f'https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{new_iv.hex()}/'
print(url)

r = requests.get(url)
d = r.json()
print(d)

