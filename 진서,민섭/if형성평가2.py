"""
if형성평가2.py
정수를 입력받아
0이면 zero
양수이면 plus
음수이면 minus
라고 출력하는 프로그램
"""
num = int(input("정수를 입력하세요"))

if num == 0:
    print("zero")
elif num > 0 :
    print("plus")
else :
    print("minus")