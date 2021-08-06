"""
if-elif-else
if 조건1:
elif 조건2:
elif 조건3:
else:
90점 이상이면 A학점
80점 이상 89점 B학점
70점 이상 79점 C학점
60점 이상 69점 D학점
60점 미만 F 학점
"""
score = int(input("점수를 입력하세요"))
if score >= 90 :
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")

    
