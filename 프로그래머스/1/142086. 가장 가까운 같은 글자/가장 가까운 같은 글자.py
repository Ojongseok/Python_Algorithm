def solution(s):
    answer = [-1 for _ in range(len(s))]
    
    for i, c in enumerate(s):
        for j in range(i-1,-1,-1):
            if s[i] == s[j]:
                answer[i]=i-j
                break
    
    return answer