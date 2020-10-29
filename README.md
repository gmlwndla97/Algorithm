Algorithm PS with python
=============
내가 보려고 만든 python 문법 정리
---------
---------------


📍 **입력받기**

- 한 줄에 띄어쓰기 된 여러 값 입력 받을 때 : 
  - ```map(int, sys.stdin.readline().rstrip().split())```
  -  기본적으로 str 형태로 들어감 
  -  여러 값일 때 map을 통해서 전체 다 int로 변환가능
  
- 2차원 배열 붙어서 입력 받을 때:
  - ```arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]```
  - list로 감싸면 알아서 한 글자씩 list 한 칸에 들어감
  - 그걸 행 만큼 반복해주면 2차월배열 생성

- 2차원 배열 떨어져서 입력 받을 때:
  - ```arr=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]```
  - split만 추가해주면 됨

- 1차원 배열 떨어져서 입력 받을 때 : 
  - ```arr=list(map(int, sys.stdin.readline().rstrip().split()))```

---------------

📍 **문자열 관련 함수**

1. 문자 개수 세기 : ```str.count('a')```
2. 문자열 찾기 : ```str.find('a')``` 또는 ``` str_a in str_b ```
3. 문자열 자르기 :```str[0:원하는 곳]``` 
4. 문자열 뒤집기 : ```str[::-1]```
5. 공백 지우기 : ```str.strip()```  +(rstrip, lstrip)
6. 알파벳 리스트 만들기 : ```from string import ascii_lowercase``` 이후 ```list(ascii_lowercase)```   +(ascii_uppercase)
7. 문자열 바꾸기 : ```str.replace('a','b')```
8. 문자열 중복제거 : ```''.join(set(str))```
9. 아스키코드 번호 반환 : ```ord(str)```
10. 아스키코드 기호 반환 : ```chr(숫자)```
11. 다음줄로 넘어만 가기 (\n말고) : ```print()```
12. 해당 단어로 시작하는지 확인하기 (prefix) : ```str.startswith(str2)```
 
--------------
📍 **자료구조 및 내장함수**
<details>
   <summary>🎲 deque(큐) </summary>
- ```
  from collections import deque
  q=deque()
 ```
  
- push, pop : ```q.append(i) , q.popleft() ```
  - 파이썬 deque에는 push가 없고 append로 추가하고 pop대신에 popleft를 사용한다.
   
  
    <summary>🎲 리스트</summary>

- 1차원 배열 생성하기 :  1Xn 크기의 배열을 만든다고 하면

  - ```arr=[0 for _ in range (n)]``` 또는 ```arr=[0]*n```

- 2차원 배열 생성하기 :  m*n 크기의 배열을 만든다고 하면 (m행 n열)

  - ```arr=[0 * m for _ in range(n)]```

- 리스트 정렬하기 :
  - 정렬된 리스트로 바꾸고 싶은 경우 : ```list.sort()```
  - 원본 리스트는 그대로 두고, 정렬된 리스트 새로 만들고 싶은 경우 : ```newList=sorted(list)```
  - 인자가 여러개일 때 먼저 첫 번째 인자 기준으로 정렬하고, 그 다음 두 번째 인자 기준으로 정렬하고 싶은 경우 :
    ``` newList=sorted(list, key=lambda x :(x[0], x[1])) ```
    (내림차순으로 정렬하고 싶으면 -를 붙여준다.)
    
     
     
- 중복 요소 제거하기:
  - ``` newlist=list(set(mylist))    ```
      
 
  
</details>

<br/><br/>

<details>
    <summary>🎲 우선순위 큐</summary>

  - heapq
    - 생성하기, 원소 추가하기 :  
      - ```
          import heapq

          h=[] 
          heapq.heappush(h, 우선순위)
        ```
    - 원소 꺼내기 :  ```heapq.heappop(h)```  
    
    
    
  - priority queue
    - 생성하기 :  
      - ```
          from queue import PriorityQueue

          q=PriorityQueue()
        ```

    - 원소 추가하기 : ``` q.put(값)```
    - 원소 추가 시 우선순위 설정 : ``` q.put((우선순위, 값))```
    - 원소 꺼내기(삭제하기) :  ``` q.get() ```  

</details>

<br/><br/>

<details>
    <summary>🎲 딕셔너리</summary>

  - 딕셔너리 value 값 기준으로 정렬하기 :
     - ```sorted(map.items(), key=lambda x:x[1], reverse=True)```  
     
  - key와 value 순서 바꾼 dictionary 생성하기 :
     - ```dic={v:k for k, v in dic.items()}```
     
  - value값으로 key찾기 : (v는 value, k는 key를 의미)
     - ```
        for k, v in dic.items():
           if v==원하는 값:
              print(k)
        ```
     - ```
         [k for k, v in dic.items() if v==원하는 값]
        ```
  - 리스트를 딕셔너리로 바꾸기 :
    -```
      list=['A','B','C']
      
      dic={string : 0 for string in list}
     ```
    이렇게 하면 {'A':0, 'B':0, 'C':0} 가 만들어진다.


</details>
<br/><br/>


<details>
    <summary>🎲 순열과 조합 permutation&combination </summary>
  
  - 순열: n개 중 r개 고름 ( 순서 상관 있음 ) : 
  ```
    import itertools
    arr=[1, 2, 3]
    permu=itertools.permutations(arr, 2)
    print(list(permu))
  ```
     
  - 조합 : n개 중 r개 고름 ( 순서 상관 없음 ) :
  ```
    import itertools
    arr=[1, 2, 3]
    combi=itertools.combinations(arr,2)
    print(list(comb))
  ```
   
     
   
 
 </details>
