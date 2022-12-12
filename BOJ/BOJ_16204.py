n, m, k = map(int, input().split())
res = min(m, k) + min(n-m, n-k)
print(res)