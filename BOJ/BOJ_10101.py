A = int(input())
B = int(input())
C = int(input())

if A+B+C != 180:
  print("Error")
elif A == B and A == C: # 세 각의 크기가 모두 같은 경우
  print("Equilateral")
elif A == B or A == C or B == C: # 두 각의 크기가 같은 경우
  print("Isosceles")
else:
  print("Scalene")