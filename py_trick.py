# -- coding: utf-8 --
# @Time : 2023/9/11
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import re


class Solution:
    def myAtoi(self, s):
        patten = r'^[\+\-]?\d+'
        re_ = re.compile(patten)

        s = s.lstrip()
        num = int(*re_.findall(s))
        return max(min(num, 2 ** 31 - 1), -2 ** 31)
