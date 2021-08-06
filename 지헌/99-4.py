'''
100 이하의 자연수 n을 입력받고 n개의 정수를 입력받아
평균을 출력하는 프로그램
(평균은 반올림하여 소수 들째자리까지 출력)
'''
result = 0
num = int(input("자연수를 입력해주세요 : "))
if num > 100:
    print("100 이하의 자연수를 입력해주세요")
    exit()
for i in range(1,num+1,1):
    num2 = int(input("정수를 입력해주세요 : "))
    result += num2
avg = result / num 
print("%.2f"%avg)
