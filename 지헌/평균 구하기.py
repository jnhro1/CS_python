'''
정수를 계속 입력받다가 0이 입력되면
0을 제외하고 이전에 입력된 자료의 수와 합계, 평균을 출력하는 프로그램
'''
result = 0
cnt = 0
while True:
    num = int(input("숫자 입력 : "))
    if num == 0:
        break
    cnt += 1
    
    result += num
    average = result / cnt

print("자료의 수 : %d , 합계 : %d , 평균 : %.2f"%(cnt,result,average)) 
        
   
        
        
        
