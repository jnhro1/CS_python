"""
if-else-활용
나이를 입력받아 20살 이상이면 An adult
그렇지 않으면 몇 년이후에 성인이 되는지
() years 라는 메세지를 출력하는 프로그램
ex.
50 > An adult
13 > 7 years
9 > 11 years
"""
age = int(input("나이를 입력하세요."))

if age >= 20 :
    print("An adult")
else :
    print("%d years" %(20-age))