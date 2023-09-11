# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import random


class Solution:

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

    # 4 寻找两个正序数组中位数
    def findMedianSortedArrays(self, nums1, nums2):
        def find_k_min(nums1, nums2, k):
            if not nums2:
                return nums1[k - 1]
            if not nums1:
                return nums2[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            t = min(len(nums1), len(nums2), k // 2)  # divide 二分
            if nums1[t - 1] < nums2[t - 1]:
                return find_k_min(nums1[t:], nums2, k - t)
            else:
                return find_k_min(nums1, nums2[t:], k - t)

        m, n = len(nums1), len(nums2)
        k1 = (m + n + 1) // 2
        k2 = (m + n + 2) // 2
        # 中位数等于第k1小和k2小的均值
        return (find_k_min(nums1, nums2, k1) + find_k_min(nums1, nums2, k2)) / 2

    # 69 x的平方根
    def mySqrt(self, x):
        l, h, ans = 0, x, -1
        while l <= h:
            mid = l + (h - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans
