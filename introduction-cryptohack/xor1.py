# all values 26 bytes
# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_bytes = bytes.fromhex(key1)

# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
current = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
current_bytes = bytes.fromhex(current)

key2_bytes = bytearray()
for i in range(len(key1_bytes)):
    key2_bytes.append(key1_bytes[i] ^ current_bytes[i])

# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
current = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
current_bytes = bytes.fromhex(current)

key3_bytes = bytearray()
for i in range(len(key2_bytes)):
    key3_bytes.append(key2_bytes[i] ^ current_bytes[i])

# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
current = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" 
current_bytes = bytes.fromhex(current)

flag_bytes = bytearray()
for i in range(len(key3_bytes)):
    flag_bytes.append(key1_bytes[i] ^ key2_bytes[i] ^ key3_bytes[i] ^ current_bytes[i])

print(flag_bytes)

