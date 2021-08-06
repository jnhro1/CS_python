num1 = int(input("주사위를 던져 첫번째로 나온 값을 입력하세요."))
num2 = int(input("주사위를 던져 두번재로 나온 값을 입력하세요."))

if (num1 >=4 and num2 >= 4):
  print("이기셨습니다.")
elif (num1 >=4 or num2 >= 4):
  print("비기셨습니다.")
elif (num1 < 4 and num2 < 4):
  print("지셨습니다.")
