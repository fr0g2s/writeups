
action = "Flag it!" 일 때, if(strncmp(guess, flag, strlen(flag)){} 코드로 진입합니다.<br>
여기서 guess를 wrong에 guessLen만큼 붙이고 출력을 합니다. <br>
wrong은 strlen(guess)+35 만큼 할당받기에 안전한것처럼  , guess는 read()로 입력받기 때문에 '\x00'을 넣어 strlen()을 속일 수 있습니다.<br>
예를 들어, "\x00aaaa"를 입력하면 guessLen=7 이지만 strlen(guess)=0 이 됩니다.<br>
<br>
따라서 guess에 "\x00"와 dummy를 적절히 입력하면 wrong[35]만큼 할당이 되고, write(1, wrong, guessLen+35); 에서 leak이 발생하기 때문에 메모리에 있는 flag[]를 읽을 수 있습니다.
