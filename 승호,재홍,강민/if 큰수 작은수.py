"""
if 큰수, 작은수.py
정수 2개를 입력받아서 큰수를 출력하세요
큰 수 :
두 수가 같습니다
"""
num1 = int(input("첫번째 수는?"))
num2 = int(input("두번째 수는?"))
if num1 < num2 :
  print("큰수 = %d" %num2)
if num1 > num2 :
  print("큰수 = %d" %num1)
if num1 == num2 :
  print("두수가 같습니다")
