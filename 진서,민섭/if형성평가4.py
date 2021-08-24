"""
if형성평가4.py
1번은 개
2번은 고양이
3번은 꽃게
로 정하고
번호를 입력하면 번호에 해당하는 동물을 출력하는 프로그램
해당 번호가 없으면 "I don't know" 라고 출력한다.
"""
print("=====번호판=====")
print(" 1. 개 ")
print(" 2. 고양이 ")
print(" 3. 꽃게 ")
print("==============")
print(" ")

num = int(input("번호를 입력하세요"))

if num == 1:
    print("개")
elif num == 2:
    print("고양이")
elif num == 3:
    print("꽃게")
else :
    print("I don't know")
