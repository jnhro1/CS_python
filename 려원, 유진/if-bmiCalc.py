print("bmi 계산기입니다")
height = float(input("키를 입력해주세요."))
weight = float(input("몸무게를 입력해주세요."))
bmi = weight / ((height * 0.01) * (height * 0.01))
if bmi > 30:
  print("당신의 bmi는 %.2f 입니다. 고도비만이시네요." %(bmi))
elif (bmi >=25 or bmi < 30):
  print("당신의 bmi는 %.2f 입니다. 비만이시네요." %(bmi))
elif (bmi >= 23 or bmi < 25):
  print("당신의 bmi는 %.2f 입니다. 과체중이시네요." %(bmi))
elif (bmi >= 18.5 or bmi < 23):
  print("당신의 bmi는 %.2f 입니다. 정상체중이시네요." %(bmi))
else:
   print("당신의 bmi는 %.2f 입니다. 저체중이시네요." %(bmi))


