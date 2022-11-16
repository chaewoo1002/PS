nums = {x for x in range(2, 10_001) if x == 2 or x % 2 == 1} # 2를 포함한 1 ~ 10000까지의 홀수 집합 생성 (짝수는 소수가 아님)

for odd in range(3, 101, 2): 
  nums -= {i for i in range(2 * odd, 10_001, odd) if i in nums}

t = int(input())
for _ in range(t):
  even = int(input())
  half = even//2
  for x in range(half, 1, -1):
    if (even-x in nums) and (x in nums):
      print(x, even-x)
      break