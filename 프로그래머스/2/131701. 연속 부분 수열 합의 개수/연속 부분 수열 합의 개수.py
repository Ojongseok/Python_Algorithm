def solution(elements):
    answer = 0
    
    n=len(elements)
    list_sum=[]
    for i in range(1,n+1):
        for j in range(n):
            if i+j>n:
                check = elements[j:] + elements[:i+j-n]
            else :
                check = elements[j:j+i]
            list_sum.append(sum(check))
    set_sum=set(list_sum)
    answer=len(set_sum)
    
    return answer