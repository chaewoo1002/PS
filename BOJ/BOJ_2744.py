str = "" # 빈 문자열 변수 생성

for i in input(): # 변수를 지정하지 않고 입력 자체로 반복문을 돌리는 것도 가능하다.
    if i.islower(): # input()으로 받은 값의 인덱스 i값이 소문자라면?
        str += i.upper()    # 대문자로 변경
    else:   # 소문자가 아니라면
        str += i.lower()    # 소문자로 변경

print(str) # 바뀐 문자열 출력