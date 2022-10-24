# away_team = list(map(int, input().split())) # 각 팀의 리스트 생성
# home_team = list(map(int, input().split()))

# print(away_team[0]*6 + away_team[1]*3 + away_team[2]*2 + away_team[3]*1 + away_team[4]*2, end=" ") # 리스트에 점수 값 곱한 후 출력
# print(home_team[0]*6 + home_team[1]*3 + home_team[2]*2 + home_team[3]*1 + home_team[4]*2)

output = []
for i in range(2):
    t, f, s, p, c = list(map(int, input().split()))
    output.append(t*6 + f*3 + s*2 + p + c*2)
for i in output:
    print(i, end=' ')