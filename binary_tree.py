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

    # 101 对称二叉树 （recursion，自顶向下左右对比）
    def isSymmetric(self, root):
        if not root:
            return True

        def compare(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return compare(l.left, l.right) and compare(r.left, r.right)

        return compare(root.left, root.right)

    # 129 求根节点到叶子节点数字之和
    def sumNumbers(self, root):
        if not root:
            return 0

        def node_sum(root_, sum_):
            if not root_:
                return 0
            sum_ = sum_ * 10 + root_.val
            if not root_.left and not root_.right:
                return sum_
            return node_sum(root_.left, sum_) + node_sum(root_.right, sum_)

        return node_sum(root, 0)

    # 98 二叉搜索树 binary search tree （中序遍历+全局值判断）
    def isValidBTS(self, root):
        if not root:
            return True

        self.pre = -math.inf

        def BTS_check(root_):
            if not root_:
                return True
            if not BTS_check(root_.left):
                return False
            if root_.val <= self.pre:
                return False
            self.pre = root_.val
            return BTS_check(root_.right)

        return BTS_check(root)

    # 112 路径总和 （前序遍历+本地值判断）
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    # 113 路径总和2 （找出所有总和满足的路径）
    def pathSum(self, root, targetSum):
        if not root:
            return []

        path, res = [], []

        def path_search(root_, target_left):
            if not root_:
                return
            path.append(root_.val)
            if target_left == root_.val and not root_.left and not root_.right:
                res.append(path.copy())
            path_search(root_.left, target_left - root_.val)
            path_search(root_.right, target_left - root_.val)
            path.pop()

        path_search(root, targetSum)
        return res

    # 662 二叉树的最大宽度
    def widthOfBinaryTree(self, root):
        if not root:
            return 0


class RecursionTemplate(Solution):
    """
    二叉树的递归/回溯/DFS 236 226 104 543
    """

    def template(self, root):
        # 1.边界判断
        # 根节点
        if not root:
            return
        # 叶子结点
        if not root.left and not root.right:
            return

        # 2.初始化全局变量，如不需要全局变量，dfs函数即为本身
        self.res = []

        # 3.递归函数 自顶向下的DFS temp为辅助变量
        # temp为本地变量 跟随层级关系变化
        def dfs(root_, temp_):
            # 根节点前处理
            root_.val = 0
            # 递归结束条件
            if not root:
                return
            # 全局变量更新
            self.res.append(root_.val)
            # 左右子树递归
            dfs(root_.left, temp_)
            dfs(root_.right, temp_)
            # 叶子结点后处理
            temp_ = []

        # 4.递归和返回
        dfs(root, [])
        return self.res

    # 236 二叉树的最近公共祖先 (DFS找两个节点，向上递归到祖先
    def lowestCommonAncester(self, root, p, q):
        # 找到节点，递归结束，找不到返回None
        if not root or root == p or root == q:
            return root
        # 递归左右子树
        left = self.lowestCommonAncester(root.left, p, q)
        right = self.lowestCommonAncester(root.right, p, q)
        # 返回找到节点的子树
        if not left:
            return right
        if not right:
            return left
        return root

    # 226 翻转二叉树
    def invertTree(self, root):
        if not root:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

    # 104 二叉树的最大深度
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 543 二叉树的直径 （左右子树拉平，一起算）
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        self.max_depth = 0

        def depth(root_):
            if not root_:
                return 0
            left_depth = depth(root_.left)
            right_depth = depth(root_.right)
            self.max_depth = max(self.max_depth, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.max_depth
