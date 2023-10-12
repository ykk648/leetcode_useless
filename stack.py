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

    # 394 字符串解码 "2[abc]3[cd]ef" -> "abcabccdcdcdef"
    def decodeString(self, s):
        """
        辅助栈，保存当前倍数和
        :param s:
        :return:
        """
        stack, res, multi = [], '', 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = '', 0
            elif c == ']':
                cur_multi, cur_res = stack.pop()
                res = cur_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


# 32 最长有效括号
def longestValidParentheses(self, s):
    stack, ans = [], 0
    for i in range(len(s)):
        if stack and s[i] == ')' and s[stack[-1]] == '(':
            stack.pop()
            ans = max(ans, i - (stack[-1] if stack else -1))
        else:
            stack.append(i)
    return ans


# 232 栈实现队列
class StackQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


# 155 最小栈
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1])))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
