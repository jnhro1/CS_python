'''
5명의 성적을 입력받아서
총점과 평균을 출력하는 프로그램
(평균은 반올림하여 소수 첫째자리까지 출력)
'''
result = 0
grade = list(map(int, input("입력 너의 성적 : ").split()))
for i in range(5):
    result += grade[i]
avg = result / 5
print("총점 : %d 평균 : %.1f "%(result,avg))

    
    
