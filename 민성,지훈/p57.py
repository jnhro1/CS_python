"""
p57.py
정수 2개를 입력받아서 큰 수와 작은 수를 출력하는 프로그램
정수를 입력하세요 : 5
정수를 입력하세요 : 10
큰 수 : 10 작은 수 : 5
"""
num1 = int(input("정수를 입력하세요"))
num2 = int(input("정수를 입력하세요"))
if num1 == num2:
    print("두 수가 같습니다")
elif num1 > num2:
    print("큰 수 : %d 작은 수 : %d" %(num1,num2))
elif num1 < num2:
    print("큰 수 : %d 작은 수 : %d" %(num2,num1))