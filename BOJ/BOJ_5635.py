import sys

lst = []

for _ in range(int(input())):
    num, day, month, year = sys.stdin.readline().rstrip().split() # rstrip()은 문자열 가장 오른쪽의 공백을 제거
    day, month, year = map(int, (day, month, year)) # 년, 월, 일만 정수 자료형으로 변경 
    lst.append((year, month, day, num))

lst.sort() # 리스트 오름차순 정렬

print(lst[-1][3]) # 인덱스 값에 -1을 입력할 경우 가장 마지막 인덱스 값 출력 => 오름차순 정렬 상태이므로 가장 큰 값이 출력됨
print(lst[0][3])  # 오름차순 상태에서 인덱스 값 0은 가장 첫번째 값 => 최소값을 출력

# 저 오늘 생일이에요 1년에 단 하루뿐인데 혼자 이러고 있으니.. 최악이네 ㅎ