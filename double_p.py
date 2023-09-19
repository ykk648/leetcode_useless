# -- coding: utf-8 --
# @Time : 2023/6/26
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 704 二分查找
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

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

    # 415 字符串相加
    def str_sum(self, num1, num2):
        p1, p2, carry, res = len(num1) - 1, len(num2) - 1, 0, ''
        while p1 >= 0 or p2 >= 0:
            n1 = num1[p1] if p1 >= 0 else 0
            n2 = num2[p2] if p2 >= 0 else 0
            sum_ = int(n1) + int(n2) + carry
            carry = sum_ // 10
            res = str(sum_ % 10) + res
            p1 -= 1
            p2 -= 1
        if carry > 0:
            res = '1' + res
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

    # 15 三数之和
    def three_sum(self, nums):
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res

    # 31 下一个排列 （下一个字典序列的更大值）
    def nextPermutation(self, nums):
        n = len(nums)
        if n < 1:
            return

        # 逆序找到第一个小值
        modify = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                modify = i
                break

        if modify == -1:
            # 无小值全翻转
            nums[:] = nums[::-1]
        else:
            # 逆序找到第一个比小值大的值
            target = -1
            for i in range(n - 1, modify, -1):
                if nums[i] > nums[modify]:
                    target = i
                    break
            # exchange
            nums[modify], nums[target] = nums[target], nums[modify]
            # 小值后翻转 （降序变升序）
            nums[modify + 1:] = nums[modify + 1:][::-1]

    # 165 比较版本号
    def compareVersion(self, version1, version2):
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            a = b = 0
            while i < m and version1[i] != '.':
                a = 10 * a + int(version1[i])
                i += 1
            while j < n and version1[j] != '.':
                b = 10 * b + int(version2[j])
                j += 1
            if a > b:
                return 1
            elif a < b:
                return -1
            i += 1
            j += 1
        return 0

    # 151 翻转字符串中的单词
    def reverseWords(self, s):
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1:j + 1])
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)