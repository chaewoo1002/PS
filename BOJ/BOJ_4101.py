import sys 

while True:
  n, m = map(int, sys.stdin.readline().split()) # 반복문 내 입력의 경우 input()대신 sys.stdin.readline() 사용, 시간초과 방지
  if(n == 0 and m == 0):  # n과 m의 이 0, 0으로 주어지면 반복 종료
     break
  print("Yes" if n > m else "No") # 파이썬 삼항연산자 표현 n > m 이면 "Yes" 아니라면 "No"