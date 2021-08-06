"""
string.py
문자형 (string) %s
컴퓨터는 숫자를 0부터 센다.
hello[n] 인덱싱 (0~n-1)
hello[n:m]
"""

hello = "안녕하세요"
print(hello[0])



name = input("당신의 이름을 입력해주세요.")
print("안녕하세요, %s님." %(name[1:3]))
print("당신의 성은 %s 이군요." %(name[0]))

