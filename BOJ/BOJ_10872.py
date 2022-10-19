def fac(n): # 재귀함수를 통해 팩토리얼 구현
    result = 1
    if n > 0 :
        result = n * fac(n-1)
    return result

n = int(input())
print(fac(n))