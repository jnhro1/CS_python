num = int(input("정수를 입력해주세요 : "))
result = 0
'''
for i in range(1,num+1):
    if i % 5 == 0:
        result += i
print(result)
'''

for i in range(0,num+1,5):
        result += i
print(result)
    
