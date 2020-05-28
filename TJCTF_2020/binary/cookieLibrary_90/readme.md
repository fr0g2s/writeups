ASLR + NX = ROP<br>
but Full RELRO, can't overwrite got<br>
so i called main to write again<br>
1. return to puts(puts@got) for leak got address<br>
2. return to main func, and input payload that have system address.<br>
3. return to write(cookie), and input "/bin/sh\x00"<br>
4. retun to system(cookie), and get shell !! <br>