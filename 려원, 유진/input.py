'''
height = 160
weight = 60.5
print(height)
print(weight)
print("나의 키는 %d cm 입니다." %(height))
print("나의 몸무게는 %.1f kg 입니다." %(weight))
print("키 : %d cm, 몸무게 : %.1f kg" %(height, weight))
'''
'''
#입력받는 법 : input
# 기본으로 저장되는 자료형
#print("이름을 입력해주세요")
name = input("이름을 입력해주세요")
print(name)
'''
'''
height = input("키를 입력해주세요.")
height = int(height)
print(height+100)
'''
'''
height = float(input("키를 입력해주세요."))
print("%.1f" %(height+100.0))
'''

'''
age = int(input("당신의 나이는 몇살입니까?"))
print(" 당신의 나이는 %d살 이군요." %(age))
'''



num1 = int(input("첫번째 정수를 입력하세요."))
num2 = int(input("두번째 정수를 입력하세요."))
num3 = int(input("세번째 정수를 입력하세요."))
plus = num1 + num2 + num3
avg = (num1 + num2 + num3) / 3
print("%d + %d + %d 의 합은 %d 입니다." %(num1, num2, num3, plus))
print("%d 과 %d, %d의 평균은 %.2f 입니다." %(num1, num2, num3, avg))





