"""
list 개념.py
여러개의 값을 하나의 변수에 담을 수 있다.
하나의 list 변수에 다양한 자료형을 담을 수 있다.
음수 인덱스가 가능하다. (문자열도) 하지만 사용을 지양해야함.
인덱싱 추출값 : 데이터만
슬라이싱 추출값 : 리스트
"""
season = ["봄", "여름", "가을", "겨울"]
grade = [1, 2, 3]
hello = "안녕하세요"

# 리스트의 인덱싱

print(season[1])
""""
print(season[0] + season[1])
print(grade[1] + grade[2])
"""
# 리스트의 슬라이싱
print(season[0:3])
print(season[0:2])

# 리스트의 길이 구하기 : len
print(len(season))

# 리스트 값 수정하기 : 인덱싱
# grade = [1, 2, 3]
grade[1] = 5
print(grade)

# 리스트 값 삭제하기 : 인덱싱, 슬라이싱
# grade = [1, 5, 3]
del grade[2]
print(grade)

num = [1,2,3,4,5]
del num[2:]
print(num)

# 리스트 값 추가하기
# append : 무조건 list 끝에 추가
num.append(3)
num.append(4)
num.append(6)
print(num)

# insert : 원하는 부분에 추가
num.insert(4,5)
print(num)

#### 중요도 낮음

# 리스트 요소 제거 : remove(x)
# 리스트에서 처음으로 나오는 x값 제거
test = [1, 2, 3, 1, 2, 3]
test.remove(3)
print(test)

# 리스트 요소 끄집어내기 : pop
# 리스트의 맨 마지막 요소를 돌려주고
# 그 요소를 삭제한다.
# [1, 2, 1, 2, 3]
popNum = test.pop()
print(popNum)
print(test)

# 리스트에 포함된 요소 x의 개수 세기 : count
# [1, 2, 1, 2]
print(test.count(1))