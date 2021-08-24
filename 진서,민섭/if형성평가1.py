"""
if형성평가1.py
두 개의 정수를 입력받아 큰 수에서 작은 수를
뺀 차를 출력하는 프로그램
5 10 -> 5
10 5 -> 5
"""
num1 = int(input("정수를 입력하세요"))
num2 = int(input("정수를 입력하세요"))

if num1 > num2 :
    print(num1-num2)
else :
    print(num2-num1)

# 삼항연산자 사용
result = num1-num2 if num1 > num2 else num2-num1

print("차이 : %d" %result)