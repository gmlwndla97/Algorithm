Algorithm PS with python
=============
내가 보려고 만든 python 문법 정리
---------

📍 **입력받기**
* 한 줄에 띄어쓰기 된 여러 값 입력 받을 때 : 
 '''python
 map(int, sys.stdin.readline().rstrip().split())
 '''
 * 여러 값일 때 map을 통해서 전체 다 int로 변환가능
* 2차원 배열 붙어서 입력 받을 때:
 '''python
 arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
 '''
 * list로 감싸면 알아서 한 글자씩 list 한 칸에 들어감
 * 그걸 행 만큼 반복해주면 2차월배열 생성


📍 **문자열 관련 함수**
* 문자 개수 세기 : '''python
str.count('a')
'''
* 인덱스 반환하기 : '''python
str.find('a')
'''
* 문자열 자르기 : '''python
str[0:원하는 곳]
'''
* 문자열 뒤집기 : '''python
str[::-1]
'''
* 알파벳 리스트 만들기 : '''python
from string import ascii_lowercase
''' 이후 '''python
list(ascii_lowercase)
'''

📍 **자료구조**
