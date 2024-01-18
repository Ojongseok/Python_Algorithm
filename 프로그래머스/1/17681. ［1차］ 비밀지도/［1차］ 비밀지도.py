def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        num1 = bin(arr1[i])[2:].zfill(n)
        num2 = bin(arr2[i])[2:].zfill(n)
        st=""
        for j in zip(num1,num2):
            if '1' in j:
                st+="#"
            else :
                st+=" "
        answer.append(st)
    
    return answer