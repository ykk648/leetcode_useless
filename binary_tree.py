# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless
import collections
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traversal:
    # 144 前序遍历 94 中序遍历 145 后序遍历
    def order_recursion(self, root):
        if not root:
            return []
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

    # 104 二叉树的最大深度
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 105 从前序和中序构造二叉树
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root

    # 110 平衡二叉树
    def isBalanced(self, root):
        def depth(root_):
            if not root_:
                return 0
            left = depth(root_.left)
            if left == -1:
                return -1
            right = depth(root_.right)
            if right == -1:
                return -1
            return max(left, right) if abs(left - right) <= 1 else -1

        return depth(root) != -1

    # 543 二叉树的直径
    def diameterOfBinaryTree(self, root):
        self.max_depth = 0

        def depth(root_):
            if not root_:
                return 0
            left = depth(root_.left)
            right = depth(root_.right)
            self.max_depth = max(self.max_depth, left + right)
            return max(left, right) + 1

        depth(root)
        return self.max_depth
