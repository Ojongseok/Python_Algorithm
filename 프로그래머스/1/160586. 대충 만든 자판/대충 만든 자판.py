def solution(keymap, targets):
    answer = []
    
    for i in range(len(targets)):
        min_touch=0
        for c in targets[i]:
            
            arr_index = [x.find(c) for x in keymap]
            arr_index = [x for x in arr_index if x!=-1]
            
            if not arr_index:
                min_touch=-1
                break
            else :
                min_touch+=(min(arr_index)+1)
        answer.append(min_touch)
            
    
    return answer