```jsx
"""
if-elif-else 활용.py
복싱 체급 프로그램
몸무게를 입력받아 체급을 출력하는 프로그램
몸무게가 50.8 kg 이하 - Flyweight
61.23kg 이하 - Lightweight
72.57kg 이하 - Middleweight
88.45kg 이하 - Cruiserweight
그 이상은 Heavyweight

"""
print("복싱 체급 안내 프로그램 입니다")
print("====================")

weight=float(input("몸무게를 입력하세요. "))

if weight < 0 :
    print("잘못 입력하셨습니다")
    exit()

if weight <= 50.8 :
    print("Flyweight")
elif weight <= 61.23 :
    print("Lightweight")
elif weight <= 72.57 :
    print("Middleweight")
else :
    print("Heavyweight")
```