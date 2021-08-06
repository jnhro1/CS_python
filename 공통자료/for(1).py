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

'''
문자를 입력받아서
입력받은 문자를
20번 반복하여 출력하는 프로그램
'''
words = input("문자를 입력하세요 : ")
for i in range(20):
    print(words,end = " ")

'''
10부터 20까지의 숫자를 차례대로 출력하는 프로그램
'''
for i in range(10,21):
    print(i)

'''
1부터 20까지의 홀수를 차례로 출력하는 프로그램
'''
for i in range(1,20):
    if i % 2 == 1:
        print(i)
'''
1부터 20까지의 홀수를 차례로 출력하는 프로그램
'''
for i in range(1,21,2):
    print(i)


'''
한 개의 수를 입력받아
1부터 입력받은 수까지의 짝수를
차례대로 출력하는 프로그램
(입력받은 수는 2 이상 50 이하의 정수이다)
'''
num = int(input("숫자 입력 (2이상 50이하) : "))
if num < 2 or num > 50:
          print("2이상, 50이하의 숫자로 입력해주세요")
          exit()
for i in range(2,num+1,2):
          print(i)

'''
자연수를 입력받아서 1부터
입력받은 수까지의 합을 출력하는 프로그램
'''

result = 0
num = int(input("자연수 입력 : "))
if num <= 0:
    print("잘못된 방법입니다 자연수를 입력해주세요")
    exit()
for i in range(1,num+1):
    result += i
print(result)


'''
정수를 입력받아서
입력받은 정수부터
100까지의합을
출력하는 프로그램
(입력받는 정수는 100 이하의 자연수이다)
'''
result = 0
num = int(input("자연수 입력(100이하만) : "))
if num <=0 or num > 100:
    print("잘못된 방법입니다 100이하 자연수를 입력해주세요")
for i in range(num,101):
    result  += i
print(result)
