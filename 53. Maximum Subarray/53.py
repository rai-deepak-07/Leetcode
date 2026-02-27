# Medium
# Array, Divide and Conquer, Dynamic Programming

def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Input: -2 1 -3 4 -1 2 1 -5 4
nums = list(map(int, input().split()))  # [-2,1,-3,4,-1,2,1,-5,4]

# [4, -1, 2, 1] has the largest sum = 6.
print(maxSubArray(nums))