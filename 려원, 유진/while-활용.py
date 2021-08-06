'''
num = 1
result = 0

while num <= 10:
    print(num)
    result  = result + num
    num = num + 1

print(result)
'''
num = int(input("100 이하의 정수를 입력해주세요."))
if num > 100:
    print("잘못 입력된 값입니다.") 
    exit()
i = 1
result = 0
while i <= num:
    result = i + result
    i = i + 1

print(result)








