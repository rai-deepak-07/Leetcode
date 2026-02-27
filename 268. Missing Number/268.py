# Easy 
# Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    n = len(nums)
    if(nums[n - 1] != n):
        return n
    elif(nums[0] != 0):
        return 0
        
    for i in range(1, n):
        next = nums[i-1] + 1
        if(nums[i] != next):
            return next       
    return -1
    
# Input: 3 0 1
# Output: 2

values = list(map(int, input().split())) # [3, 0, 1]
print(missingNumber(values))  # 2