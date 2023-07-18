# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import collections
import math


class Traversal:
    # 144 前序遍历 94 中序遍历 145 后序遍历
    def order_recursion(self, root):
        if not root:
            return root
        # return [root.val] + self.order_recursion(root.left) + self.order_recursion(root.right)  # 前序
        # return self.order_recursion(root.left) + [root.val] + self.order_recursion(root.right)  # 中序
        return self.order_recursion(root.left) + self.order_recursion(root.right) + [root.val]  # 后序

    def order_iteration(self, root):
        res, stack, cur = [], [], root
        # 中序
        while stack or cur:
            while cur:
                # 左子树压栈
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        # 前序
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        # 后序
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        res = res[::-1]

        return res


class Solution:
    # 102 二叉树的层序遍历 （BFS）
    def vals_order(self, root):
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)
            vals = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                vals.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if vals:
                res.append(vals)

        return res

    # 102 二叉树的右视图 （BFS 层序遍历每层的最后一个
    def vals_order_right_view(self, root):
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)
            vals = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                vals.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if vals:
                res.append(vals[-1])

        return res

    # 130 二叉树的锯齿形遍历 （BFS）
    def zigzag_order(self, root):
        queue = collections.deque()
        queue.append(root)
        res = []
        zigzag_flag = False

        while queue:
            size = len(queue)
            vals = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                vals.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if vals:
                res.append(vals[::-1] if zigzag_flag else vals)
                zigzag_flag = not zigzag_flag

        return res

    # 236 二叉树的最近公共祖先 (recursion DFS
    def lowest_ancester(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowest_ancester(root.left, p, q)
        right = self.lowest_ancester(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    # 124 二叉树的最大路径和
    def max_sum(self, root):
        self.ans = -math.inf

        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            self.ans = max(left_max + right_max + node.val, self.ans)
            return max(max(left_max, right_max) + node.val, 0)

        dfs(root)
        return self.ans
