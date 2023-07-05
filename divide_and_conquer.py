# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import random


class Solution:
    # 912 排序数组 （recursion divide&conquer 升序）
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

    # 33 搜索旋转排序数组 （O(logn)）
    def search_rotate_num(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
