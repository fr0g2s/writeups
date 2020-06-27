분석 메모<br>
<br>
<ol>
  <li><h3>addcommand</h3></li>
  명령어를 필터링함.<br>
  <br>
== filtering list ==<br>
flag<br>
/bin<br>
sh<br>
echo<br>
cat<br>
shutdown<br>
init 0<br>
============<br>
추가된 명령어 문자열들은 힙 영역에 있음.<br>
명령어들의 주소는 < magic >이 가지고 있음.<br>
< head >는 < magic >의 주소를 알려줌.<br>
< ind >는 현재 명령어 갯수<br>
<br>
  <li><h3>runcommand</h3></li>
명령어의 번호를 입력받고 수행.<br>
명령어 없이 run 안됨.<br>
<br>
  <li><h3>editcommand</h3></li>
추가했던 명령어를 "/bin/sh"로 바꾸는데 여기선 필터링을 안함.<br>
<br>
  <li><h3>exit</h3></li><br>
  종료
</ol>
