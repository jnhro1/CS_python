'''
1.문제의 주제
2. 초성 나타내기
3. 만약 힌트를 입력한다면 힌트주기
4.포기라고 입력하면 "Game failed"가 뜨면서 종료
'''
def giveup():
    print("아쉽게도 정답이 아닙니다.. 너무 어려우시면 '포기' or '힌트'라고 입력해주세요")
def hint_message():
    print("힌트를 보시러면 '힌트'라고 입력해주세요")
heart = 3
heart_icon = "♥"
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
hint_message()
print("ㅂㅁ")

while True:
    for i in range(1,heart+1):
        print(heart_icon, end = " ")
    print("")
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
        giveup()
        heart -= 1
        if heart == 0:
            print("흐어접")
            print("총 점수는 %d입니다"%score)
            exit()
        continue

        
    
#두번째 문제
print("두번째 문제 주제는 아이스크림입니다")
hint_message()
print("ㅇㅅㄹㅌ")

while True:
    for i in range(1,heart+1):
        print(heart_icon, end = " ")
    print("")
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
        giveup()
        heart -= 1
        if heart == 0:
            print("목숨 엔드!")
            print("총 점수 %d입니다"%score)
            exit()
        continue
#3번째 문제
print("이번 주제는 게임 입니다")
hint_message()
print("ㅅㅅㅁㅍㅎ")

while True:
    for i in range(1,heart+1):
        print(heart_icon, end = " ")
    print("")
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
        giveup()
        heart -= 1
        if heart == 0:
            print("허접은 아니군 하지만 탈락")
            print("총 점수는 %d점 이였다"%score)
            exit()
        continue
#4번째문제
print("이번 주제는 사자성입니다 ")
hint_message()
print("ㄷㅇㄱㅇ")
while True:
    for i in range(1,heart+1):
        print(heart_icon, end = " ")
    print("")
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
        giveup()
        heart -= 1
        if heart == 0:
            print("목숨이 다되어 게임이 끝남")
            print("최종 점수는 %d점임"%score)
            exit()
        
#문제 파이브
print("이번 주제는 애니메이션 입니다")
hint_message()
print("ㄱㅁㅇㅋㄴ")

while True:
    for i in range(1,heart+1):
        print(heart_icon, end = " ")
    print("")
    answer5 = input("정답을 입력해주세요 : ")
    if answer5 == "귀멸의 칼날" or "귀멸의칼날":
        score += 1
        print("정답입니다!")
        break
    elif answer5 == "힌트" :
        print("힌트 = '극장판에서 열차안에서 싸움이 일어났었던 애니'")
        continue
    elif answer5 == "포기" :
        print("총 점수는 %d점임 " %score)
        print("ㅂㅂ")
        exit()
    else:
        giveup()
        heart -= 1
        if heart == 0:
            print("마지막인데 목숨이 다되어 아쉽군요")
            print("최종점수는 %d점 이었습니다" %score)
            continue
if heart == 3:
    print("당신은 초성퀴즈의 고수입니다(히든엔딩)")

print("모든 문제를 풀었습니다 축하합니다")
print("최종 점수는 %d점입니다" %score)
print("최종 목숨은 %d개였습니다" %heart)