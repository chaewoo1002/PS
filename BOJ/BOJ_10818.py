# n = int(input())

# lst =  list(map(int, input().split()))
# lst_min = lst[0]
# lst_max = lst[0]

# for i in lst[1:]:
#     if lst_min > i: 
#         lst_min = i
#     elif lst_max < i: 
#         lst_max = i

# print(lst_min, lst_max)

# 파이썬은 이미 리스트 내의 최대, 최소값을 찾아내주는 메서드가 구현되어 있다. 굳이 사용을 안한다면 위의 코드와 같이 풀 수 있지만, 
# 힘들게 만들어 이미 구현되어 있는 메서드는 세상의 이치에 맞게끔 사용 해주도록 하자

n = int(input())
lst = list(map(int, input().split()))

print(min(lst), max(lst))