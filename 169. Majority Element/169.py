# Easy 
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

def majorityElement(nums):
    nums.sort()     # [1,1,1,2,2,2,2]
    return nums[len(nums)//2]
        
# Inupt: 2 2 1 1 1 2 2
nums = list(map(int, input().split()))  # [2,2,1,1,1,2,2]
print(majorityElement(nums))    # Output: 2