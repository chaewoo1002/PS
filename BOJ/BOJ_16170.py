import datetime

now = datetime.datetime.now() + datetime.timedelta(hours=9) # 한국은 UTC+9 시간을 사용한다. 세계 표준시 UTC+0으로 맞춰주도록 하자.

print(now.year)
print(now.month)
print(now.day)