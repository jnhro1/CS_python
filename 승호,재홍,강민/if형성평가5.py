"""
if형성평가5.py
1~12 사이의 정수를 입력받아 입력받은 월의 날수를
출력하는 프로그램
1 > 1월은 31일입니다.
month 
1 - 31
2 - 28
3 - 31
4 - 30
5 - 31
6 - 30
7 - 31
8 - 31
9 - 30
10 - 31
11 - 30
12 - 31
"""
month = int(input("알고싶은 달을 입력하세요: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    print("%d월은 31일 입니다" %month)
elif month == 4 or month == 6 or month == 9 or month == 11 :
    print("%d월은 30일 입니다" %month)
elif month == 2 :
    print("%d월은 28일 입니다" %month)
else :
    print("잘못입력하셨습니다.")