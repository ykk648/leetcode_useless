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
