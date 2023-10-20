hex_values = [
   0x7b425448, 0x5f796877, 
    0x5f643164, 0x34735f31, 0x745f3376, 0x665f3368, 0x5f67346c, 
    0x745f6e30, 0x355f3368, 0x6b633474, 0x7d213f, 0x8adce00, 
    0xf7f193fc, 0x56598f8c, 0xffd0e198, 0x56596441, 0x1, 0xffd0e244, 
    0xffd0e24c, 0x8adce00, 0xffd0e1b0
]


hex_strings = [hex(value)[2:] for value in hex_values]
hex_strings= hex_strings[::-1]

divided_hex = [value[i:i+2] for value in hex_strings for i in range(0, len(value), 2)]

ascii_values = [chr(int(hex_group, 16)) for hex_group in divided_hex]

ascii_values = ascii_values[::-1]


string=""
for i in ascii_values:
    string+= i
print(string)
