import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if A % C == 0 :
    num1 = A//C
else :
    num1 = (A//C) + 1

if B % D == 0 :
    num2 = B//D
else :
    num2 = (B//D) + 1

num = max(num1, num2)

print(L - num)