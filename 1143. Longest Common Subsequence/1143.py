# Medium
# Topics: String, Dynamic Programming

def longestCommonSubsequence(text1, text2):
    row, col = len(text1), len(text2)
    dp = [[0] * (col + 1) for _ in range(row + 1)]
        
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[row][col]

# Inputs: text1 = "abcde", text2 = "ace" 

text1 = input()
text2 = input()

print(longestCommonSubsequence(text1, text2))  # 3