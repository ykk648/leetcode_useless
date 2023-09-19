# -- coding: utf-8 --
# @Time : 2023/6/26
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import collections
import math


class Solution:
    # 3 无重复字符的最长子串 求长度
    def length_of_substring(self, s):
        max_len, hashmap = 0, {}
        start = 0
        for end in range(1, len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:
                max_len = max(max_len, end - start + 1)
            while len(hashmap) < end - start + 1:
                head = s[start]
                hashmap[head] -= 1
                if len(hashmap[head]) == 1:
                    del hashmap[head]
                start += 1
        return max_len

    # 76 最小覆盖子串
    def minWindow(self, s, t):
        def check(a, b):
            return all(a.get(k, -1) >= v for k, v in b.items())

        res, min_len = "", math.inf
        hash, hash_t = {}, {}
        for ch in t:
            hash_t[ch] = hash_t.get(ch, 0) + 1

        start = 0

        for end in range(len(s)):
            tail = s[end]
            hash[tail] = hash.get(tail, 0) + 1

            while check(hash, hash_t):
                if end - start + 1 < min_len:
                    res = s[start:end + 1]
                    min_len = len(res)
                head = s[start]
                hash[head] -= 1
                if hash[head] == 0:
                    del hash[head]
                start += 1
        return res

    # 239 滑动窗口最大值
    def maxSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        res = []
        queue = collections.deque()
        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
