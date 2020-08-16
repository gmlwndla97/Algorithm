Algorithm PS with python
=============
내가 보려고 만든 python 문법 정리
---------

📍 **입력받기**

##### 1. 한 줄에 띄어쓰기 된 여러 값 입력 받을 때 : 
```
 map(int, sys.stdin.readline().rstrip().split())
 ```
 + 여러 값일 때 map을 통해서 전체 다 int로 변환가능
 
##### 2. 2차원 배열 붙어서 입력 받을 때:
```arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]```
 + list로 감싸면 알아서 한 글자씩 list 한 칸에 들어감
 + 그걸 행 만큼 반복해주면 2차월배열 생성
---------------

📍 **문자열 관련 함수**

##### 1. 문자 개수 세기 : ```str.count('a)```
##### 2. 인덱스 반환하기 : ```str.find('a')```
##### 3. 문자열 자르기 :```str[0:원하는 곳]```
##### 4. 문자열 뒤집기 : ```str[::-1]```
##### 5. 알파벳 리스트 만들기 : ```from string import ascii_lowercase``` 이후 ```list(ascii_lowercase)```
--------------
📍 **자료구조**
