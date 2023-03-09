# 다음 딕셔너리에 대한 물음에 답하라.

days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

# 사용자가 월을 입력하면 해당 월의 일수를 출력하라.
# month1 = input("Month : ")
# 키값이 title 형식이므로, 이를 활용했다.
# print(days[month.title()])

# 알파벳 순서로 모든 월을 출력하라.
alpha_month = list(days.keys())
print(sorted(alpha_month))

# 일수가 31인 월을 모두 출력하라.
month_31 = []
for i in days:
    if days[i] == 31:
        month_31.append(i)

print(month_31)

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라.
# 키값과 밸류값의 위치를 바꾼 뒤 일수를 기준으로 정렬 후,
# 다시 이름이 앞으로 오게끔 정렬.
days_item = days.items()
# 키와 밸류의 위치를 바꾸는 코드.
days_item = [ (day, month) for (month, day) in days_item]
# 안의 값을 일수로 정렬.
days_item.sort()
# 다시 키와 밸류의 위치를 바꾸는 코드.
days_item = [ (month, day) for (day, month) in days_item]
# 출력.
print(days_item)

# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month2 = input("Month : ")

for i in days:
    if i[0:3] == month2.title():
        print(days[i])
