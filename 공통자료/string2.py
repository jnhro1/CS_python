#count : 문자열에서 찾고자 하는 문자 갯수 반환
fruit = "apple"
print(fruit.count('p'))

#index : 찾고자 하는 문자의 위치 반환
hello = "coding is happy"
print(hello.index('g'))

#upper : 소문자를 대문자로 바꾸기
upperHello = hello.upper()
#upperHello = "CODING IS HAPPY"
print(upperHello)

#lower : 대문자를 소문자로 바꾸기
print(upperHello.lower())

#replace : 특정 문자를 다른 문자로 대체하기
print(hello.replace('coding','sleepling'))
