# 리스트 방식이 시간초과가 발생한다면 함수를 사용해보도록 하자
def isPrime(n):
  if n == 1:
    return False # 1은 소수가 아님
  else:
    for i in range(2, int(n**0.5) + 1): # 2 ~ n의 제곱 + 1 중 나눠지는 수가 있는지 확인
      if n%i == 0: # i중 나눠지는 수가 있다면 소수가 아님
        return False
    return True

min, max = map(int, input().split())

for i in range(min, max+1):
  if isPrime(i):
    print(i)

# 기존 코드 (리스트방식 사용함에 따라 시간 초과)

# min, max = map(int, input().split())

# pnum_lst = []
# for i in range(min, max + 1):
#   div_num = 0
#   if i > 1:
#     for j in range(2, i):
#       if i % j == 0:
#         div_num += 1
#     if div_num == 0:
#       pnum_lst.append(i)

# for i in pnum_lst:
#   print(i)