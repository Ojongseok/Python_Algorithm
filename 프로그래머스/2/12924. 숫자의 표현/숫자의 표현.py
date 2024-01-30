def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        a = i
        hap=a
        while hap<n:
            a+=1
            hap+=a
        if hap==n:
            answer+=1
    
    return answer