a = int(input())
b = int(input())
c = int(input())

# 앞 10자리는 고정으로 9780921418이며, 9780921418의 1-3-sum은 91이다.
print("The 1-3-sum is", 91 + a + b*3 + c) # a * 1과 c * 1이지만 어차피 결과는 a + c이므로 생략