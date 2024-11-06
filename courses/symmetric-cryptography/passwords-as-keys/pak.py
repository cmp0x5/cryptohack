from Crypto.Cipher import AES
import requests
import hashlib

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    
    return {"plaintext": decrypted.hex()}


r = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/') 
data = r.json()
ciphertext = data['ciphertext']

with open('./words') as f:
    words = [w.strip() for w in f.readlines()]
    for word in words:
        word_hex = word.encode("utf-8").hex()
        word_bytes = bytes.fromhex(word_hex)
        word_hash = hashlib.md5(word_bytes).hexdigest()
        #request_url = 'https://aes.cryptohack.org/passwords_as_keys/decrypt/' + ciphertext + '/' + word_hash.hexdigest() + '/'
        #r = requests.get(request_url)
        data = decrypt(ciphertext, word_hash)
        plaintext = bytes.fromhex(data['plaintext'])
        print(plaintext)



