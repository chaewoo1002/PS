# 기존 함수(시간 초과)
# def isPrime(num): # 입력받은 값이 소수인지 판별하는 isPrime 함수 생성
#   if num == 1: # 1은 소수가 아니다
#     return False
#   else: # 2 ~ n사이에 
#     for i in range(2, num):
#       if num % i != 0: # 나머지가 0이 아니라면 pass(건너뜀)
#         pass
#       else: # 2, n을 설정했으므로 만약, n이 5라면 2 ~ 4까지만 실행된다. num-1까지만 실행되므로 나눈 나머지가 0인 수가 더 존재한다면 소수가 아님
#         return False
#   return True

def isPrime(num):
  if num == 1:
    return False
  for i in range(2, int(num**0.5) + 1): # 2 ~ 입력값의 제곱근 + 1
    if num%i == 0: # num을 i로 나눈 값의 나머지가 0이라면?
      return False #  ㄴ> False 반환 (1과 자신을 제외한 나눠지는 수 i가 있기 때문)
  return True


num_list = list(range(2, 123456*2)) # 문제에서 제한된 범위 만큼 리스트 생성
prime_list = []
for i in num_list:
  if isPrime(i):
    prime_list.append(i)

n = int(input())
while True:
  if n == 0: # n의 값이 0이라면 반복 종료
    break
  cnt = 0 # 소수의 개수
  for i in prime_list:
    if n < i <= 2*n:
      cnt += 1
  print(cnt)
  n = int(input())