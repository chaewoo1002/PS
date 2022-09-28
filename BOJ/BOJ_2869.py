import math # math.ceil()을 사용하기 위해 모듈 import

a, b, v = map(int,input().split())  # 공백을 기준으로 3개 map()으로 나눠 입력
date = math.ceil((v-b) / (a-b)) # 문제의 조건을 코드로 구현하면 (v-b) / (a-b)가 된다. 여기서 /(나누기) 연산자를 사용하게 되면
                                # 파이썬에서 나누기 연산자는 소수점까지 구해지게 되므로 어떤 경우 4.2일 과 같은 결과가 도출될 수 있다.
                                # 이를 방지하기 위해서 4.0일은 math.ceil()을 사용해 올림 연산을 해주면 된다.
                                # 4.0일은 4일이지만 4.1일부터는 5일이기에
print(date)

# 기존코드 (시간초과)

# a, b, v = map(int,input().split())

# now_v = 0
# date = 0

# while now_v <= v:
#     now_v += a
#     date += 1
#     if now_v >= v: 
#         break
#     now_v -= b

# print(date)