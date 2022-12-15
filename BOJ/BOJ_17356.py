A, B = map(float, input().split()) # 단순 사칙연산, 정수가 아닌 실수를 받아야하므로 float 자료형 사용
M = (B-A) / 400
res = 1 / (1+10 ** M)
print(res)