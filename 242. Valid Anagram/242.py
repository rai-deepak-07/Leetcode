# Easy
# Topics: Hash Table, String, Sorting

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    for i in s:
        if s.count(i) != t.count(i):
            return False 
    return True


# s = "anagram", t = "nagaram"
s = input()
t = input()

print(isAnagram(s, t))  # True