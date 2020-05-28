이름, 패스워드... 등의 값을 input()을 통해 입력받는다.<br>
Tinder Bio를 입력할 때, input()안에서 8*16 = 128 바이트를 입력받으면서 오버플로우 발생.<br>
local_14값을 0xc0d3d00d(-0x3f2c2ff3) 으로 만들어 flag를 획득하면 된다.<br>
<br>