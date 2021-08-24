"""
초성게임
자료형
- 정수형 (int) %d
- 실수형 (float) %f
- 문자형 (string) %s
"""
# 게임 시작 화면
print("=======초성게임=======")
print("게임을 시작하시겠습니까? (예 / 아니오)")

while True :   
    startAnswer = input("입력하세요 : ")
    if startAnswer == "예" :
        print("게임을 시작합니다.")
        print("=================")
        break
    elif startAnswer == "아니오" :
        print("게임을 종료합니다.")
        #프로그램 강제 종료 시키는 명령어 : exit()
        exit()
    else :
        print("잘못된 대답입니다.")

# 첫번째 문제
print("첫번째 문제입니다")
print("")
print("이번 주제는 햄버거 브랜드입니다")
print("===========")
print("=   ㄹㄷㄹㅇ   =")
print("===========")
# 문제 제시할 때 힌트 출력
print("")

while True :
    answer1 = input("입력하세요 : ")
    if answer1 == "롯데리아" :
        print("정답입니다")
        break
    elif answer1 == "힌트" :
        print("롯데마트의 두글자를 땄습니다.")
        continue
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        continue
# 두번째 문제
print("두번째 문제입니다")
print("")
print("이번 주제는 드라마입니다")
print("================")
print("=   ㅅㄱㄹㅇㅇㅅㅅㅎ   =")
print("================")
# 문제 제시할 때 힌트 출력
print("")
while True :
    answer2 = input("입력하세요 : ")
    if answer2 == "슬기로운의사생활" :
        print("정답입니다")
        break
    elif answer2 == "힌트" :
        print("조정석 주연")
        continue
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        continue
# 세번째 문제
print("세번째 문제입니다")
print("")
print("이번 주제는 브랜드입니다")
print("================")
print("=   ㅁㅈㅋㅊㄴ   =")
print("================")
# 문제 제시할 때 힌트 출력
print("")
while True :
    answer2 = input("입력하세요 : ")
    if answer2 == "메종키츠네" :
        print("정답입니다")
        break
    elif answer2 == "힌트" :
        print("여우")
        continue
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        continue
# 네번째 문제
print("네번째 문제입니다")
print("")
print("이번 주제는 과자입니다")
print("================")
print("=   ㅎㄹㅂ  =")
print("================")
# 문제 제시할 때 힌트 출력
print("")
while True :
    answer2 = input("입력하세요 : ")
    if answer2 == "홈런볼" :
        print("정답입니다")
        break
    elif answer2 == "힌트" :
        print("야구")
        continue
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        continue
# 다섯번째 문제
print("다섯번째 문제입니다")
print("")
print("이번 주제는 치킨입니다")
print("================")
print("=   ㅁㅅㅋㄴ   =")
print("================")
# 문제 제시할 때 힌트 출력
print("")
while True :
    answer2 = input("입력하세요 : ")
    if answer2 == "멕시카나" :
        print("정답입니다")
        break
    elif answer2 == "힌트" :
        print("강다니엘이 모델임")
        continue
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        continue
