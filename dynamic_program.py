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

    # 70 爬楼梯
    def climb_stairs(self, n):
        if n <= 1:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
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

    # 1143 最长公共子序列
    def max_common_sequence(self, text1, text2):
        n1, n2 = len(text1) + 1, len(text2) + 1
        dp = [[0] * n2 for _ in range(n1)]

        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

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

    # 72 编辑距离
    def min_dis(self, word1, word2):
        n1, n2 = len(word1) + 1, len(word2) + 1
        dp = [[0] * n1 for _ in range(n2)]

        for i in range(n1):
            dp[i][0] = i
        for i in range(n2):
            dp[0][i] = i
        for i in range(1, n1):
            for j in range(1, n2):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j])
        return dp[-1][-1]


class KnapsackProblem:
    # 322 零钱兑换 （返回最小硬币数量）
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1

    # 518 零钱兑换2 （返回组合数）
    def coinChange2(self, coins, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]
