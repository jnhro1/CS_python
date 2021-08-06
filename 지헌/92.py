'''
10개의 정수를 입력받아 그 수들 중 짝수의 개수가 몇 개인지 출력하는 프로그램
'''
result = 0
num = list(map(int, input("정수를 입력해주세요").split()))
for i in range(10):
    if num[i] % 2 == 0:
        result += 1
print(result)
