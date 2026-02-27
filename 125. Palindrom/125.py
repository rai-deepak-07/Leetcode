# Easy 
# Topics: Two Pointers, String

def isPalindrome(s):
    new_s = [c.lower() for c in s if c.isalnum()]
    return new_s == new_s[::-1]
 
# Input: A man, a plan, a canal: Panama
s = input() 
print(isPalindrome(s)) #True