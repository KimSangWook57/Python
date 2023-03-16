# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
# 예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때 
# {'led':'on', 'motor':'off', 'switch':off'} 반환. 
# # Hint: dict([['a','b'], ['c', 'd']]) => {'a': 'b', 'c': 'd'}

str1 = 'led=on&motor=off&switch=off'

def strToDict(str):
    # 1차 분리
    sp1 = str.split('&')
    # 2차 분리용 리스트
    sp2 = []
    # 2차 분리
    for i in sp1:
        sp2.append(i.split('='))
    # 딕셔너리에 담기.
    dic1 = dict(sp2)
    # 결과 출력.
    print(dic1)

strToDict(str1)