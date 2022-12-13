s, k, h = map(int, input().split())
if s + k + h >= 100: # 입력받은 값들의 총합이 100 이상일때
    print("OK");
else:
    if s < k and s < h:
        print("Soongsil");
    elif k < s and k < h:
        print("Korea");
    elif h < s and h < k:
        print("Hanyang");