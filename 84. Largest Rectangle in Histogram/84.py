# Hard
# Topics: Array, Stack, Monotonic Stack


def largestRectangleArea(heights):
    n = len(heights)
    pse = [-1] * n  #[-1, -1, -1, ....., n]
    nse = [n] * n   #[n, n, n,....., n]
    stack = []

    # Previous Smaller Element / Left Smallest Element
    for i in range(n):  # Left to Right
        
        # Pop elements from the stack until we find a smaller element or the stack is empty
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
            
        pse[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    # Next Smaller Element / Right Smallest Element
    for i in range(n - 1, -1, -1): # Right to Left
        
        # Pop elements from the stack until we find a smaller element or the stack is empty
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        
        nse[i] = stack[-1] if stack else n
        stack.append(i)

    max_area = 0
    for i in range(n):
        height = heights[i]
        width = nse[i] - pse[i] - 1
        max_area = max(max_area, height * width)

    return max_area


# Input:
# 2 1 5 6 2 3
heights = list(map(int, input().split()))   # [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))