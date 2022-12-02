import sys

while True:
    n = float(sys.stdin.readline())
    if n == 0: break
    print('%.2f' %(1+n+n**2+n**3+n**4))