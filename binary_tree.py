# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import collections


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
