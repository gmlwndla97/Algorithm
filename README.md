Algorithm PS with python
=============
내가 보려고 만든 python 문법 정리
---------

📍 **입력받기**
* 한 줄에 띄어쓰기 된 여러 값 입력 받을 때 : 
 \' map(int, sys.stdin.readline().rstrip().split())\'
 - 여러 값일 때 map을 통해서 전체 다 int로 변환가능
 
* 2차원 배열 붙어서 입력 받을 때:
(C:\Users\82103\Desktop)
\'arr=[list(map(int, input())) for _ in range(n)]'\
