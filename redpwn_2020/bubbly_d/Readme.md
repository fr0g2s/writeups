어셈코드가 심각하게 길었는데, 멀리서 보니 비슷한 패턴이 보였다.<br>
대충 코드로 바꿔보면,<br>
```
nums[i] xor nums[i+1]
nums[i+1] xor nums[i]
nums[i] xor nums[i+1]
```
xor trick이다! 반갑다.<br>
<br>
xor trick으로 인접한 두 수(nums[myinput], nums[myinput+1])를 바꾼다.<br>
그리고 check()에서 모두 오름차순인지 비교한다.<br>
<br>
버블 정렬!!!<br>
<br>
알고보면 문제에서 힌트를 매우 많이 줬었다...<br>
<br>

