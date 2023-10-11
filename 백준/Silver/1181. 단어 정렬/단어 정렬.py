n = int(input())
wordArr = [input() for _ in range(n)]
wordDict = set(wordArr)

sortedWordDict = sorted(wordDict, key=lambda x : (len(x), x))


for i in sortedWordDict : 
    print(i)