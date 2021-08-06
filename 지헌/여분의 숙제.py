num = int(input("10개 이하의 과목수를 입력해주세요 : "))
if num >= 10:
    print("10개 이하로 입력해주세요")
    exit()
score = list(map(int, input("과목들의 점수를 입력해주세요 : ").split()))
result = 0
for i in range(num):
    result += score[i]
avg = result / num
if avg >= 80:
    print("pass")
else:
    print("fail")
           
