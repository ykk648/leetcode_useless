# -- coding: utf-8 --
# @Time : 2023/6/26
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 3 无重复字符的最长子串
    def length_of_substring(self, s):
        max_len, hashmap = 0, {}
        start = 0
        for end in range(1, len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:
                max_len = max(max_len, end - start)
            while len(hashmap) > end - start + 1:
                head = s[start]
                hashmap[head] -= 1
                if len(hashmap[head]) == 1:
                    del hashmap[head]
                start += 1
        return max_len
