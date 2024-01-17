def solution(n):
    answer = 0
    
    arr = list(map(int, str(n)))
    arr.sort(reverse=True)
    
    x= "".join(map(str, arr))
    answer= int(x)
    
    return answer