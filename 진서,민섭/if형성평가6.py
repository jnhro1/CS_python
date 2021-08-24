"""
if형성평가6.py
1이나 3을 입력하면 "야호"
2나 4를 입력하면 "무야호"
그 외의 숫자를 입력하면 "유야호" 라고 출력한다.
"""
num = int(input("숫자를 입력하세요"))

if num == 1 or num == 3:
    print("야호")
elif num == 2 or num == 4:
    print("무야호")
else :
    print("유야호")