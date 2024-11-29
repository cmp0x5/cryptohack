import requests

def get_current_block(string):
    plaintext = ''.join([f'{ord(a):02x}' for a in string])
    url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/' + plaintext + '/'
    r = requests.get(url)
    d = r.json()
    ciphertext = d['ciphertext']
    blocks_cipher = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]
    return blocks_cipher

def get_block_hash(plaintext):
    url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/' + plaintext + '/'
    r = requests.get(url)
    d = r.json()
    ciphertext = d['ciphertext']
    blocks_cipher = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]
    return blocks_cipher

flag = ""
num_chars = 15 
while num_chars > 0:
    string = 'a' * num_chars 
    res_block = get_current_block(string)[0]
    print(res_block)
    string = 'a' * num_chars + flag
    string += 'x'
    for c in range(48, 126):
        string = string[:-1] + chr(c)
        plaintext = ''.join([f'{ord(a):02x}' for a in string])
        curr_block = get_block_hash(plaintext)[0]
        if curr_block == res_block:
            flag += chr(c)
            print('found ' + chr(c))
            num_chars -= 1
            break
    print(flag)

print(flag)

# second block

num_chars = 16
while True:
    string = 'a' * num_chars
    res_block = get_current_block(string)[1]
    print(res_block)
    string = 'a' * num_chars + flag
    string += 'x'
    for c in range(48, 126):
        string = string[:-1] + chr(c)
        plaintext = ''.join([f'{ord(a):02x}' for a in string])
        curr_block = get_block_hash(plaintext)[1]
        if curr_block == res_block:
            flag += chr(c)
            print('found ' + chr(c))
            num_chars -= 1
            break
    print(flag)
    if len(flag) == 25: # 3rd block is added with an input of 7 bytes
        break

print(flag)
