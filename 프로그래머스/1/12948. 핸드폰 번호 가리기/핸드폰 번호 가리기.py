def solution(phone_number):
    answer = ''
    
    for i in range(0, len(phone_number)) :
        if i < len(phone_number)-4:
            answer = answer+"*"
        else :
            answer = answer+phone_number[i]
    
    return answer