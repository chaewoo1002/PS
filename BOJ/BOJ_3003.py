chess = [1, 1, 2, 2, 2, 8]

my = list(map(int, input().split()))

for i in range(0, len(chess)):
    print(chess[i] - my[i], end=' ')