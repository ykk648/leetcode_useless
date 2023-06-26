# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 20 有效的括号
    def quote_judge(self, s):
        dict_ = {']': '[', ')': '(', '}': '{'}
        stack = []
        for q in s:
            if stack and q in dict_:
                if stack[-1] == dict_[q]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(q)
        return not stack
