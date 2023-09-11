# -- coding: utf-8 --
# @Time : 2023/7/10
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 46 全排列 （dfs）
    def find_all_iters(self, nums):
        res = []

        def dfs(nums_, tmp):
            if not nums_:
                res.append(tmp)
            for i in range(len(nums_)):
                dfs(nums_[:i] + nums_[i + 1:], tmp + [nums_[i]])

        dfs(nums, [])
        return res

    # 93 复原IP地址
    def restoreIpAddresses(self, s):
        res = []

        def dfs(s, idx, tmp):
            if idx > 4:
                return
            if idx == 4 and not s:
                res.append(tmp[:-1])
            for i in range(len(s)):
                if s[:i + 1] == '0' or (s[0] != '0' and 0 < int(s[:i + 1]) < 256):
                    dfs(s[i + 1:], idx + 1, tmp + s[:i + 1] + '.')

        dfs(s, 0, '')
        return res

    # 22 括号生成
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left:
                return
            if len(paths) == n * 2:
                res.append(paths)
                return
            dfs(paths + '(', left + 1, right)
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res
