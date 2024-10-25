encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encoded_bytes = bytes.fromhex(encoded)

for i in range(0x00, 0xFF):
    current = bytearray()
    for byte in encoded_bytes: 
        current.append(i ^ byte)
    if current[0:6] == b'crypto':
        print(current)
