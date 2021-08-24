"""
삼항연산자 활용.py
3개의 정수를 입력받아 삼항 연사자를 이용하여
입력받은 수들 중 최소값을 출력하는 프로그램

min_data : 최솟값
num1 num2 num3
"""
num1 = int(input("정수를 입력하세요"))
num2 = int(input("정수를 입력하세요"))
num3 = int(input("정수를 입력하세요"))

min_data = num2 if num1 > num2 else num1
min_data = min_data if min_data < num3 else num3

print("최솟값 : %d" %min_data)