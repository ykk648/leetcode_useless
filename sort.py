# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/AI_power
import random


class Solution:
    # 912 排序数组
    def quick_sort(self, num_list):
        if len(num_list) == 0:
            return num_list
        pivot = random.choice(num_list)
        left = self.quick_sort([x for x in num_list if x < pivot])
        right = self.quick_sort([x for x in num_list if x > pivot])
        middle = [x for x in num_list if x == pivot]
        return left + middle + right

    # 215 数组第K个最大元素
    def get_k_max(self, num_list, k):
        num_list = self.quick_sort(num_list)
        return num_list[-k]
