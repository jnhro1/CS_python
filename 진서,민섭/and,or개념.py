"""
andor.py
and : 두 조건식이 모두 참일 때
or : 두 조건식 중 하나만 참일 때

주사위를 두번 던져서 나온 수를 입력받아 두 수가 모두 4 이상이면 "이겼습니다."
한 개만 4 이상이면 "비겼습니다"
모두 4 미만이면 "졌습니다"
"""
num1 = int(input("주사위 값을 입력하세요"))
num2 = int(input("주사위 값을 입력하세요")) 

if (num1 >= 4) and (num2 >= 4):
    print("이겼습니다.")
elif (num1 >= 4) or (num2 >= 4):
    print("비겼습니다.")
elif (num1 < 4) and (num2 < 4):
    print("졌습니다.")