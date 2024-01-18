def solution(a, b):
    answer = ''
    
    day=b-1
    
    for i in range(1,a) :
        if i==2 :
            day+=29
        elif i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            day+=31
        else:
            day+=30
                
    day=day%7

    
    if day==0:
        answer="FRI"
    elif day==1:
        answer="SAT"
    elif day==2:
        answer="SUN"
    elif day==3:
        answer="MON"
    elif day==4:
        answer="TUE"
    elif day==5:
        answer="WED"
    else:
        answer="THU"



    return answer