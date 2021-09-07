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

# 목숨
heart = 3
heartIcon = "♥"

# 점수
score = 0

def printHeart() :
    for i in range(1, heart+1) :
        print(heartIcon, end = " ")
    

# 첫번째 문제
printHeart()
print("")
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
        score = score + 20
        break
    elif answer1 == "힌트" :
        print("롯데마트의 두글자를 땄습니다.")
        continue
    elif answer1 == "포기" :
        print("벌써부터 포기라니,,, 실망이네요")
        print("점수 : %d" %score)
        exit()
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        # 목숨 차감
        heart = heart - 1
        printHeart()
        print("")
        # 게임 종료 여부 확인
        if heart == 0 :
            print("목숨 종료!")
            print("점수 : %d" %score)
            exit()
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
        score = score + 20
        break
    elif answer2 == "힌트" :
        print("조정석 주연")
        continue
    elif answer2 == "포기" :
        print("벌써부터 포기라니,,, 실망이네요")
        print("점수 : %d" %score)
        exit()
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        # 목숨 차감
        heart = heart - 1
        printHeart()
        print("")
        # 게임 종료 여부 확인
        if heart == 0 :
            print("목숨 종료!")
            print("점수 : %d" %score)
            exit()
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
    answer3 = input("입력하세요 : ")
    if answer3 == "메종키츠네" :
        print("정답입니다")
        score = score + 20
        break
    elif answer3 == "힌트" :
        print("여우")
        continue
    elif answer3 == "포기" :
        print("벌써부터 포기라니,,, 실망이네요")
        print("점수 : %d" %score)
        exit()
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        # 목숨 차감
        heart = heart - 1
        printHeart()
        print("")
        # 게임 종료 여부 확인
        if heart == 0 :
            print("목숨 종료!")
            print("점수 : %d" %score)
            exit()
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
    answer4 = input("입력하세요 : ")
    if answer4 == "홈런볼" :
        print("정답입니다")
        score = score + 20
        break
    elif answer4 == "힌트" :
        print("야구")
        continue
    elif answer4 == "포기" :
        print("벌써부터 포기라니,,, 실망이네요")
        print("점수 : %d" %score)
        exit()
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        # 목숨 차감
        heart = heart - 1
        printHeart()
        print("")
        # 게임 종료 여부 확인
        if heart == 0 :
            print("목숨 종료!")
            print("점수 : %d" %score)
            exit()
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
    answer5 = input("입력하세요 : ")
    if answer5 == "멕시카나" :
        print("정답입니다")
        score = score + 20
        break
    elif answer5 == "힌트" :
        print("강다니엘이 모델임")
        continue
    elif answer5 == "포기" :
        print("벌써부터 포기라니,,, 실망이네요")
        print("점수 : %d" %score)
        exit()
    else :
        print("틀렸습니다.")
        # 틀렸을때 힌트 출력
        print("정 모르겠다면 '힌트'라고 입력해보세요")
        # 목숨 차감
        heart = heart - 1
        printHeart()
        print("")
        # 게임 종료 여부 확인
        if heart == 0 :
            print("목숨 종료!")
            print("점수 : %d" %score)
            exit()
        continue

# 문제 다 맞췄을 때
print("축하합니다! 당신은 진정한 초성왕!")
print("점수 : %d" %score)