print(" 안녕하세요 BMI 측정기입니다")
name=input("이름이 무엇인가요?")
print("  반갑습니다 %s님"%name[1:3])
height=float(input("키를 입력하세요.(m)"))
if(height>3):
    print("잘못입했습니다")
    exit(0)
weight=float(input("몸무게를 입력하세요(Kg)"))

def  bmiFunc(height,weight):
    bmi = weight/(height*height)
    if bmi<=18.5:
        result="저체중입니다.밥좀 많이 드세요"
    elif bmi<=23:
        result="정상입니다.지금의 생활을 꾸준히 해주세요."
    elif bmi<=25:
        result="과체중 의심 입니다.운동을 조금씩 해주세요"
    elif bmi<=30:
        result="비만입니다.하루에 스쿼트를 20개씩 해주세요"
    elif bmi>30:
        result="고도비만입니다.그만좀 먹으시고 운동좀 하세요"

    return print(result)
bmiFunc(height,weight)
