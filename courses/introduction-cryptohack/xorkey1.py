encoded = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encoded_bytes = bytes.fromhex(encoded)

key = b"myXORkey"

flag = bytearray()
for i in range(len(encoded_bytes)):
    flag.append(encoded_bytes[i] ^ key[i%len(key)])

print(flag)


