N, A, B, C, D = map(int, input().split())
A = (N//A + (1 if N%A else 0)) * B # 히히 삼항연산자 발싸
C = (N//C + (1 if N%C else 0)) * D # 22

print(min(A, C))