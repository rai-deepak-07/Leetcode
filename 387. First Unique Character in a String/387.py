# Easy 
# Topics: Junior, Hash Table, String, Queue, Counting

def firstUniqChar(s):
    hmap = {}
    for c in s:
        hmap[c] = hmap.get(c, 0) + 1

    for i in range(len(s)):
        if(hmap[s[i]] == 1):
            return i
    return -1

# Input: s = "leetcode"

s = input()
print(firstUniqChar(s))     # 0