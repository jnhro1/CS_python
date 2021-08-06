num1 = int(input("첫번째 정수를 입력해주세요."))
num2 = int(input("두번째 정수를 입력해주세요."))
num3 = int(input("세번째 정수를 입력해주세요."))
if (num1 > num2):
 max = num1
else:
   max = num2
if (num1 > num3):
 max = num1
else:
   max = num3

if (num1<num2):
 min = num1
else:
  min = num2
if (num1 < num3):
  min = num1
else:
    min = num2
    
print("가장 큰 정수는 %d 입니다." %(max))
print("가장 작은 정수는 %d 입니다." %(min))
  
