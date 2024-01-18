def solution(sizes):
    answer = 0
    
    w = [x[0] for x in sizes]
    h = [x[1] for x in sizes]
    
    for i in range(len(w)):
        if w[i] < h[i]:
            w[i],h[i]=h[i],w[i]
        
    answer = max(w)*max(h)
    
    return answer