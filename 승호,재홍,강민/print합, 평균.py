"""
국어, 영어, 수학, 컴퓨터 과목의 점수를 입력받아서 총점과 평균을 구하는 프로그램
평균은 소수점 한자리까지 출력
"""
korea = int(input("국어 점수는?"))
english = int(input("영어 점수는?"))
math = int(input("수학 점수는?"))
computer = int(input("컴퓨터 점수는?"))

hap = korea + english + math + computer
avg = hap / 4

print("총점 = %d" %hap)
print("평균점 = %.1f" %avg)
