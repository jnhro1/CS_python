'''
10 이하의 정수를 입력받아
입력받은 정수만큼 파이썬 프로그래밍
이라고 출력하는 프로그램
'''
num = int(input("10이하 정수 입력하셈"))
if (num > 10) or (num < 0):
    print("-이상의 수를 입력해주세요")
    exit()
for i in range(num):
    print("파이썬 프로그래밍")
