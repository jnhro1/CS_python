"""
이력서 입력기
"""
name = input("이름이 무엇인가요?")

age = int(input("나이는 몇살인가요?"))

height = float(input("키는 몇인가요?소수점까지 입력해주세요"))

print("이름 : %s , 나이 : %d , 키 : %.1f" %(name, age, height))
