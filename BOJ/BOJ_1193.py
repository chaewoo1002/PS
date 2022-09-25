n = int(input())

lne = 0 # 몇번째 줄인지 표시
end = 0

while n > end:
    lne += 1
    end += lne

dif = end - n
if lne%2 == 0:  # 짝수번째 라인일때는 분모가 1씩 작아지고 분모가 1씩 커진다
    nmt = lne - dif # nmt는 분자(numerator)의 약자
    dmt = dif + 1   # dmt는 분모(denominator)의 약자
else:   # 홀수번째 라인일때는 분자가 1씩 커지고 분모가 1씩 작아진다
    nmt = dif + 1
    dmt = lne - dif

print(f"{nmt}/{dmt}")