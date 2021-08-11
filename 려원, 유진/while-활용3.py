```jsx
"""
while활용3.py

점수를 계속 입력을 받다가 0이 입력되면 0을 제외하고
이전에 입력된 자료의 수와 합계, 평균을 출력하는 프로그램
(평균은 반올림하여 소수 둘째자리)
ex) 15 88 97 0
입력된 자료의 개수 = 3
입력된 자료의 합계 = 200
입력된 자료의 평균 = 66.67
"""
# 변수의 갯수, 리스트에 접근할 인덱스값
cnt = 0
# 누적 합계를 저장할 변수
sum_ = 0
num = input("점수를 입력하세요").split()
num = list(map(int, num))
# num = [15, 88, 97, 0]

while num[cnt] != 0:
    sum_ = sum_ + num[cnt]
    cnt = cnt + 1
avg = sum_ / cnt
print("입력된 자료의 개수 = %d" %cnt)
print("입력된 자료의 합계 = %d" %sum_)
print("입력된 자료의 평균 = %.2f" %avg)

"""

정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를
포함하여 합계와 평균을 출력하는 프로그램
(평균은 반올림하여 소수 첫째자리까지 출력)
ex) 1 2 3 4 5 6 7 8 9 10 100
합계 = 155 평균 14.1

정수를 계속 입력 받다가 0이 입력되면
입력된 수중 홀수의 합과 평균을 출력하는
프로그램
(정수 미만은 버림)
"""

cnt = 0
sum_ = 0
num = input("정수를 입력하세요").split()
num = list(map(int, num))
# num = [10, 50, 30, 120]

while True:
    sum_ = sum_ + num[cnt]
    if (num[cnt] >= 100) :
        break
    cnt = cnt + 1
avg = sum_ / cnt
print("입력된 자료의 합계 = %d" %sum_)
print("입력된 자료의 평균 = %.1f" %avg)

"""
정수를 계속 입력 받다가 0이 입력되면
입력된 수중 홀수의 합과 평균을 출력하는
프로그램
(정수 미만은 버림)
5 8 17 6 31 0
홀수의 합 = 53 홀수의 평균 = 17
"""

cnt = 0
sum_ = 0
odd_cnt = 0
num = list(map(int, input("정수를 입력하세요").split()))
# num = [5, 8, 17, 6, 31, 0]

while True:
    if (num[cnt] == 0) :
        break
    if (num[cnt] % 2 == 1):
        sum_ = sum_ + num[cnt]
        odd_cnt = odd_cnt + 1
    cnt = cnt + 1
avg = sum_ / cnt
print("입력된 자료의 합계 = %d" %sum_)
print("입력된 자료의 평균 = %d" %avg)
```