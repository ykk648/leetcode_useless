# -- coding: utf-8 --
# @Time : 2023/7/10
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 54 螺旋矩阵
    def spiral_order(self, matrix):
        res = []
        while matrix:
            res.append(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res

    # (state machine)
    def spiral_order_state(self, matrix):
        if not matrix or not matrix[0]:
            return matrix

        row, col = len(matrix), len(matrix[0])
        x, y = 0, 0  # 坐标
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 方向
        left, right, top, bottom = 0, col - 1, 0, row - 1  # 边界
        cur_d = 0  # 方向index
        res = []

        while len(res) != row * col:
            res.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                top += 1
            elif cur_d == 1 and x == bottom:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                bottom -= 1
            elif cur_d == 3 and x == top:
                cur_d += 1
                left += 1

            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res
