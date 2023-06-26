# -- coding: utf-8 --
# @Time : 2023/6/26
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 42 接雨水 (双指针)
    def trap(self, nums):
        res = 0
        left, right = 0, len(nums) - 1
        left_max, right_max = nums[left], nums[right]
        while left < right:
            if left_max <= right_max:
                left_max = max(left_max, nums[left])
                res += left_max - nums[left]
                left += 1
            else:
                right_max = max(right_max, nums[right])
                res += right_max - nums[right]
                right -= 1
        return res

    # 88 合并两个有序数组 （升序 双指针）
    def merge_list(self, list1, m1, list2, m2):
        p1, p2, tail = m1 - 1, m2 - 1, m1 + m2 - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                list1[tail] = list2[p2]
            elif p2 == -1:
                list1[tail] = list1[p1]
            elif list1[p1] < list2[p2]:
                list1[tail] = list2[p2]
                p2 -= 1
            else:
                list1[tail] = list1[p1]
                p1 -= 1
            tail -= 1
