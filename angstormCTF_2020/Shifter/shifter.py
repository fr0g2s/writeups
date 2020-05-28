from pwn import *

p = remote('misc.2020.chall.actf.co', 20300)

alpha = [chr(a) for a in range(65,97,1)]

fibo = [int(0) for _ in range(0, 51, 1)]
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1
for i in range(3, 50, 1):
	fibo[i] = fibo[i-1] + fibo[i-2]

print p.recvuntil('--------------------\n')
state = 3
for _ in range(0,50,1):
	buff = p.recvline().replace('\n','')
	print 'recv = ', buff
	buff = buff.split(' ')
	plaintext = buff[state-2]
	n = int(buff[state].replace('n=',''))
	state = 4
	result = ''

	log.info('plaintext = %s' % plaintext)
	log.info('n = %d' % n)
	fi = fibo[n]
	log.info('nth sosu = %d' % fibo[n])

	for c in range(len(plaintext)):
		nextIndex = (alpha.index(plaintext[c])+fi)%26
		result += alpha[nextIndex]

	log.info('result = %s' % result)
	p.sendline(result)

print p.recvline()
