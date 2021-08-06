
def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b
print("50 과 10계산기")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")


number=int(input("골라"))

if number==1:
    print(add(50,10))


elif number==2:
    print(minus(50,10))


elif number==3:
    print(multi(50,10))



elif number==4:
    print(div(50,10))

else:
    print("잘못 입력했습니다")


    








