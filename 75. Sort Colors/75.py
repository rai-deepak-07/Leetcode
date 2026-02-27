# Medium
# Topic: Array, Two Pointers, Sorting

def sortColors(nums):
    low, mid = 0, 0
    high = len(nums) - 1
    while(mid <= high):
        if(nums[mid] == 0):
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif(nums[mid] == 1):
            mid += 1
        elif(nums[mid] == 2):
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
    return nums


# Input: 2 1 0 1 2 0

numbers = list(map(int, input().split()))   # [2, 1, 0, 1, 2, 0]

print(sortColors(numbers))  # [0, 0, 1, 1, 2, 2]
print(*sortColors(numbers))  # 0 0 1 1 2 2