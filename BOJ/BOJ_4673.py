# 참고 https://wook-2124.tistory.com/252

normalNum = set(range(1, 10001)) # range()를 사용해 1 ~ 10000까지 숫자를 불러온 후 set()으로 집합 생성
nonSelfNum = set()  # .add() 메서드 사용을 위해 set()을 사용해 집합 생성, set()을 통해 생성한 집합에서는 .add(), .remove()등 메서드 사용 가능

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    nonSelfNum.add(i)

selfNum = sorted(normalNum - nonSelfNum)    # list에서 (리스트명.sort())를 사용하는 것과 같은 원리. 집합 내의 값들을 오름차순으로 정렬해준다
                                            # .sort()와 다르게 sorted() 메서드는 집합뿐 아니라 어떠한 이터러블 객체든 정렬이 가능하다.

for x in selfNum:
    print(x)