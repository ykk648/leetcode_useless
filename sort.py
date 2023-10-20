# -- coding: utf-8 --
# @Time : 2023/9/8
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

class Solution:
    # 912 快排 （recursion divide&conquer 升序）
    def quick_sort(self, num_list):
        if len(num_list) == 0:
            return num_list
        pivot = random.choice(num_list)
        left = self.quick_sort([x for x in num_list if x < pivot])
        right = self.quick_sort([x for x in num_list if x > pivot])
        middle = [x for x in num_list if x == pivot]
        return left + middle + right

    # 912 堆排
    def heap_sort(self, num_list):
        def max_heap_adjust(arr, i, e):
            j = i * 2 + 1  # l_child
            while j <= e:
                r_child = j + 1
                if r_child <= e and arr[r_child] > arr[j]:
                    j += 1
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i = j
                    j = i * 2 + 1
                else:
                    break

        n = len(num_list)
        for i in range(n // 2 - 1, -1, -1):
            max_heap_adjust(num_list, i, n - 1)

        for j in range(n - 1, -1, -1):
            num_list[0], num_list[j] = num_list[j], num_list[0]
            max_heap_adjust(num_list, 0, j - 1)
        return num_list

    # 56 合并区间
    def merge2one(self, intervals):
        """
        :param intervals: [[1,3],[2,6],[8,10],[15,18]]
        :return: [[1,6],[8,10],[15,18]]
        """
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals[1:]:
            if ans[-1][1] < s:
                ans.append([s, e])
            else:
                ans[-1][1] = max(e, ans[-1][1])
        return ans
