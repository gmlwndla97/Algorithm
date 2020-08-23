Algorithm PS with python
=============
내가 보려고 만든 python 문법 정리
---------
---------------


📍 **입력받기**

 1. 한 줄에 띄어쓰기 된 여러 값 입력 받을 때 : 
 >>```map(int, sys.stdin.readline().rstrip().split())```
  >>+ 기본적으로 str 형태로 들어감 
 >>+ 여러 값일 때 map을 통해서 전체 다 int로 변환가능
2. 2차원 배열 붙어서 입력 받을 때:
>> ```arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]```
>>  + list로 감싸면 알아서 한 글자씩 list 한 칸에 들어감
>>  + 그걸 행 만큼 반복해주면 2차월배열 생성

3. 2차원 배열 떨어져서 입력 받을 때:
>> ```arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]```
>>  + split만 추가해주면 됨

4. 1차원 배열 떨어져서 입력 받을 때 : 
>> ```arr=list(map(int, sys.stdin.readline().rstrip().split()))```

---------------

📍 **문자열 관련 함수**

 1. 문자 개수 세기 : ```str.count('a')```
2. 문자열 찾기 : ```str.find('a')``` 또는 ``` str_a in str_b ```
3. 문자열 자르기 :```str[0:원하는 곳]```
 4. 문자열 뒤집기 : ```str[::-1]```
 5. 공백 지우기 : ```str.strip()```  +(rstrip, lstrip)
6. 알파벳 리스트 만들기 : ```from string import ascii_lowercase``` 이후 ```list(ascii_lowercase)```   +(ascii_lowercase)
 7. 문자열 바꾸기 : ```str.replace('a','b')```
 8. 문자열 중복제거 : ```''.join(set(str))```
9. 아스키코드 번호 반환 : ```ord(str)```
10. 아스키코드 기호 반환 : ```chr(숫자)```
  11. 다음줄로 넘어만 가기 (\n말고) : ```print()```
 
--------------
📍 **자료구조**

 1. 1차원 배열 생성하기 :  1Xn 크기의 배열을 만든다고 하면

> ```arr=[0 for _ in range (n)]``` 또는 ```arr=[0]*n```

 2. 2차원 배열 생성하기 :  m*n 크기의 배열을 만든다고 하면 (m행 n열)

>```arr=[0 * m for _ in range(n)]```

3. 리스트 정렬하기 :
> + 정렬된 리스트로 바꾸고 싶은 경우 : ```list.sort()```
> + 원본 리스트는 그대로 두고, 정렬된 리스트 새로 만들고 싶은 경우 : ```sorted(list)```


