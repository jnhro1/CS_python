'''
1.문제의 주제
2. 초성 나타내기
3. 만약 힌트를 입력한다면 힌트주기
4.포기라고 입력하면 "Game failed"가 뜨면서 종료
'''
#시작
print("초성게임을 시작하시겠습니까? 예 / 아니오")
while True:
    startAnswer = input("입력 플리즈 : ")
    if startAnswer == "예":
        print("게임을 시작하겠습니다")
        break
    
    elif startAnswer == "아니오":
        print("안녕히가세요^^")
        exit()
    else:
        print("잘못된 답변입니다")
        continue
#게임 스타트
print("=========================")
score = 0

#문제1
print("이번 주제는 햄버거입니다")
print("힌트를 보시러면 '힌트'라고 입력해주세요")
print("ㅂㅁ")

while True:
    answer1 = input("정답을 입력해주세요 : ")
    if answer1 == "빅맥":
        score += 1
        #socre = socre + 1
        print("정답입니다!")
        print("====================")
        break
    elif answer1 == "힌트":
        print("힌트는 '맥도날드 대표메뉴'입니다")
        continue
    elif answer1 == "포기":
        print("가셈")
        print("총 점수는 %d점임 " %score)
        exit()
    else:
        print("아쉽게도 정답이 아닙니다.. 너무 어려우시면 '포기' or '힌트'라고 입력해주세요")
        continue
        
    
#두번째 문제
print("두번째 문제 주제는 아이스크림입니다")
print("힌트를 보시려면 '힌트'를 입력해주세요!")
print("ㅇㅅㄹㅌ")

while True:
    answer2 = input("정답을 입력해주세요 : ")
    if answer2 == "엑설런트" :
        score += 1
        print("정답입니다!")
        print("====================")
        break
    elif answer2 == "힌트" :
        print("힌트 = '빙그레의 추억의 아이스크림'")
        continue
    elif answer2 == "포기" :
        print("총 점수는 %d점임 " %score)
        print("포기하셨군요 잘가세요 ^^")
        exit()
    else:
        print("아쉽게도 정답이 아닙니다.. 너무 어려우시면 '힌트' or '포기'라고 입력해주세요")
        continue
#3번째 문제
print("이번 주제는  입니다 (난이도 극악)")
print("힌트를 보시려면 '힌트'를 입력해주세요!")
print("ㅅㅅㅁㅍㅎ")

while True:
    answer3 = input("정답을 입력해주세요 : ")
    if answer3 == "산소미포함" :
        score += 1
        print("정답입니다! 정말 엄청나군요")
        print("====================")
        break
    elif answer3 == "힌트":
        print("힌트 = '숨쉬지마'")
        continue
    elif answer3 == "포기" :
        print("총 점수는 %d점임 " %score)
        print("잘가셈 ㅂㅂ")       
        exit()
    else:
        print("틀렸습니다 힌트를 보시거나 '포기'라고 입력해주세요")
        continue
#4번째문제
print("이번 주제는 사자성입니다 ")
print("힌트를 보시려면 '힌트'를 입력해주세요")
print("ㄷㅇㄱㅇ")
while True:
    answer4 = input("정답을 입력해주세요 : ")
    if answer4 == "도원결의" : 
        score += 1
        print("정답입니다!")
        print("====================")
        break
    elif answer4 == "힌트" :
        print("의형제를 맺음")
        continue
    elif answer4 == "포기" :
        print("총 점수는 %d점임 " %score)
        print("안녕히가세요")
        exit()
    else:
        print("틀림")
#문제 파이브
print("이번 주제는 애니메이션 입니다")
print("힌트를 보시려면 '힌트'를 입력하거나 '포기'라고 입력해주세요")
print("ㄱㅁㅇㅋㄴ")

while True:
    answer5 = input("정답을 입력해주세요 : ")
    if answer5 == "귀멸의 칼날" :
        score += 1
        print("정답입니다!")
        break
    elif answer5 == "힌트" :
        print("힌트 = '극장판에서 열차안에서 싸움이 일어났었던 애니'")
        continue
    elif answer5 == "포기" :
        print("총 점수는 %d점임 " %score)
        print("꺼져")
        exit()
    else:
        print("틀렸습니다 힌트를 보시거나 포기라고 입력해주세요")
        continue
print("모든 문제를 맞춤 ㅊㅊ")
print("최종 점수는 %d점입니다"%score)