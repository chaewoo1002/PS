import sys # sys 모듈 import

num = int(input())

for i in range(num):
    h, w, n = map(int, sys.stdin.readline().split()) # 반복문 내에서 입력을 받아야하므로 사전에 시간초과 방지
    room_num = n//h + 1 # n에서 건물 층수를 나눈 값 + 1이 객실의 호수가 됨
    floor = n % h
    if n % h == 0:           # n이 건물 층수의 배수라면
        room_num = n // h    # 객실의 호수는 n에서 건물 층수를 나눈 몫이 됨
        floor = h
    print(floor * 100 + room_num)