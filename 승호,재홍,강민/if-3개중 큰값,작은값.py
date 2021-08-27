"""
if-3개중 큰값,작은값.py
정수 3개를 입력 받아 그 중 가장 큰 수와 작은수를 출력하는 프로그램
max_data : 가장 큰 수
min_data : 가장 작은 수
num1 num2 num3
"""
num1 = int(input("정수를 입력하세요."))
num2 = int(input("정수를 입력하세요."))
num3 = int(input("정수를 입력하세요."))

if num1 > num2 :
    max_data = num1
    min_data = num2
else :
    max_data = num2
    min_data = num1

if num3 > max_data :
    max_data = num3
else :
    if num3 < min_data :
        min_data = num3

print("가장 큰 수 : %d" %max_data)
print("가장 작은 수 : %d" %min_data)