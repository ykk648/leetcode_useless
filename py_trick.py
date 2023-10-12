# -- coding: utf-8 --
# @Time : 2023/9/11
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import re


class Solution:
    # 8 字符串转换整数
    def myAtoi(self, s):
        patten = r'^[\+\-]?\d+'
        re_ = re.compile(patten)

        s = s.lstrip()
        num = int(*re_.findall(s))
        return max(min(num, 2 ** 31 - 1), -2 ** 31)

    # 43 字符串相乘
    def multiply(self, num1, num2):
        res = 0
        f1 = 1
        for i in range(len(num1) - 1, -1, -1):
            f2 = 1
            n1 = f1 * int(num1[i])
            for j in range(len(num2) - 1, -1, -1):
                n2 = f2 * int(num2[j])
                res += n1 * n2
                f2 *= 10
            f1 *= 10
        return str(res)

    # 470 用rand(7)实现rand(10)
    def rand10(self):
        """
        (randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数
        :return:
        """

        def rand7():
            return 0

        num = (rand7() - 1) * 7 + rand7()
        while num > 40:
            num = (rand7() - 1) * 7 + rand7()
        return 1 + num % 10
