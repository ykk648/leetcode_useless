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
                self.stack.append((val,val))
            else:
                self.stack.append((val, min(self.stack[-1][1])))

        def pop(self):
            self.stack.pop()

        def top(self):
            return self.stack[-1][0]

        def getMin(self):
            return self.stack[-1][1]