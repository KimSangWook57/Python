# end를 사용해서 끝부분을 어떻게 할지 정할 수 있다. 디폴트값 = "/n"
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
