def solution(n):
    answer = 0
    
    for num in range(2,n+1):
        isPrime = False
        for i in range(2,int(num**(1/2))+1):
            if num%i==0:
                isPrime=True
                break
        if isPrime==False:
            answer+=1
    
    return answer