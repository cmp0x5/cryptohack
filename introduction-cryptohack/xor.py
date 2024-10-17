string = "label"
key = 0xD
new_string = ""

for c in string:
    n = int(hex(ord(c)), 16)
    curr_char = n ^ key
    new_string += chr(curr_char)


print(new_string)

