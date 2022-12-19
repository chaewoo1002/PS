t = int(input())
tmp = list(map(int, input().split()))
res = 0
for i in tmp:
    if i == t:
        res += 1
print(res)