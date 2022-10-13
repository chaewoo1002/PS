import sys # 반복문 내 입력 사용
res = 0

for i in range(5):
  res += int(sys.stdin.readline())

print(res)