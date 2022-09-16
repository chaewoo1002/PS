# 참고 https://wook-2124.tistory.com/252

normalNum = set(range(1, 10001)) # range()를 사용해 1 ~ 10000까지 숫자를 불러온 후 set()으로 집합 생성
nonSelfNum = set()  # .add() 메서드 사용을 위해 set()을 사용해 집합 생성, set()을 통해 생성한 집합에서는 .add(), .remove()등 메서드 사용 가능

for i in range(1, 10001):
    for j in str(i):    # i의 값을 한글자씩 나눠줌(문자로 변환) ex) i = 853, j = '8', '5', '3'
        i += int(j)     # 나눠준 글자들을 다시 정수 자료형으로 변경 및 i에 값들을 더해준다 ==> i의 값은 생성자가 있는 숫자들이 된다. 
    nonSelfNum.add(i)   # 구해진 생성자가 있는 숫자들을 nonSelfNum(셀프넘버가 아닌 숫자들)에 추가

selfNum = sorted(normalNum - nonSelfNum)    # list에서 (리스트명.sort())를 사용하는 것과 같은 원리. 집합 내의 값들을 오름차순으로 정렬
                                            # .sort()와 다르게 sorted() 메서드는 집합뿐 아니라 어떠한 이터러블 객체든 정렬이 가능
''' 
1 ~ 10000까지의 숫자가 있는 집합에서 생성자가 있는 숫자들을 모두 뺀 후 정렬 
    ㄴ> 정렬된 셀프넘버를 출력 가능하게 됨 
'''

for x in selfNum:
    print(x)    # 정렬된 셀프넘버를 한줄씩 출력