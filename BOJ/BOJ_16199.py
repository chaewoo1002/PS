born_year, born_month, born_day = map(int, input().split())
year, month, day = map(int, input().split())

if born_month < month:
  international_age = year - born_year
elif born_month == month and born_day <= day:
  international_age = year - born_year
else:
  international_age = year - born_year-1

korean_age = year - born_year+1

age = year - born_year

print(international_age, korean_age, age, sep="\n") # 만나이, 세는나이, 연나이를 줄바꿈으로 출력