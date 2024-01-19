def solution(answers):
    answer = []
    
    answer_1 = [1,2,3,4,5] # 5
    answer_2 = [2,1,2,3,2,4,2,5] # 8
    answer_3 = [3,3,1,1,2,2,4,4,5,5] # 10
    
    an = [0 for i in range(3)]
    
    for i, v in enumerate(answers) :
        if v == answer_1[i%5]:
            an[0]+=1
        if v== answer_2[i%8]:
            an[1]+=1
        if v==answer_3[i%10]:
            an[2]+=1
        
    top = max(an)
    
    answer = [i+1 for i,v in enumerate(an) if v == top]
    
    return answer