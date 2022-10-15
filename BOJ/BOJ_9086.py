n = int(input()) # 반복 횟수 입력

for i in range(n):
  str = input() # 문자열 입력
  print(str[0] + str[-1]) # 문자열의 첫번째 인덱스, 문자열의 -1번째 인덱스 -> 문자열의 마지막 글자를 출력