```assembly
start
   0x1000:      lea    rsi,[rip+0x1ffa]        # 0x3001
   0x1007:      call   write			# puts("Enter access code:")
   0x100c:      xor    rdi,rdi
   0x100f:      lea    rsi,[rip+0x203a]        # 0x3050
   0x1016:      mov    rdx,0x30
   0x101d:      xor    rax,rax
   0x1020:      syscall					# read(0, [0x3050], 0x30)
   0x1022:      lea    rbp,[rip+0x200f]        # 0x3038
   0x1029:      xor    rsi,rsi
   0x102c:      call   isCorrect	# 0x107e
   0x1031:      cmp    QWORD PTR [rip+0x1fff],0x0        # 0x3038
   0x1039:      je     0x1050

if(!isCorrect())
   0x103b:      lea    rsi,[rip+0x1fe7]        # 0x3029
   0x1042:      call   write					# puts("Access denied")
   0x1047:      mov    rdi,0xffffffffffffffff
   0x104e:      jmp    0x105f
  
if(isCorrect())
   0x1050:      lea    rsi,[rip+0x1fbe]        # 0x3015
   0x1057:      call   write					# puts("Access authorized")
   0x105c:      xor    rdi,rdi
   0x105f:      mov    rax,0x3c
   0x1066:      syscall							# exit(0)
   
write
   0x1068:      mov    rdi,0x1
   0x106f:      movzx  rdx,BYTE PTR [rsi-0x1]
   0x1074:      mov    rax,0x1
   0x107b:      syscall
   0x107d:      ret

   
   
		
isCorrect(rbp=0x3038(9),rsi=0)
	idx = 0
   0x107e:      cmp    rsi,0x1
   0x1082:      jne    0x1085
   0x1084:      ret
   
   0x1085:      mov    rax,QWORD PTR [rbp+rsi*8+0x0]	# rax=_0x3038[idx]
   0x108a:      mov    rax,QWORD PTR [rbp+rax*8+0x0]	# rax=_0x3038[_0x3038[idx]]
   0x108f:      mov    rbx,QWORD PTR [rbp+rsi*8+0x8]	# rbx=_0x3038[idx+1]
   0x1094:      sub    QWORD PTR [rbp+rbx*8+0x0],rax	# _0x3038[_0x3038[idx+1]] -= _0x3038[_0x3038[idx]]
   0x1099:      ja     0x10b3
   0x109b:      cmp    QWORD PTR [rbp+rsi*8+0x10],0x2	# _0x3038[idx+2] == 2
   0x10a1:      je     0x10b2
   0x10a3:      cmp    QWORD PTR [rbp+rsi*8+0x10],0x0	# _0x3038[idx+2] == 0
   0x10a9:      je     0x10b3
   0x10ab:      mov    rsi,QWORD PTR [rbp+rsi*8+0x10]	# rsi=_0x3038[idx+2]
   0x10b0:      jmp    0x107e
   0x10b2:      int3
   
   0x10b3:      add    rsi,0x3
   0x10b7:      jmp    0x107e
```
   
```c
   while(rsi!=1){
		idx = rsi*8;
		if(_0x3038[_0x3038[idx+1]] - _0x3038[_0x3038[idx]]){
			rsi+=3;
		} else{
			if(_0x3038[idx+2] == 2){
				int3
			} else if (_0x3038[idx_2] == 0){
				rsi+=3;
			} else{
				rsi=_0x3038[idx+2];	// _0x3038[idx+2]=1 로 만들자.
			}
		}
   }
```
