# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 121 买卖股票的最佳时机 (DP
    def max_profit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
        return dp[-1]

    # 53 最大子序和
    def max_sum(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)

    # 300 最长上升子序列
    def max_length_ascending(self, nums):
        n = len(nums)
        if n == 0:
            return nums
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 5 最长回文子串 （二维DP）
    def max_sub_palindrome(self, s):
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
