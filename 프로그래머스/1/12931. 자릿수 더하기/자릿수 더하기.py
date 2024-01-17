def solution(n):
    answer = 0

    splitListN = list(map(int, str(n)))
    answer = sum(splitListN)

    return answer