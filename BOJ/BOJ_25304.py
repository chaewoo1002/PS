# price = int(input())
# rec = 0

# n = int(input())

# for i in range(n):
#     pri, nub = input().split()
#     pri, nub = int(pri), int(nub)
#     rec += (pri * nub)

# if (price == rec) :
#     print("Yes")

# else : 
#     print("No")

# 코드를 간략화 하기 위해서는 rec 변수 삭제, if else문 간략화 가능 아래 코드로 구현 (정답 참고)

price = int(input())

n = int(input())

for i in range(n):
    pri, nub = input().split()
    pri, nub = int(pri), int(nub)
    price -= (pri * nub)

print("Yes" if (price == 0) else "No")