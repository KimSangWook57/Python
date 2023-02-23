# 문제 2 : 사과 총 가격 계산
# 개수 * 가격 + 개수 * 가격 * 부가세율 / 100 = 총 가격

count = int(input("개수 입력(개) : "))
price = int(input("가격 입력(원) : "))
tax = float(input("부가세율 입력(%) : "))

totalPrice = count * price + count * price * tax / 100
print(f"개수 : {count}개, 가격 : {price}원, 부가세율 : {tax:.2f}%, 총 가격 : {totalPrice:.0f}원")

