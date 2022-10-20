a = list(map(int, input().split())) # 공백 기준으로 값을 리스트에 정렬
c = list(map(int, input().split()))
b = [c[0]-a[2], c[1]//a[1], c[2]-a[0]] # 단순 계산

print(*b) # 리스트 출력의 [] 와 , 출력을 막아주기 위해 리스트 앞에 *을 붙여줌.(값만 따로 출력)