'''
0이 입력될 때까지 정수를 계속 입력받아
3의 배수와 5의 배수를 제외한 수들의 개수를 출력하는 프로그램
'''
cnt = 0

while True:
    num = int(input("숫자 입력 : "))
    if num == 0:
        break
    if num % 3 == 0:
        continue
    elif num % 5 == 0:
        continue
    cnt += 1
print("개수는 %d개입니다"%cnt)
    
