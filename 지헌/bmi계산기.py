"""
bmi 지수 측정기 (비만)
함수 이름 : bmi
bmi = 몸무게 / (키X키)
18.5이하 = 저체중
18.5 ~ 23 = 정상
23 ~ 25 = 과체중
25 ~ 30 = 비만
30이상 = 고도비만
bmi(키,몸무게) = 호출
"""
name = input("안녕하세요. 당신의 이름은 무엇인가요? ")
print("반갑습니다. %s님." %name[1:3])
height = float(input("당신의 키는 몇입니까? (미터로 해주세요) "))
if height >= 3:
    print("잘못 입력하셨습니다 미터로 다시 입력해주세요 예, 1.39")
    exit()
weight = float(input("당신의 몸무게는 몇인가요? "))
print("키 : %f" %height)
print("몸무게 : %f" %weight)
def bmiFunc(height, weight):
    bmi = weight / (height * height)
    
    if bmi <= 18.5:                                         
        result = "저체중 입니다"
    elif  bmi <= 23:
        result = "정상입니다"
    elif  bmi <= 25:
        result = " 과체중 입니다"                  
    elif  bmi <= 30:
        result = "비만입니다"
    elif bmi >= 30:
        result = "고도비만입니다"
    return result
saveresult =bmiFunc(height,weight)
print(saveresult)

