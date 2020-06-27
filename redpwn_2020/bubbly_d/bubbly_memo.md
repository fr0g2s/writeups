<pre>
```avrasm
   0x0000000000001259 <+128>:   lea    rdx,[rax*4+0x0]
   0x0000555555555261 <+136>:   lea    rax,[rip+0x2df8]        # nums
   0x0000555555555268 <+143>:   mov    edx,DWORD PTR [rdx+rax*1] # nums[input*4]
   0x000055555555526b <+146>:   mov    eax,DWORD PTR [rbp-0xc]	
   0x000055555555526e <+149>:   add    eax,0x1	# input+1
   0x0000555555555271 <+152>:   mov    eax,eax
   0x0000555555555273 <+154>:   lea    rcx,[rax*4+0x0]
   0x000055555555527b <+162>:   lea    rax,[rip+0x2dde]  
   0x0000555555555282 <+169>:   mov    eax,DWORD PTR [rcx+rax*1]	# nums[(input+1)*4]
   0x0000555555555285 <+172>:   mov    esi,DWORD PTR [rbp-0xc]		# input
   0x0000555555555288 <+175>:   mov    ecx,edx
   0x000055555555528a <+177>:   xor    ecx,eax						# nums[input*4] ^ nums[(input+1)*4]
   0x000055555555528c <+179>:   mov    eax,esi
   0x000055555555528e <+181>:   lea    rdx,[rax*4+0x0]
   0x0000555555555296 <+189>:   lea    rax,[rip+0x2dc3]        		
   0x000055555555529d <+196>:   mov    DWORD PTR [rdx+rax*1],ecx	# nums[input*4] = nums[input*4]^nums[(input+1)*4]
   
   0x00005555555552a0 <+199>:   mov    eax,DWORD PTR [rbp-0xc]
   0x00005555555552a3 <+202>:   add    eax,0x1						# input+1
   0x00005555555552a6 <+205>:   mov    eax,eax
   0x00005555555552a8 <+207>:   lea    rdx,[rax*4+0x0]
   0x00005555555552b0 <+215>:   lea    rax,[rip+0x2da9]        
   0x00005555555552b7 <+222>:   mov    edx,DWORD PTR [rdx+rax*1]	# nums[(input+1)*4]
   0x00005555555552ba <+225>:   mov    eax,DWORD PTR [rbp-0xc]		# input
   0x00005555555552bd <+228>:   mov    eax,eax
   0x00005555555552bf <+230>:   lea    rcx,[rax*4+0x0]
   0x00005555555552c7 <+238>:   lea    rax,[rip+0x2d92]       
   0x00005555555552ce <+245>:   mov    eax,DWORD PTR [rcx+rax*1]	# nums[input*4]
   0x00005555555552d1 <+248>:   mov    ecx,DWORD PTR [rbp-0xc]		
   0x00005555555552d4 <+251>:   lea    esi,[rcx+0x1]
   0x00005555555552d7 <+254>:   mov    ecx,edx
   0x00005555555552d9 <+256>:   xor    ecx,eax	# nums[(input+1)*4]^nums[input*4]
   0x00005555555552db <+258>:   mov    eax,esi	# input+1
   0x00005555555552dd <+260>:   lea    rdx,[rax*4+0x0]
   0x00005555555552e5 <+268>:   lea    rax,[rip+0x2d74]        # 0x555555558060 <nums>
   0x00005555555552ec <+275>:   mov    DWORD PTR [rdx+rax*1],ecx	# nums[(input+1)*4] = nums[(input+1)*4]^nums[input*4]
   
   0x00005555555552ef <+278>:   mov    eax,DWORD PTR [rbp-0xc]
   0x00005555555552f2 <+281>:   mov    eax,eax
   0x00005555555552f4 <+283>:   lea    rdx,[rax*4+0x0]
   0x00005555555552fc <+291>:   lea    rax,[rip+0x2d5d]        # 0x555555558060 <nums>
   0x0000555555555303 <+298>:   mov    edx,DWORD PTR [rdx+rax*1]	# nums[input*4]
   0x0000555555555306 <+301>:   mov    eax,DWORD PTR [rbp-0xc]
   0x0000555555555309 <+304>:   add    eax,0x1	# input+1
   0x000055555555530c <+307>:   mov    eax,eax
   0x000055555555530e <+309>:   lea    rcx,[rax*4+0x0]
   0x0000555555555316 <+317>:   lea    rax,[rip+0x2d43]        # 0x555555558060 <nums>
   0x000055555555531d <+324>:   mov    eax,DWORD PTR [rcx+rax*1]	# nums[(input+1)*4]
   0x0000555555555320 <+327>:   mov    esi,DWORD PTR [rbp-0xc]
   0x0000555555555323 <+330>:   xor    edx,eax
   0x0000555555555325 <+332>:   mov    ecx,edx
   0x0000555555555327 <+334>:   mov    eax,esi	# input
   0x0000555555555329 <+336>:   lea    rdx,[rax*4+0x0]
   0x0000555555555331 <+344>:   lea    rax,[rip+0x2d28]        # 0x555555558060 <nums>
   0x0000555555555338 <+351>:   mov    DWORD PTR [rdx+rax*1],ecx	# nums[input*4] = nums[input*4]^nums[(input+1)*4]
   0x000055555555533b <+354>:   mov    eax,0x0
   
   0x0000555555555340 <+359>:   call   0x555555555165 <check>

   
   nums
   1, 10, 3, 2, 5, 9, 8, 7, 4, 6
   8번 안에 정렬시켜야함.
   
<solve>
input/ nums
 1  	1 3 10 2 5 9 8 7 4 6
 2  	1 3 2 10 5 9 8 7 4 6
 3  	1 3 2 5 10 9 8 7 4 6
 4  	1 3 2 5 9 10 8 7 4 6
 5  	1 3 2 5 9 8 10 7 4 6
 6  	1 3 2 5 9 8 7 10 4 6
 7  	1 3 2 5 9 8 7 4 10 6
 8  	1 3 2 5 9 8 7 4 6 10
 
 1  	1 2 3 5 9 8 7 4 6 10
 6  	1 2 3 5 9 8 4 7 6 10
 5  	1 2 3 5 9 4 8 7 6 10
 4  	1 2 3 5 4 9 8 7 6 10
 3  	1 2 3 4 5 9 8 7 6 10
 
 7  	1 2 3 4 5 9 8 6 7 10
 6  	1 2 3 4 5 9 6 8 7 10
 5  	1 2 3 4 5 6 9 8 7 10
 
 7  	1 2 3 4 5 6 9 7 8 10
 6  	1 2 3 4 5 6 7 9 8 10
 
 7  	1 2 3 4 5 6 7 8 9 10
 ```
 </pre>