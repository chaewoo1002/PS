# n = input()
# num = input()
# add_num = 0
# for i in num:
#     add_num += int(i) 
# print(add_num)

# 위는 기존 코드, 아래는 정답을 참고 해 간략화한 새로운 코드

n = input()                     # 사실 여긴 의미가 없다, 아래 코드 한줄만 있어도 정답이지만, 입력이 두줄이기에 첫번째 줄을 걸러주는 코드

print(sum(map(int,input())))    # ex)12345가 입력되었으면 1개씩 1, 2, 3, 4, 5로 분리하고 sum()을 통해 총합을 구함