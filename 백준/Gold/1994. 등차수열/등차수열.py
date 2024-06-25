def longest_arithmetic_subsequence(nums):
    if not nums:
        return 0

    nums.sort()
    n = len(nums)
    dp = [{} for _ in range(n)]
    max_length = 1

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            max_length = max(max_length, dp[i][diff])

    return max_length


# 입력
N = int(input().strip())
nums = [int(input().strip()) for _ in range(N)]

# 출력
print(longest_arithmetic_subsequence(nums))
