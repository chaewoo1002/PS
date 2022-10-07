import sys

n, m = map(int, input().split()) # 행, 렬 입력 받기

num_lst = []

for _ in range(n) :
    num_lst.append(list(map(int, sys.stdin.readline().split()))) # 리스트 내에 값 입력 받기

for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split())) # tmp를 사용하여 리스트 행렬 정리
    for j in range(m) :
        num_lst[i][j] += tmp[j] # 2차원 리스트의 i행 j열 인덱스에 tmp[j]값 초기화

for i in range(n) :
    for j in range(m) :
        print(num_lst[i][j], end = " ") # 순서대로 행렬A 출력 후 줄바꿈, 행렬B 출력 후 줄바꿈, 행렬 A,B의 합 출력
    print()