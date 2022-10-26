n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)] # arr은 도화지 크기 100 * 100로 설정하므로 range(101)로 설정한다(0~100)

for _ in range(n):
    a, b = map(int, input().split()) # 정사각형 색종이 가로, 세로 값 입력

    for i in range(a, a+10) : # 가로 크기 10
        for j in range(b, b+10) : # 세로 크기 10
            arr[i][j] = 1 # 

count = 0 
for row in arr :
    count += row.count(1)
print(count)