"""
while형성평가1.py

정수를 입력받아 1부터 입력받은 정수까지를
차례대로 출력하는 프로그램
5
1 2 3 4 
"""

input_data = int(input("정수를 입력하세요"))

# while에서 변할 값
num = 0

while(num < input_data) :
    num = num + 1
    print(num)