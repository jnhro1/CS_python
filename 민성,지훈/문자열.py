name=input("이름을 입력해 주세요")
#문자열 포매팅
print("안녕하세요 %s님"%name)
#문자열 인덱스
print("당신의 성은 %s입니다"%name[0])
#문자열 슬라이싱
print("당신의 이름은 %s 입니다"%name[1:3])
#문자열 갯수 세기 len(변수명)
print("당신의 이름은 %s 글자 입니다"%len(name))
print("Banna라는 글자에는 n의 갯수는%d개이고 a의 갯수는 %d개 가 있다"%(name.count("n"),name.count("a")))
