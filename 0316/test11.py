import datetime

# 현재 날짜
today = datetime.date.today()

# 100일 후의 날짜
hundred_days_later = today + datetime.timedelta(days=100)

# 1000일 후의 날짜
thousand_days_later = today + datetime.timedelta(days=1000)

# 결과 출력
print("100일 후:", hundred_days_later)
print("1000일 후:", thousand_days_later)

import calendar

# 2023년 3월의 달력을 출력합니다.
print("2023년 3월의 달력:")
print(calendar.month(2023, 3))

# 2023년 3월 15일의 요일을 확인합니다. (월요일: 0, 화요일: 1, ..., 일요일: 6)
year = 2023
month = 3
day = 15
weekday = calendar.weekday(year, month, day)
print("2023년 3월 15일은 요일 인덱스 {}에 해당하는 요일입니다.".format(weekday))

# 요일 인덱스를 사용하여 요일 이름을 가져옵니다.
weekday_name = calendar.day_name[weekday]
print("2023년 3월 15일은 {}입니다.".format(weekday_name))
