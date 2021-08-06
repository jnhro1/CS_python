'''
자연수를 입력받아서 1부터
입력받은 수까지의 합을 출력하는 프로그램
'''
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

    
          
          
          
