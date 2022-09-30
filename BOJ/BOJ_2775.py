import sys

n = int(input())

for _ in range(n):
    floor = int(sys.stdin.readline())
    room_num = int(sys.stdin.readline())
    floor_0 = [x for x in range(1, room_num + 1)]  # 코드 간략화를 위해 list comprehension 기능 사용(리스트 생성)
                                                   # https://mingrammer.com/introduce-comprehension-of-python/
    for i in range(floor): 
        for j in range(1, room_num): # 호실 번호, 1 ~ (room_num-1) 까지 반복
            floor_0[j] += floor_0[j-1] # 층에 따라 각 호실의 사람 수 값 변경
    print(floor_0[-1]) # 리스트 내의 가장 마지막 값 출력