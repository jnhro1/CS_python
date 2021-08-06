
'''
정수를 입력받다가
0이 입력되면 그때까지 입력받은 홀수의 개수와
짝수의 개수를 출력하는 프로그램을 작성하시오
'''
even = 0
odd = 0

while True:
    num = int(input("숫자를 입력하세요"))
    if num == 0:
        print("짝수는 %d개입니다"%even)
        print("홀수는 %d개입니다"%odd)
        break
    
    
    if num % 2 == 0:
        even += 1
    if num % 2 == 1:
        odd += 1
            
    
    
              
        
                
            
            


