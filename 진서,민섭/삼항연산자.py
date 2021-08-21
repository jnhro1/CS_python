"""
삼항연산자.py

if 조건문에 두개의 수를 비교하면서,
참과 거짓에 따라 무조건 둘 중 하나를 반환할 때

두 정수를 입력받아서 더 큰 수를 max_ 에 넣는 프로그램
"""
num1 = int(input("정수를 입력하세요"))
num2 = int(input("다른 정수를 입력하세요"))

if num1 == num2 :
    print("서로 다른 두 수를 입력하세요")
    exit()

"""
if num1 > num2 :
    max_ = num1
else :
    max_ = num2
"""
# max_ = num1 if num1 > num2 else num2
max_ = num2  if num1 < num2 else num1

print("max : %d" %max_)