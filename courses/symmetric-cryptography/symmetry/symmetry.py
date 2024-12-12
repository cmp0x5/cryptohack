import requests

r = requests.get('https://aes.cryptohack.org/symmetry/encrypt_flag/')
d = r.json()
flag = d['ciphertext']

iv = flag[:32]
flag = flag[32:]

r = requests.get(f"https://aes.cryptohack.org/symmetry/encrypt/{flag}/{iv}/")
d = r.json()

flag_hex = d['ciphertext']
print(bytes.fromhex(flag_hex))
