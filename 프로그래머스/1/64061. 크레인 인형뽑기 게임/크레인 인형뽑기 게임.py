def solution(board, moves):
    answer = 0
    
    n= len(board)
    arr=[[] for _ in range(n)]
    result=[]
    
    for b in board:
        for i, v in enumerate(b):
            if v!=0:
                arr[i].insert(0,v)
    
    for m in moves:        
        if arr[m-1]:
            pick = arr[m-1].pop()
            if result:
                if result[-1] == pick:
                    answer+=2
                    result.pop()
                else :
                    result.append(pick)
            else :
                result.append(pick)
    
    
    return answer