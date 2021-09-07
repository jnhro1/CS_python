"""
while누적합활용.py

100 이하의 정수를 입력받아 while문을
이용하여 1부터 입력받은 정수까지의 합을
출력하는 프로그램
"""

input_data = int(input("100이하의 정수를 입력하세요"))

if (input_data > 100) or (input_data < 1) :
    print("잘못 입력하셨습니다")
    exit()

# while에서 변할 값
num = 0

# 누적합을 담을 변수
sum_data = 0

while(num < input_data) :
    num = num + 1
    print(num)
    sum_data = sum_data + num
    print("누적합 : %d" %sum_data)