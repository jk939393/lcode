#1768. Merge Strings Alternately
def mergeAlternately(word1: str, word2: str) -> str:
    a= len(word1)
    b =len(word2)
    length = max(len(word1), len(word2))
    merged = ''
    for i in range(length):
        print(i)
        if i < a:
            merged = merged + word1[i]
        if i < b:
            merged = merged + word2[i]
    return merged
word1 ='abcd'
word2='pq'
m =mergeAlternately(word1,word2)

print(m)