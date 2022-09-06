n = input() # 문자열 입력 받기
arr = list(range(97, 123)) # 소문자 아스키 코드 범위 97 ~ 123만큼의 리스트 생성

for i in arr:
    print(n.find(chr(i)), end = " ") # chr 메서드는 값을 아스키코드 숫자를 문자로 변환해주고, find() 메서드는 리스트 안의 값의 인덱스를 찾아준다