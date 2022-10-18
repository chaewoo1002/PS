n = int(input()) # 파이썬에서는 리스트 생성에 굳이 숫자의 개수를 받을 필요는 없다. / 버리는 입력 /
num_lst = list(map(int,input().split())) #  공백을 기준으로  값을 나열해 리스트 생성

res = int(input()) # 찾을 값 입력
print(num_lst.count(res)) # 리스트명.count(값)을 입력하면 리스트 내에 값의 개수를 찾아준다.