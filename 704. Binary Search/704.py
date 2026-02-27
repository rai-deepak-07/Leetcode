# Easy
# Topics: Array, Binary Search

def search(nums, target):
    low = 0
    high = len(nums) - 1

    while(low <= high):
        mid = low + (high - low) // 2
        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Input: 
# -1 0 3 5 9 12 
# 9
    
nums = list(map(int, input().split()))  # [-1, 0, 3, 5, 9, 12]
target = int(input())   # 9

print(search(nums, target)) # 4