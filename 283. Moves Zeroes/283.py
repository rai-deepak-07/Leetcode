# Easy 
# Topics: Array, Two Pointers

def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


# Input: 
# 0 1 0 3 12
nums = list(map(int, input().split()))  # [0, 1, 0, 3, 12]
result = moveZeroes(nums)

print(result)  # [1, 3, 12, 0, 0]
print(*result)  # 1 3 12 0 0
