# -- coding: utf-8 --
# @Time : 2023/6/29
# @Author : ykk648
# @Project : https://github.com/ykk648/leetcode_useless

# 146 LRU缓存 利用py3.7以后dict有序的特性（代替双向链表+hashmap）
class LruCache:
    def __init__(self, capacity):
        self.ht = {}
        self.capacity = capacity

    def get(self, key):
        s = self.ht.get(key, -1)
        if s != -1:
            self.ht.pop(key)
            self.ht[key] = s
        return s

    def put(self, key, value):
        if key in self.ht:
            self.ht.pop(key)
        elif len(self.ht) >= self.capacity:
            # O(1) 去除字典第一个值
            k = next(iter(self.ht))
            self.ht.pop(k)
        self.ht[key] = value


# class Solution:
#     def lru_cache(self, ):
