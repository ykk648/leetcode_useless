# -- coding: utf-8 --
# @Time : 2023/7/10
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 46 全排列 （backtrack）
    def find_all_iters(self, nums):
        res = []

        def backtrack(nums_, tmp):
            if not nums_:
                res.append(tmp)
            for i in range(len(nums_)):
                backtrack(nums_[:i] + nums_[i + 1:], tmp + [nums_[i]])

        backtrack(nums, [])
        return res

    # 93 复原IP地址
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(s, idx, tmp):
            if idx > 4:
                return
            if idx == 4 and not s:
                res.append(tmp[:-1])
            for i in range(len(s)):
                if s[:i + 1] == '0' or (s[0] != '0' and 0 < int(s[:i + 1]) < 256):
                    backtrack(s[i + 1:], idx + 1, tmp + s[:i + 1] + '.')

        backtrack(s, 0, '')
        return res
