"""
두 정수를 입력받아서 나눈 몫과 나머지를 다음과 같은 형식으로 출력하는 프로그램
35 10
35 / 10 = 3...5
"""
num1 = int(input("첫번재 수는?"))
num2 = int(input("두번째 수는?"))

print(" %d / %d = %d ... %d " %(num1, num2, num1 / num2, num1 % num2))

