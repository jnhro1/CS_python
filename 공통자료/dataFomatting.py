"""
변수 : 데이터가 저장되는 공간
컴퓨터에는 메모리가 존재한다.
데이터 타입 : 문자열, 숫자
정수형(소숫점 x), 실수형(소숫점 o)
변수를 만든다 = 변수를 선언한다.
"""
#문자열(string) %s
name = "나현"
#정수형(int) %d
age = 13
#실수형(float) %f
height = 180.6 

#문자열 출력
print("안녕하세요")
#변수 출력
print(name)
#문자열 + 변수 출력 : 데이터 포매팅(format)
print("이름 : %s" %name)
print("나이 : %d" %age)
print("키 : %.1f" %height)


