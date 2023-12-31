# -- coding: utf-8 --
# @Time : 2023/6/25
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Island:
    # 200 岛屿数量 (dfs 递归)
    def island_nums(self, grid):
        row, col, res = len(grid), len(grid[0]), 0

        # 定义一个dfs
        def dfs(x, y):
            grid[x][y] = '0'
            for nb in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= nb[0] < row and 0 <= nb[1] < col:
                    if grid[nb[0]][nb[1]] == '1':
                        dfs(*nb)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    dfs(x, y)
                    res += 1
        return res

    # 695 岛屿的最大面积
    def maxAreaOfIsland(self, grid):
        row, col, res = len(grid), len(grid[0]), 0

        self.count = 0

        def dfs(x, y):
            grid[x][y] = 0
            self.count += 1
            for nb in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= nb[0] < row and 0 <= nb[1] < col:
                    if grid[nb[0]][nb[1]] == 1:
                        dfs(*nb)
            return self.count

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    self.count = 0
                    res = max(res, dfs(x, y))
        return res
