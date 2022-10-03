n = int(input())
nums = map(int, input().split())

p_num = 0 # prime number

for i in nums:
  div_num = 0 # 나눠지는 수
  if i > 1 :
    for j in range(2, i): # 2부터 n-1까지 (1은 소수가 아님)
      if i % j == 0:
        div_num += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가 
    if div_num == 0:
      p_num += 1  # 나눠지는 수가 없으므로 소수

print(p_num)