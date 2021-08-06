강제 종료하는 명령어 exit()
두 비교식의 공통된 부분 (교집합) and
두 비교식의 합한 부분 (합집합) or

score = int(input("점수를 입력해주세요."))
if (score <0 or score > 100):
  print("잘못 입력된 값입니다.")
  exit()
elif score >= 90:
  print("수")
elif score >= 80:
  print("우")
elif score >= 70:
  print("미")
elif score >= 60:
  print("양")
elif score < 60:
  print("가")





  
