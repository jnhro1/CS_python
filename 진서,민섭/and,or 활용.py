"""
초성게임

자료형
- 정수형 (int) %d
- 실수형 (float) %f
- 문자형 (string) %s
"""
# 게임 시작 화면
print("=======초성게임=======")
print("게임을 시작하시겠습니까? (예 / 아니오)")

while True :   
    startAnswer = input("입력하세요 : ")
    if startAnswer == "예" :
        print("게임을 시작합니다.")
        print("=================")
        break
    elif startAnswer == "아니오" :
        print("게임을 종료합니다.")
        #프로그램 강제 종료 시키는 명령어 : exit()
        exit()
    else :
        print("잘못된 대답입니다.")

# 첫번째 문제
print("첫번째 문제입니다")
print("")
print("이번 주제는 햄버거 브랜드입니다")
print("===========")
print("=   ㄹㄷㄹㅇ   =")
print("===========")
print("")

while True :
    answer1 = input("입력하세요 : ")
    if answer1 == "롯데리아" :
        print("정답입니다")
    else :
        print("틀렸습니다.")
```

```jsx
"""
and-or 활용.py
두 개의 실수를 입력받아 모두 4.0 이상이면 "A"
모두 3.0 이상이면 "B"
아니면 "C"라고 출력하는 프로그램
"""
num1 = float(input("첫번째 실수를 입력하세요"))
num2 = float(input("두번째 실수를 입력하세요"))

# 만약  4.5 초과거나 0점 미만이면 잘못입력했습니다. 프로그램 종료
if (num1 > 4.5) or (num2 > 4.5) or (num1 < 0) or (num2 < 0) :
    print("잘못 입력했습니다")
    exit()

if (num1 >= 4.0) and (num2 >= 4.0) :
    print("A")
elif (num1 >= 3.0) and (num2 >= 3.0) :
    print("B")
else :
    print("C")
```